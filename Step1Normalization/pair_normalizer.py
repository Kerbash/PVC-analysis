import numpy as np
import pandas as pd


def pair_normalizer_midpoint(sample, control):
    """
    Normalize a pair of samples by subtracting the midpoint for columns with '_' in the name.
    Other columns are kept unchanged.

    Args:
        sample: A pandas Series representing the sample data
        control: A pandas Series representing the control data

    Returns:
        A pandas DataFrame with normalized sample and control rows
    """
    # Create copies to avoid modifying original data
    sample_norm = sample.copy()
    control_norm = control.copy()

    # Find all PPI columns (columns with '_' in the name)
    ppi_cols = [col for col in sample.index if '_' in str(col)]

    # Only normalize PPI columns by subtracting midpoint
    for col in ppi_cols:
        midpoint = (sample[col] + control[col]) / 2
        sample_norm[col] = sample[col] - midpoint
        control_norm[col] = control[col] - midpoint

    # Create DataFrame with both normalized rows
    norm_df = pd.DataFrame([sample_norm, control_norm])
    norm_df.index = [sample.name, control.name]

    return norm_df


def pair_normalizer_log2fold(sample, control):
    """
    Normalize a pair of samples by calculating log2 fold change for columns with '_' in the name.
    Handles zeros and negative values safely. Other columns are kept unchanged.

    Args:
        sample: A pandas Series representing the sample data
        control: A pandas Series representing the control data

    Returns:
        A pandas DataFrame with normalized sample and control rows
    """
    # Create copies to avoid modifying original data
    sample_norm = sample.copy()
    control_norm = control.copy()

    # Find all PPI columns (columns with '_' in the name)
    ppi_cols = [col for col in sample.index if '_' in str(col)]

    # Apply log2 fold change normalization only to PPI columns
    for col in ppi_cols:
        # Handle potential zeros and negative values
        # Add a small epsilon to avoid division by zero and log of zero/negative
        epsilon = 1e-10

        # For sample: calculate log2(sample/control) with safety handling
        if control[col] == 0:
            # If control is zero, use a large value based on sign of sample
            if sample[col] > 0:
                sample_norm[col] = 10.0  # Large positive value
            elif sample[col] < 0:
                sample_norm[col] = -10.0  # Large negative value
            else:
                sample_norm[col] = 0.0  # Both are zero
        else:
            # Safe log2 fold calculation with sign preservation
            ratio = sample[col] / (control[col] if control[col] != 0 else epsilon)
            if ratio > 0:
                sample_norm[col] = np.log2(np.abs(ratio) + epsilon)
            elif ratio < 0:
                sample_norm[col] = -np.log2(np.abs(ratio) + epsilon)
            else:
                sample_norm[col] = 0.0

        # For control: always set to zero
        control_norm[col] = 0.0

    # Create DataFrame with both normalized rows
    norm_df = pd.DataFrame([sample_norm, control_norm])
    norm_df.index = [sample.name, control.name]

    return norm_df


def pair_normalizer_zero_control(sample, control):
    """
    Normalize a pair of samples by setting control to zero and subtracting control value
    from sample for columns with '_' in the name. Other columns are kept unchanged.

    Args:
        sample: A pandas Series representing the sample data
        control: A pandas Series representing the control data

    Returns:
        A pandas DataFrame with normalized sample and control rows
    """
    # Create copies to avoid modifying original data
    sample_norm = sample.copy()
    control_norm = control.copy()

    # Find all PPI columns (columns with '_' in the name)
    ppi_cols = [col for col in sample.index if '_' in str(col)]

    # For PPI columns, set control to zero and subtract control value from sample
    for col in ppi_cols:
        sample_norm[col] = sample[col] - control[col]
        control_norm[col] = 0.0

    # Create DataFrame with both normalized rows
    norm_df = pd.DataFrame([sample_norm, control_norm])
    norm_df.index = [sample.name, control.name]

    return norm_df
