import pandas as pd
import numpy as np
import os

# -----------------------------
# 1. Load dataset
# -----------------------------
data_path = r"C:\Users\kisho\Downloads\archive\7282_1.csv"
if not os.path.exists(data_path):
    raise FileNotFoundError(f"File not found: {data_path}")

# Auto-detect based on extension
if data_path.lower().endswith(".csv"):
    df = pd.read_csv(data_path, encoding="utf-8")
else:
    df = pd.read_excel(data_path)

print(f"Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.\n")

# -----------------------------
# 2. Basic info
# -----------------------------
print("Basic info:")
print(df.info())
print("\nMissing values per column:")
print(df.isna().sum())
print("-" * 60)

# -----------------------------
# 3. Correlation matrix (numeric features)
# -----------------------------
numeric_df = df.select_dtypes(include=[np.number])
corr_matrix = numeric_df.corr(numeric_only=True)

print("\nCorrelation Matrix (numeric features):")
print(corr_matrix)

# Identify highly correlated pairs
threshold = 0.8
high_corr_pairs = []
for col1 in corr_matrix.columns:
    for col2 in corr_matrix.columns:
        if col1 != col2:
            corr_value = corr_matrix.loc[col1, col2]
            if abs(corr_value) >= threshold:
                high_corr_pairs.append((col1, col2, corr_value))

if high_corr_pairs:
    print("\nHighly correlated pairs (|corr| >= 0.8):")
    for pair in high_corr_pairs:
        print(f"{pair[0]} ↔ {pair[1]} = {pair[2]:.2f}")
else:
    print("\nNo highly correlated numeric pairs above the threshold.")

# -----------------------------
# 4. Grouped summaries
# -----------------------------
target = "overall_rating"
interesting_patterns = []

if target in df.columns:
    categorical_cols = df.select_dtypes(include=["object", "category"]).columns
    print("\nGrouped summaries (mean/median of target by category):\n")
    for col in categorical_cols:
        if df[col].nunique() < 50:  # limit to smaller categorical sets
            grouped = (
                df.groupby(col)[target]
                .agg(["mean", "median", "count"])
                .sort_values("mean", ascending=False)
            )
            print(f"\n--- {col} ---")
            print(grouped.head(10))

            # Capture a pattern summary
            top_val = grouped.index[0]
            top_mean = grouped.iloc[0]["mean"]
            interesting_patterns.append(
                f"Hotels with '{col} = {top_val}' have the highest mean overall_rating ({top_mean:.2f})."
            )
else:
    print(f"\nTarget column '{target}' not found in dataset.")

# -----------------------------
# 5. Flag potential leakage variables
# -----------------------------
leakage_flags = []
keywords = ["rating", "score", "rank", "review", "star", "outcome", "target"]

for col in df.columns:
    if any(k in col.lower() for k in keywords) and col != target:
        leakage_flags.append(col)

if leakage_flags:
    print("\nPotential leakage variables (possibly derived from target):")
    for col in leakage_flags:
        print(f"- {col}")
        interesting_patterns.append(
            f"Column '{col}' may leak information about the target variable '{target}'."
        )
else:
    print("\nNo clear leakage variables detected by keyword heuristic.")

# -----------------------------
# 6. Summarize most interesting patterns
# -----------------------------
print("\nSummary of Interesting Patterns Found:")
if interesting_patterns:
    for i, summary in enumerate(interesting_patterns, 1):
        print(f"{i}. {summary}")
else:
    print("No major patterns identified — review data may be too sparse or noisy.")

print("\nAnalysis complete!")
