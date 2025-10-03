import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Ellipse

from lib.constant import RESPONSE_TYPE_KEY, META_DATA_COLUMNS
from lib.normalizer import min_max_only_ppi

"""
HELPER FOR CREATING A GRAPH

EXAMPLE USAGE:
from lib.graph_plot import create_ppi_network, plot_ppi_network, get_network_stats

# Load and create network
df = pd.read_csv('data/01_Sig_Feature_output/norm_mean_important_array.csv', index_col=0)
# Create a PPI network
G = create_ppi_network(df, weight_threshold=0.007)
print(G)

# Plot network
fig = plot_ppi_network(G, title="Normalized PPI Importance for RF Identifying Negative Response (Threshold=0.007)")
# save the figure
fig.savefig('data/01_Sig_Feature_output/norm_ppi_network.png')
plt.show()

# Print network statistics
stats = get_network_stats(G)
for key, value in stats.items():
    print(f"{key}: {value}")
"""


def plot_pairs(_df, _pair_dict, target, title):
    # normalize and PCA the data
    _df = min_max_only_ppi(_df)
    # drop all except PPI (columns with "_" in the name)
    norm_used_ppi = _df.filter(regex='_')

    pca = PCA(n_components=2)
    pca.fit(norm_used_ppi)
    pca_used_df = pd.DataFrame(pca.transform(norm_used_ppi), columns=['PC1', 'PC2'])
    pca_used_df.index = norm_used_ppi.index
    # add the response type (for those indexes that exist)
    pca_used_df[target] = _df[target]

    # plot the pca with the pairs
    _plt = pca_with_cluster_graph(pca_used_df,
                                  title=title,
                                  style=None,
                                  hue=target,
                                  normalize=False)

    return _plt


def plot_ellipse(ax, X_pca, label_indices, color):
    """
    Adds an ellipse to the current plot based on the PCA data points.
    :param ax: matplotlib axis object
    :param X_pca: The PCA-transformed data
    :param label_indices: Boolean mask for the data points in this category
    :param color: The color of the ellipse
    """
    subset = X_pca[label_indices]

    # Only plot ellipse if we have enough points
    if len(subset) < 2:
        return

    # Calculate the covariance matrix and means of the data points
    cov = np.cov(subset, rowvar=False)
    mean = np.mean(subset, axis=0)

    # Eigenvalues and eigenvectors for the ellipse orientation
    eigenvals, eigenvecs = np.linalg.eigh(cov)

    # Sort eigenvectors by eigenvalues
    order = eigenvals.argsort()[::-1]
    eigenvals, eigenvecs = eigenvals[order], eigenvecs[:, order]

    # Get the angle of the ellipse rotation in degrees
    angle = np.degrees(np.arctan2(*eigenvecs[:, 0][::-1]))

    # Width and height of the ellipse based on the eigenvalues
    width, height = 2 * np.sqrt(eigenvals)

    # Add an ellipse to the plot with a more transparent background and thicker, more opaque outline
    ellipse = Ellipse(
        xy=mean,
        width=width,
        height=height,
        angle=angle,
        facecolor=color,
        edgecolor=color,
        alpha=0.1,  # Background transparency
        linewidth=2,  # Thicker outline
        linestyle='-',  # Solid line for the outline
        fill=True  # Ensure the ellipse is filled
    )
    ellipse.set_edgecolor((color[0], color[1], color[2], 1))  # Make the outline more opaque
    ax.add_patch(ellipse)


