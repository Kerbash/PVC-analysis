# CAR-T Analysis Pipeline

A prototype computational pipeline that tries to surface candidate protein–protein interaction (PPI) signatures from a noisy CAR-T cell therapy dataset. It was developed to attack one particularly stubborn data-quality pattern; two other independently-built approaches were developed alongside it as cross-checks on the same dataset.

This is exploratory, hypothesis-generating code. The intended output is a short list of PPI candidates worth following up on biologically — not effect sizes, not a tuned classifier, and not a general-purpose tool.

## Background

### What's being measured

For each sample (a patient × T-cell subset × condition) the assay reports the pairwise interaction signal between 19 proteins in the TCR / CAR signaling pathway: PKCt, LCK, ZAP70, CD3z, CD28, TCRb, GRAP2, TAK1, FYN, PI3K, TRAF2, LAT, FYB, SLP76, BIRC3, TRAF1, VAV1, NCK, and 2A. Every column named `ProteinA_ProteinB` (e.g. `LCK_CD3z`, `ZAP70_TCRb`) is one such PPI intensity.

Samples are labeled with the patient's clinical response — control, optimal response, CRS (cytokine release syndrome), neurotoxicity, or inverse-of-remission. The question is which PPIs differ between responders and non-responders.

### Why the data is hard

Two problems make direct comparison unreliable:

1. **Protein concentration varies across samples.** Two samples with identical underlying biology but different total protein loaded will report different absolute interaction intensities. Comparing raw PPI values across samples therefore mixes biological signal with loading variance.
2. **Sample size is small relative to the feature count.** ~190 PPI features against a much smaller number of samples — classical p ≫ n territory, where any single ranking is unstable.

The pipeline's job is to extract whatever stable signal exists despite both problems. It does not claim to solve them.

## Approach

### Step 1 — Pairing on protein concentration

Rather than normalize each sample independently, the pipeline pairs each experimental sample with a control whose `protein conc` is close (within ±threshold of their midpoint), then operates on the pair. The reasoning: if the experimental and its paired control were measured at comparable concentration, their *difference* is closer to a biological contrast than either absolute value is. The pairing is the main mitigation for the loading-variance problem.

Once paired, the pair is centered using one of three strategies in [Step1Normalization/pair_normalizer.py](Step1Normalization/pair_normalizer.py):

- **midpoint** — subtract `(sample + control) / 2` from both rows
- **log2-fold** — `log2(sample / control)` with explicit safety handling for zeros
- **zero-control** — set control to zero, subtract control value from sample

### Step 2 — Ranking PPIs by response association

After normalization, a Random Forest is trained to predict response class, and feature importances are aggregated across cross-validation folds via Borda / average rank. The same ranking is run on the CD4 and CD8 T-cell subsets separately and on the full dataset, then re-checked by re-training on the top-N features.

### Why three normalization variants

The three centering strategies are not an unresolved design choice — they are deliberate. Each handles loading variance under a different noise assumption, and the deliverable is the PPIs that **rank consistently across all three**. A feature that's top-ranked under only one normalization is treated as method-specific noise; a feature that survives all three is more likely to reflect a real association.

This within-project consensus is a first filter. Findings worth taking seriously are those that also surface in the parallel approaches developed alongside this pipeline.

## Scope

**Is**: a prototype for one specific data-quality pattern — small N, varying protein loading, paired sample/control structure. The output is a shortlist of candidate PPIs for biological validation.

**Isn't**: a general method, a tuned classifier, or a source of effect-size estimates. The Random Forest uses fixed defaults (`n_estimators=100`, `max_depth=3`); feature importances are RF impurity scores, which carry known biases that aren't corrected for here. None of that is hidden — the design assumes a second, independent filter downstream.

## Repository layout

```
lib/
  constant.py        protein names, PPI column list, response-type key, metadata columns
  normalizer.py      whole-matrix and PPI-only min-max
  numberline.py      1D class-colored scatter (visualization helper)
  graph_plot.py      PCA + clustering ellipses, used at multiple stages

Step1Normalization/
  preprocess.ipynb                    load + clean
  Pair Vector Centralization.ipynb    main pairing + centering flow + PCA checks
  find_protein_conc_pair.py           pair by protein conc within ±threshold of midpoint
  pair_normalizer.py                  three centering strategies
  input/   cleaned.csv, pure_or_0.25_thresh_paired_df.csv
  output/  normalized_output.csv, PCA SVGs (all / CD4 / CD8, pre- and post-norm)

Step2MLandPPIRanking/
  PPI Ranking.ipynb                   RF + LDA, ranking aggregation, top-N validation, plots
  output/                             .pkl models, ranking CSVs, dendrograms, heatmaps, bump chart
```

## How to run

The analysis is driven from the notebooks. Run in this order:

1. `Step1Normalization/preprocess.ipynb`
2. `Step1Normalization/Pair Vector Centralization.ipynb`
3. `Step2MLandPPIRanking/PPI Ranking.ipynb`

A local `.venv/` is included; install runtime dependencies into it: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`.

## Caveats worth keeping in mind

- Pairing in [find_protein_conc_pair.py](Step1Normalization/find_protein_conc_pair.py) is greedy and order-dependent; the chosen pairs can shift if the input is reordered.
- RF impurity importance is used as-is, without permutation correction.
- Top-feature performance is not validated against an independent cohort within this repository.

These choices are acceptable for a prototype whose findings are re-checked by independent methods. They would not be acceptable for a standalone deliverable. The framing is the difference.
