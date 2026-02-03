# fast-ephermeris-surroogate

# Overview
it is a system which when given a planet and timestamp input returns the aerospacial coordinates of the planet , it is faster than the slow accurate systems which use heavey mathematical calculations

# Problem statement
The slower very accurate position calculators are slow , 10 - 20ms for one calculations which seems short for a human but for a supercomputer doing millions of calculations per second it is a huge number so , this system uses machine learning to reduce the time becuse , a well trained model , uses more than 50x less time than a precise calculator.

# Approach
First we will train a model using a data set which will be fetched by the slow calculaotr  , for now we will train it for a specifc timeine and then when we enter a input the trained model will instantly return me a set of coordinates for the planet.

# Data generation
The training data will be generated will be collected by the accurate calculator from a specific tiemline  , in gaps of 6 hours example - 2/10/2014 00:00 and the next data will be from 2/20/2014 06:00 

# Evaluation metrics
This project evaluates models along two dimensions: latency and accuracy.
Both are required to justify replacing the slow system.

Latency-

Latency is measured as time per inference.
We report P50 (median) and P95 (tail latency).
P95 is emphasized because tail latency matters in real systems.
Latency is measured under repeated runs with warm-up to avoid noisy measurements.
Goal: minimize latency while remaining within acceptable error bounds.

Accuracy-

Accuracy is measured as 3D position error, computed as the distance between:
the surrogate output, and
the trusted slow system output.

We report:
P50 error (typical case),
P95 / P99 error (bad cases),
Worst-case error (catastrophic risk).
Goal: quantify how much error is introduced in exchange for speed.

# Baseline

Before introducing machine learning models, we establish simple and strong baselines to understand how difficult the problem is and to ensure that any improvement from ML is meaningful.
The slow, high-accuracy numerical system is treated as the ground truth for accuracy and as the upper bound on latency.

Accuracy: treated as exact

Latency: measured to understand why it is unsuitable for high-frequency or low-latency use

LAST VALUE-
this baseline predicts the position at a given time using the most recent available position.

You already know the position at some earlier time.

Now someone asks for the position a little later.

Instead of calculating anything new, you say:

“I’ll just reuse the last position I saw.”

It assumes the system changes smoothly over time.

This baseline establishes how far a model can go without learning any global patterns.


LINEAR INTERPOLATION - 
This baseline estimates positions by linearly interpolating between the nearest known timestamps.

It captures local smoothness in the system.

It is fast, deterministic, and difficult to beat for nearby timestamps.

This serves as a strong non-ML baseline that machine learning models must outperform on the accuracy–latency tradeoff to be justified.

# Safety & Fallback
When we input a value way greater or smaller then the trained dataset , we cannot trust the surrogate

if the input is like this the system falls back to slow accurate one

# Data generation
Training data is generated offline using a trusted but slow numerical calculator that computes object positions for a given timestamp.

A fixed time range is selected (e.g., 2014–2025).

Timestamps are sampled at a regular interval (e.g., every 6 hours).

This produces a dense but manageable set of input–output pairs.

To avoid temporal leakage:
data is split by time, not randomly.
earlier timestamps are used for training,
later timestamps are reserved for validation and testing.

# Results

Latency comparison

The slow reference system exhibits consistently higher latency due to expensive numerical computation.

Simple baselines (last-value, interpolation) are fast but rely on stored data points.

The surrogate model achieves significantly lower and more predictable latency, especially at the P95 level.


Accuracy is measured as 3D positional error relative to the slow reference system.

Observed behavior:

The last-value baseline performs reasonably for short intervals but accumulates error over time.

Linear interpolation improves typical error but can still produce large errors in certain regimes.

The surrogate model achieves lower median error while controlling tail and worst-case errors.


the slow system provides perfect accuracy but unacceptable latency,

baselines offer low latency but limited accuracy,

the surrogate model lies on the Pareto frontier-> u cannot improve one thing without breaking another , achieving a favorable balance between speed and accuracy.

# Limitataion

Key limitations include:

Limited time range:
The surrogate model is only validated within the chosen training window. Inputs far outside this range may require fallback to the slow system.

Approximation error:
The surrogate intentionally trades exact accuracy for speed. While errors are quantified and controlled, exact equivalence with the slow system is not guaranteed.

Domain specificity:
The model learns patterns specific to the selected objects and coordinate system. Extending to other domains would require regenerating data and retraining.

No physical reasoning:
The model does not encode physical laws or constraints; it purely learns a data-driven mapping from time to position.

Not a replacement for high-precision use cases:
Applications requiring exact or certified precision should rely exclusively on the slow reference system.

# Reproducibility

Reproducibility steps include:

Offline data generation:
Ground truth data can be regenerated by re-running the data generation script with the same timestamp range and sampling cadence.

Deterministic training:
Random seeds are fixed where applicable to ensure consistent model training and evaluation results.

Clear project structure:
Data, models, and artifacts are stored in well-defined directories to avoid hidden dependencies.

Single-command execution:
Key experiments can be reproduced by running the provided scripts in sequence as documented in this repository.



# STRUCTURE 

data/

Contains all datasets used in the project.
Raw ground-truth data generated from the slow system is stored separately from processed, model-ready datasets to avoid leakage and ensure reproducibility.

data/raw/
Stores ground-truth position data exactly as produced by the slow reference system, without any modification or preprocessing.

data/processed/
Contains cleaned and time-split datasets (train/validation/test) used directly for baselines and model training.

src/

Contains all source code, organized by responsibility to keep experiments modular and easy to reason about.

src/data_generation/
Code for generating timestamps and querying the slow reference system to build the raw dataset.

src/baselines/
Simple non-ML methods (e.g., last-value, interpolation) used to establish minimum performance benchmarks.

src/models/
Machine learning surrogate models that approximate the slow system with lower latency.

src/evaluation/
Evaluation logic for computing accuracy metrics, latency benchmarks, and comparative analysis.

src/utils/
Shared helper functions (time handling, math utilities, common helpers) used across modules.

artifacts/

Stores outputs generated by experiments, separated from training data to clearly distinguish results from inputs.

artifacts/plots/
Saved figures such as accuracy–latency tradeoff plots and error distributions used in reporting.

artifacts/tables/
Final result tables summarizing baseline comparisons, model performance, and safety/fallback impact.

Root files

README.md
High-level description of the problem, approach, results, and limitations of the project.

project_notes.md
Personal decision log documenting design choices, tradeoffs, and lessons learned during development.

requirements.txt
Lists all dependencies required to reproduce the environment and rerun experiments.