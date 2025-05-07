import pandas as pd


def min_max_normalize(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize the float columns of the DataFrame using Min-Max normalization.

    Parameters:
    - df (pd.DataFrame): The input DataFrame to normalize.

    Returns:
    - pd.DataFrame: A new DataFrame with normalized float columns.
    """
    # Create a copy of the original DataFrame to avoid modifying it
    normalized_df = df.copy()

    # Identify float columns
    float_cols = normalized_df.select_dtypes(include=['float']).columns

    # Apply Min-Max normalization
    for col in float_cols:
        min_val = normalized_df[col].min()
        max_val = normalized_df[col].max()
        normalized_df[col] = (normalized_df[col] - min_val) / (max_val - min_val)

    return normalized_df


def min_max_only_ppi(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize the float columns of the DataFrame using Min-Max normalization.

    Parameters:
    - df (pd.DataFrame): The input DataFrame to normalize.

    Returns:
    - pd.DataFrame: A new DataFrame with normalized float columns.
    """
    # Create a copy of the original DataFrame to avoid modifying it
    normalized_df = df.copy()

    # Identify float columns
    float_cols = normalized_df.select_dtypes(include=['float']).columns

    # Apply Min-Max normalization
    for col in float_cols:
        # only for columns that the name has '_'
        if col.find('_') != -1:
            min_val = normalized_df[col].min()
            max_val = normalized_df[col].max()
            normalized_df[col] = (normalized_df[col] - min_val) / (max_val - min_val)

    return normalized_df
