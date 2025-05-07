import pandas as pd

def find_protein_conc_pair(df1: pd.DataFrame,
                           df2: pd.DataFrame,
                           threshold: float,
                           column_name: str = 'protein conc',
                           paired_df: pd.DataFrame = None,
                           start_pair_num: int = 0):
    """
    Find pairs of rows between two DataFrames where values in column_name
    are within a threshold *of their midpoint*.

    Args:
        df1, df2: DataFrames to pair
        threshold: maximum allowed relative difference to midpoint
                   (e.g. 0.2 for ±20%)
        column_name: name of the concentration column
        paired_df: existing DataFrame to append to (or None)
        start_pair_num: integer to start numbering pairs

    Returns:
        (paired_df, next_pair_num)
    """
    if paired_df is None:
        paired_df = pd.DataFrame()
    current_pair_num = start_pair_num
    df2_copy = df2.copy()

    for _, row1 in df1.iterrows():
        if df2_copy.empty:
            break

        value1 = row1[column_name]
        # find closest by absolute distance
        closest_pos = (df2_copy[column_name] - value1).abs().argsort().iloc[0]
        closest_row = df2_copy.iloc[closest_pos].copy()
        closest_idx = df2_copy.index[closest_pos]

        value2 = closest_row[column_name]
        mid = (value1 + value2) / 2
        if mid == 0:
            # avoid division by zero; skip if both are zero
            continue

        diff_ratio = abs(value1 - value2) / mid
        if diff_ratio > threshold:
            # outside ±threshold of the midpoint
            continue

        # drop matched row so it can't be reused
        df2_copy = df2_copy.drop(closest_idx)

        # tag and append both rows
        for r in (row1, closest_row):
            r_copy = r.copy()
            r_copy['pair num'] = current_pair_num
            paired_df = pd.concat([paired_df, pd.DataFrame([r_copy])], ignore_index=False)

        current_pair_num += 1

    return paired_df, current_pair_num
