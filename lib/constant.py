# Description: This file contains the constants used in the project.

RESPONSE_TYPE_KEY = {
    0: 'Control',
    1: 'Optimal response',
    2: 'CRS',
    3: 'NT (Neurotoxicity)',
    4: 'Inverse of remission',
}

META_DATA_COLUMNS = ['experiment', 'type', 'control', 'has control', 'patient',
                     'poor response inverse of remission', 'CRS', 'NT', 'optimal response', 'response type']

# COLUMNS WHICH ARE THE EXPERIMENTAL CONDITIONS
TRAIT_COLUMNS = [
    "patient", "cd4v8", "experiment", "cell count", "protein conc", "% CAR",
    "thaw", "stim", "cd19", "cd3", "type", "control", "has control",
    "poor response inverse of remission", "CRS", "NT", "optimal response",
    "response type", "reorder"
]

PROTEIN_NAMES = ['PKCt', '2A', 'LCK', 'GRAP2', 'TAK1', 'FYN', 'PI3K', 'TCRb', 'CD28', 'CD3z', 'TRAF2', 'ZAP70', 'LAT',
                 'FYB', 'SLP76', 'BIRC3', 'TRAF1', 'VAV1', 'NCK']

# Columns which are explicitly protein-protein interaction columns
PPI_COLUMN_NAMES = ['2A_BIRC3', 'BIRC3_BIRC3', 'CD28_BIRC3', 'FYB_BIRC3', 'LAT_BIRC3', 'LCK_BIRC3', 'NCK_BIRC3',
                    'PI3K_BIRC3', 'PKCt_BIRC3', 'SLP76_BIRC3', 'TAK1_BIRC3', 'TCRb_BIRC3', 'TRAF1_BIRC3', 'TRAF2_BIRC3',
                    'VAV1_BIRC3', 'ZAP70_BIRC3', '2A_CD28', 'BIRC3_CD28', 'CD28_CD28', 'FYB_CD28', 'LAT_CD28',
                    'LCK_CD28', 'NCK_CD28', 'PI3K_CD28', 'PKCt_CD28', 'SLP76_CD28', 'TAK1_CD28', 'TCRb_CD28',
                    'TRAF1_CD28', 'TRAF2_CD28', 'ZAP70_CD28', '2A_CD3z', 'BIRC3_CD3z', 'CD28_CD3z', 'FYB_CD3z',
                    'LAT_CD3z', 'LCK_CD3z', 'NCK_CD3z', 'PI3K_CD3z', 'PKCt_CD3z', 'SLP76_CD3z', 'TAK1_CD3z',
                    'TCRb_CD3z', 'TRAF1_CD3z', 'TRAF2_CD3z', 'VAV1_CD3z', 'ZAP70_CD3z', '2A_FYN', 'BIRC3_FYN',
                    'CD28_FYN', 'FYB_FYN', 'LAT_FYN', 'LCK_FYN', 'NCK_FYN', 'PI3K_FYN', 'PKCt_FYN', 'SLP76_FYN',
                    'TAK1_FYN', 'TCRb_FYN', 'TRAF1_FYN', 'TRAF2_FYN', 'VAV1_FYN', 'ZAP70_FYN', '2A_GRAP2',
                    'BIRC3_GRAP2', 'CD28_GRAP2', 'FYB_GRAP2', 'LAT_GRAP2', 'LCK_GRAP2', 'NCK_GRAP2', 'PI3K_GRAP2',
                    'PKCt_GRAP2', 'SLP76_GRAP2', 'TAK1_GRAP2', 'TCRb_GRAP2', 'TRAF1_GRAP2', 'TRAF2_GRAP2', 'VAV1_GRAP2',
                    'ZAP70_GRAP2', '2A_LAT', 'BIRC3_LAT', 'CD28_LAT', 'FYB_LAT', 'LAT_LAT', 'LCK_LAT', 'NCK_LAT',
                    'PI3K_LAT', 'PKCt_LAT', 'SLP76_LAT', 'TAK1_LAT', 'TCRb_LAT', 'TRAF1_LAT', 'TRAF2_LAT', 'VAV1_LAT',
                    'ZAP70_LAT', '2A_LCK', 'BIRC3_LCK', 'CD28_LCK', 'FYB_LCK', 'LAT_LCK', 'LCK_LCK', 'NCK_LCK',
                    'PI3K_LCK', 'PKCt_LCK', 'SLP76_LCK', 'TAK1_LCK', 'TCRb_LCK', 'TRAF1_LCK', 'TRAF2_LCK', 'VAV1_LCK',
                    'ZAP70_LCK', '2A_PKCt', 'BIRC3_PKCt', 'CD28_PKCt', 'FYB_PKCt', 'LAT_PKCt', 'LCK_PKCt', 'NCK_PKCt',
                    'PI3K_PKCt', 'PKCt_PKCt', 'SLP76_PKCt', 'TAK1_PKCt', 'TCRb_PKCt', 'TRAF1_PKCt', 'TRAF2_PKCt',
                    'VAV1_PKCt', 'ZAP70_PKCt', '2A_SLP76', 'BIRC3_SLP76', 'CD28_SLP76', 'FYB_SLP76', 'LAT_SLP76',
                    'LCK_SLP76', 'NCK_SLP76', 'PI3K_SLP76', 'PKCt_SLP76', 'SLP76_SLP76', 'TAK1_SLP76', 'TCRb_SLP76',
                    'TRAF1_SLP76', 'TRAF2_SLP76', 'VAV1_SLP76', 'ZAP70_SLP76', '2A_TAK1', 'BIRC3_TAK1', 'CD28_TAK1',
                    'FYB_TAK1', 'LAT_TAK1', 'LCK_TAK1', 'NCK_TAK1', 'PI3K_TAK1', 'PKCt_TAK1', 'SLP76_TAK1', 'TAK1_TAK1',
                    'TCRb_TAK1', 'TRAF1_TAK1', 'TRAF2_TAK1', 'VAV1_TAK1', 'ZAP70_TAK1', '2A_TCRb', 'BIRC3_TCRb',
                    'CD28_TCRb', 'FYB_TCRb', 'LAT_TCRb', 'LCK_TCRb', 'NCK_TCRb', 'PI3K_TCRb', 'PKCt_TCRb', 'SLP76_TCRb',
                    'TAK1_TCRb', 'TCRb_TCRb', 'TRAF1_TCRb', 'TRAF2_TCRb', 'VAV1_TCRb', 'ZAP70_TCRb', '2A_TRAF1',
                    'BIRC3_TRAF1', 'CD28_TRAF1', 'FYB_TRAF1', 'LAT_TRAF1', 'LCK_TRAF1', 'NCK_TRAF1', 'PI3K_TRAF1',
                    'PKCt_TRAF1', 'SLP76_TRAF1', 'TAK1_TRAF1', 'TCRb_TRAF1', 'TRAF1_TRAF1', 'TRAF2_TRAF1', 'VAV1_TRAF1',
                    'ZAP70_TRAF1', '2A_TRAF2', 'BIRC3_TRAF2', 'CD28_TRAF2', 'FYB_TRAF2', 'LAT_TRAF2', 'LCK_TRAF2',
                    'NCK_TRAF2', 'PI3K_TRAF2', 'PKCt_TRAF2', 'SLP76_TRAF2', 'TAK1_TRAF2', 'TCRb_TRAF2', 'TRAF1_TRAF2',
                    'TRAF2_TRAF2', 'VAV1_TRAF2', 'ZAP70_TRAF2', '2A_ZAP70', 'BIRC3_ZAP70', 'CD28_ZAP70', 'FYB_ZAP70',
                    'LAT_ZAP70', 'LCK_ZAP70', 'NCK_ZAP70', 'PI3K_ZAP70', 'PKCt_ZAP70', 'SLP76_ZAP70', 'TAK1_ZAP70',
                    'TCRb_ZAP70', 'TRAF1_ZAP70', 'TRAF2_ZAP70', 'VAV1_ZAP70', 'ZAP70_ZAP70']

