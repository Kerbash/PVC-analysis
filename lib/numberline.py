import numpy as np
import seaborn as sns


def create_numberline(X, y, title='Numberline Visualization', figsize=(8, 2), class_key=None):
    """
    Create a minimalist numberline visualization with points colored by class.

    Parameters:
    -----------
    X : numpy.ndarray
        Numerical values to plot (2D array with a single column)
    y : numpy.ndarray
        Binary or multi-class labels for coloring the points
    title : str, optional
        Title of the plot (default is 'Numberline Visualization')
    figsize : tuple, optional
        Figure size (width, height) in inches (default is (8, 2))

    Returns:
    --------
    matplotlib.figure.Figure
        The created figure object
    """
    import matplotlib.pyplot as _plt
    # Ensure X is a 2D NumPy array and flatten to 1D
    if isinstance(X, np.ndarray) and X.ndim == 2 and X.shape[1] == 1:
        x_values = X.flatten()
    else:
        raise ValueError("X must be a 2D NumPy array with a single column")

    # Ensure y is a NumPy array
    y = np.asarray(y)

    # Validate input shapes
    if len(x_values) != len(y):
        raise ValueError("X and y must have the same number of samples")

    # Create a new figure with no border
    fig, ax = _plt.subplots(figsize=figsize)
    ax.set_facecolor('none')

    # Remove all spines (borders)
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Get unique classes and create a color palette
    unique_classes = np.unique(y)

    # Use a color-blind friendly palette
    if len(unique_classes) <= 2:
        # Binary case: use red and blue for clear distinction
        palette = ['#1E90FF', '#FF6347']  # dodgerblue and tomato
    else:
        # For more than 2 classes, use a colorblind-friendly palette
        palette = sns.color_palette("colorblind", len(unique_classes))

    # Create color mapping
    color_dict = dict(zip(unique_classes, palette))

    # Plot the base numberline (thin line at 0)
    ax.axhline(y=0, color='gray', linewidth=0.5, alpha=0.5)

    # Create colors and markers list based on the classes
    colors = [color_dict[cls] for cls in y]

    # Plot points on the numberline
    ax.scatter(x_values, [0] * len(x_values), c=colors, s=100, alpha=0.7,
               edgecolors='black', linewidth=1)

    # Customize the plot
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_xlabel('Values', fontsize=10)
    ax.set_yticks([])  # Remove y-axis ticks

    # Add a legend
    if class_key:
        handles = [ax.scatter([], [], c=color_dict[cls], label=f'{class_key[cls]}',
                              edgecolors='black', linewidth=1)
                   for cls in unique_classes]
    else:
        handles = [ax.scatter([], [], c=color_dict[cls], label=f'{cls}',
                              edgecolors='black', linewidth=1)
                   for cls in unique_classes]
    ax.legend(handles=handles, title='Classes', loc='upper right', fontsize=8)

    # Adjust layout and return the figure
    _plt.tight_layout()
    return fig