def pca_with_cluster_graph(x,
                           title='PCA plot of CART data',
                           drop_columns=None,
                           hue='patient',
                           style='response type',
                           draw_ellipses=True,
                           label_points=False,
                           dot_size=50,
                           normalize=True,
                           return_pca=False,
                           palette={0.0: 'red', 1.0: 'green'}
                           ):
    """
    This function creates a PCA plot of the data with optional clustering and ellipses.

    :param x: dataframe
    :param title: the title of the plot
    :param drop_columns: columns to drop from the dataframe
    :param hue: the column to use for point colors
    :param style: the column to use for point styles
    :param draw_ellipses: boolean flag to determine if ellipses should be drawn
    :param label_points: boolean flag to determine if points should be labeled
    :param dot_size: the size of the dots on the plot
    :param normalize: boolean flag to determine if the data should be normalized
    :param return_pca: boolean flag to determine if the PCA object should be returned
    :return: None (displays the plot)
    """
    scaler = StandardScaler()

    # Handle drop columns
    if drop_columns is None:
        drop_columns = META_DATA_COLUMNS

    data_for_pca = x.copy()
    plot_kwargs = {}
    category_data = {}

    # Process hue and style
    for category_type, category_name in [('hue', hue), ('style', style)]:
        if category_name:
            if category_name == 'response type':
                # if its response type map it to known values
                category_data[category_type] = x[category_name].map(RESPONSE_TYPE_KEY)
            else:
                category_data[category_type] = x[category_name]

            plot_kwargs[category_type] = category_data[category_type].astype('category')

    # Drop all necessary columns for PCA
    columns_to_drop = drop_columns + [col for col in [hue, style] if col is not None]
    columns_to_drop = list(set(columns_to_drop))  # Remove duplicates
    data_for_pca = data_for_pca.drop(columns_to_drop, axis=1, errors='ignore')

    # Perform PCA
    if normalize:
        x_transform = scaler.fit_transform(data_for_pca)
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(x_transform)
    else:
        X_pca = data_for_pca.values

    # Create plot
    plt.figure(figsize=(10, 10))
    ax = plt.gca()

    # Plot data points
    sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], ax=ax, s=dot_size, palette=palette, **plot_kwargs)

    # if we are doing ellipses and have a custom palette
    if draw_ellipses:
        categories = plot_kwargs['hue'].cat.categories
        colors = [palette.get(cat, c) for cat, c in
                  zip(categories, sns.color_palette())] if palette else sns.color_palette()

        for category, color in zip(categories, colors):
            # Convert color name to RGB tuple if it's a string
            if isinstance(color, str):
                color = plt.cm.colors.to_rgba(color)
            label_indices = plot_kwargs['hue'] == category
            plot_ellipse(ax, X_pca, label_indices, color)

    # set no background color but grid to black
    ax.set_facecolor('white')
    ax.grid(color='black', linestyle='-', linewidth=0.25)

    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.title(title)
    plt.legend(framealpha=0.5)

    if return_pca:
        # assemble the pca df and return it
        pca_df = pd.DataFrame(X_pca, columns=['PC1', 'PC2'], index=x.index)
        return plt, pca_df
    else:
        return plt


def pca_graph(x,
              title='PCA plot of CART data',
              drop_columns=None,
              hue='patient',
              style='response type',
              label_points=False):
    """
    This function takes in a dataframe and plots a PCA graph of the data. The function will standardize the data and

    :param x: dataframe
    :param title: the title of the plot
    :param drop_columns: the columns to drop from the dataframe if drop none [] otherwise default will be used,
                        both hue and style columns will be dropped
    :param hue: the column to use for the hue
    :param style: the column to use for the style
    :param label_points: boolean flag to determine if points should be labeled
    :return: a PCA plot
    """
    scaler = StandardScaler()

    # grab the hue and style columns values
    kwargs = {}
    # see if we are doing hue
    if hue:
        if hue == 'response type':
            x[hue] = x[hue].map(RESPONSE_TYPE_KEY)
        kwargs['hue'] = x[hue].astype('category')
        # drop the hue column
        x = x.drop(hue, axis=1)

    # Handling style
    if style:
        if style == 'response type':
            x[style] = x[style].map(RESPONSE_TYPE_KEY)
        kwargs['style'] = x[style].astype('category')
        x = x.drop(style, axis=1)

    # drop columns
    if drop_columns is None:
        drop_columns = META_DATA_COLUMNS
    if len(drop_columns) > 0:
        # drop the columns that exist in the dataframe
        x = x.drop(columns=drop_columns, errors='ignore')

    x = scaler.fit_transform(x)

    # PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(x)

    # plot
    plt.figure(figsize=(10, 10))
    sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], **kwargs)
    # if we are labeling points
    if label_points:
        for i, txt in enumerate(x.index):
            plt.annotate(txt, (X_pca[i, 0], X_pca[i, 1]))
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.title(title)
    #  make the legend 50% opaque
    plt.legend(framealpha=0.5)
    return plt