# Columns which are explicitly protein-protein interaction columns and also experimental conditions
# (might be useful for clustering)
EXPERIMENTAL_DATA_COL = ['2A_BIRC3', 'BIRC3_BIRC3', 'CD28_BIRC3', 'FYB_BIRC3', 'LAT_BIRC3', 'LCK_BIRC3', 'NCK_BIRC3',
                         'PI3K_BIRC3', 'PKCt_BIRC3', 'SLP76_BIRC3', 'TAK1_BIRC3', 'TCRb_BIRC3', 'TRAF1_BIRC3',
                         'TRAF2_BIRC3',
                         'VAV1_BIRC3', 'ZAP70_BIRC3', '2A_CD28', 'BIRC3_CD28', 'CD28_CD28', 'FYB_CD28', 'LAT_CD28',
                         'LCK_CD28', 'NCK_CD28', 'PI3K_CD28', 'PKCt_CD28', 'SLP76_CD28', 'TAK1_CD28', 'TCRb_CD28',
                         'TRAF1_CD28', 'TRAF2_CD28', 'ZAP70_CD28', '2A_CD3z', 'BIRC3_CD3z', 'CD28_CD3z', 'FYB_CD3z',
                         'LAT_CD3z', 'LCK_CD3z', 'NCK_CD3z', 'PI3K_CD3z', 'PKCt_CD3z', 'SLP76_CD3z', 'TAK1_CD3z',
                         'TCRb_CD3z', 'TRAF1_CD3z', 'TRAF2_CD3z', 'VAV1_CD3z', 'ZAP70_CD3z', '2A_FYN', 'BIRC3_FYN',
                         'CD28_FYN', 'FYB_FYN', 'LAT_FYN', 'LCK_FYN', 'NCK_FYN', 'PI3K_FYN', 'PKCt_FYN', 'SLP76_FYN',
                         'TAK1_FYN', 'TCRb_FYN', 'TRAF1_FYN', 'TRAF2_FYN', 'VAV1_FYN', 'ZAP70_FYN', '2A_GRAP2',
                         'BIRC3_GRAP2', 'CD28_GRAP2', 'FYB_GRAP2', 'LAT_GRAP2', 'LCK_GRAP2', 'NCK_GRAP2', 'PI3K_GRAP2',
                         'PKCt_GRAP2', 'SLP76_GRAP2', 'TAK1_GRAP2', 'TCRb_GRAP2', 'TRAF1_GRAP2', 'TRAF2_GRAP2',
                         'VAV1_GRAP2',
                         'ZAP70_GRAP2', '2A_LAT', 'BIRC3_LAT', 'CD28_LAT', 'FYB_LAT', 'LAT_LAT', 'LCK_LAT', 'NCK_LAT',
                         'PI3K_LAT', 'PKCt_LAT', 'SLP76_LAT', 'TAK1_LAT', 'TCRb_LAT', 'TRAF1_LAT', 'TRAF2_LAT',
                         'VAV1_LAT',
                         'ZAP70_LAT', '2A_LCK', 'BIRC3_LCK', 'CD28_LCK', 'FYB_LCK', 'LAT_LCK', 'LCK_LCK', 'NCK_LCK',
                         'PI3K_LCK', 'PKCt_LCK', 'SLP76_LCK', 'TAK1_LCK', 'TCRb_LCK', 'TRAF1_LCK', 'TRAF2_LCK',
                         'VAV1_LCK',
                         'ZAP70_LCK', '2A_PKCt', 'BIRC3_PKCt', 'CD28_PKCt', 'FYB_PKCt', 'LAT_PKCt', 'LCK_PKCt',
                         'NCK_PKCt',
                         'PI3K_PKCt', 'PKCt_PKCt', 'SLP76_PKCt', 'TAK1_PKCt', 'TCRb_PKCt', 'TRAF1_PKCt', 'TRAF2_PKCt',
                         'VAV1_PKCt', 'ZAP70_PKCt', '2A_SLP76', 'BIRC3_SLP76', 'CD28_SLP76', 'FYB_SLP76', 'LAT_SLP76',
                         'LCK_SLP76', 'NCK_SLP76', 'PI3K_SLP76', 'PKCt_SLP76', 'SLP76_SLP76', 'TAK1_SLP76',
                         'TCRb_SLP76',
                         'TRAF1_SLP76', 'TRAF2_SLP76', 'VAV1_SLP76', 'ZAP70_SLP76', '2A_TAK1', 'BIRC3_TAK1',
                         'CD28_TAK1',
                         'FYB_TAK1', 'LAT_TAK1', 'LCK_TAK1', 'NCK_TAK1', 'PI3K_TAK1', 'PKCt_TAK1', 'SLP76_TAK1',
                         'TAK1_TAK1',
                         'TCRb_TAK1', 'TRAF1_TAK1', 'TRAF2_TAK1', 'VAV1_TAK1', 'ZAP70_TAK1', '2A_TCRb', 'BIRC3_TCRb',
                         'CD28_TCRb', 'FYB_TCRb', 'LAT_TCRb', 'LCK_TCRb', 'NCK_TCRb', 'PI3K_TCRb', 'PKCt_TCRb',
                         'SLP76_TCRb',
                         'TAK1_TCRb', 'TCRb_TCRb', 'TRAF1_TCRb', 'TRAF2_TCRb', 'VAV1_TCRb', 'ZAP70_TCRb', '2A_TRAF1',
                         'BIRC3_TRAF1', 'CD28_TRAF1', 'FYB_TRAF1', 'LAT_TRAF1', 'LCK_TRAF1', 'NCK_TRAF1', 'PI3K_TRAF1',
                         'PKCt_TRAF1', 'SLP76_TRAF1', 'TAK1_TRAF1', 'TCRb_TRAF1', 'TRAF1_TRAF1', 'TRAF2_TRAF1',
                         'VAV1_TRAF1',
                         'ZAP70_TRAF1', '2A_TRAF2', 'BIRC3_TRAF2', 'CD28_TRAF2', 'FYB_TRAF2', 'LAT_TRAF2', 'LCK_TRAF2',
                         'NCK_TRAF2', 'PI3K_TRAF2', 'PKCt_TRAF2', 'SLP76_TRAF2', 'TAK1_TRAF2', 'TCRb_TRAF2',
                         'TRAF1_TRAF2',
                         'TRAF2_TRAF2', 'VAV1_TRAF2', 'ZAP70_TRAF2', '2A_ZAP70', 'BIRC3_ZAP70', 'CD28_ZAP70',
                         'FYB_ZAP70',
                         'LAT_ZAP70', 'LCK_ZAP70', 'NCK_ZAP70', 'PI3K_ZAP70', 'PKCt_ZAP70', 'SLP76_ZAP70', 'TAK1_ZAP70',
                         'TCRb_ZAP70', 'TRAF1_ZAP70', 'TRAF2_ZAP70', 'VAV1_ZAP70', 'ZAP70_ZAP70', 'cd4v8', 'cell count',
                         'protein conc', '% CAR', 'thaw', 'stim', 'cd19', 'cd3']
