"""
Types of Data — Column Classifier Utility
Module 01, Lesson 06

Run this script to audit any list of columns and get a type breakdown.
Usage: python script.py
"""

import statistics
from collections import Counter


# ── Section 1: Type Classification ───────────────────────────────────────────

ORDINAL_SETS = [
    {"S", "M", "L", "XL", "XXL"},
    {"XS", "S", "M", "L", "XL"},
    {"Dissatisfied", "Neutral", "Satisfied", "Very Satisfied"},
    {"Poor", "Fair", "Good", "Excellent"},
    {"None", "Mild", "Moderate", "Severe"},
    {"Low", "Medium", "High"},
    {"School", "Undergraduate", "Postgraduate", "PhD"},
    {"F", "D", "C", "B", "A"},
]

LIKELY_ID_KEYWORDS = {"id", "code", "pin", "zip", "phone", "mobile", "number"}


def guess_stat_type(column, column_name=""):
    """
    Guesses the statistical type of a column.
    Returns (stat_type, category, confidence, note).
    Always verify with domain knowledge — this is a starting point, not a verdict.
    """
    if not column:
        return "Unknown", "Unknown", "Low", "Empty column"

    non_null = [v for v in column if v is not None]
    if not non_null:
        return "Unknown", "Unknown", "Low", "All values are None/missing"

    python_types = set(type(v).__name__ for v in non_null)
    unique_vals  = set(non_null)
    n_unique     = len(unique_vals)
    n_total      = len(non_null)

    name_lower = column_name.lower()

    # Bool → nominal binary
    if python_types == {"bool"}:
        return "Nominal (binary)", "Qualitative", "High", "True/False — two categories"

    # Float → continuous
    if python_types == {"float"}:
        return "Continuous", "Quantitative", "High", "Decimal values — arithmetic is valid"

    # String → qualitative (nominal or ordinal)
    if python_types == {"str"}:
        str_vals = set(str(v) for v in non_null)
        for ordinal_set in ORDINAL_SETS:
            if str_vals.issubset(ordinal_set) and len(str_vals) > 1:
                return "Ordinal", "Qualitative", "High", f"Matches known ordinal set: {sorted(ordinal_set)}"
        return "Nominal", "Qualitative", "Medium", "Text categories — check for hidden ordering"

    # Integer → discrete or nominal
    if python_types == {"int"}:
        if any(kw in name_lower for kw in LIKELY_ID_KEYWORDS):
            return "Nominal", "Qualitative", "High", "Name suggests ID/code — arithmetic meaningless"
        if n_unique == 2:
            return "Nominal (binary)", "Qualitative", "High", "Only 2 unique integer values — binary flag"
        if n_unique > n_total * 0.8:
            return "Nominal or Continuous", "Check context", "Low", \
                   "High cardinality int — could be ID or continuous measure; check domain"
        return "Discrete", "Quantitative", "Medium", f"{n_unique} unique values — likely a count"

    # Mixed types
    return "Mixed", "Unknown", "Low", f"Multiple Python types found: {python_types}"


# ── Section 2: Column Statistics ─────────────────────────────────────────────

def column_summary(column, column_name="", stat_type=None):
    """Prints appropriate statistics based on the column's statistical type."""
    non_null = [v for v in column if v is not None]
    n_missing = len(column) - len(non_null)

    print(f"\n  Column      : {column_name}")
    print(f"  Total rows  : {len(column)}  |  Missing: {n_missing}")
    print(f"  Stat type   : {stat_type or 'not specified'}")

    if not non_null:
        print("  → No non-null values to summarise.")
        return

    if stat_type in ("Continuous", "Discrete"):
        try:
            print(f"  Min         : {min(non_null)}")
            print(f"  Max         : {max(non_null)}")
            print(f"  Mean        : {statistics.mean(non_null):.2f}")
            print(f"  Median      : {statistics.median(non_null):.2f}")
            if len(non_null) > 1:
                print(f"  Std dev     : {statistics.stdev(non_null):.2f}")
        except TypeError:
            print("  → Cannot compute numeric stats on this column.")

    elif stat_type in ("Nominal", "Nominal (binary)", "Ordinal"):
        counts = Counter(non_null)
        most_common = counts.most_common(5)
        print(f"  Unique vals : {len(set(non_null))}")
        print(f"  Top values  :")
        for val, count in most_common:
            pct = count / len(non_null) * 100
            print(f"    {str(val):<20} {count:>4}  ({pct:.1f}%)")
    else:
        print("  → Type unknown — inspect manually.")


# ── Section 3: Full Dataset Audit ────────────────────────────────────────────

def audit_dataset(named_columns):
    """
    Audits a list of (column_name, column_data) tuples.
    Prints type classification and summary for each column.
    """
    print("=" * 65)
    print("  DATASET AUDIT — DATA TYPE CLASSIFICATION")
    print("=" * 65)
    print(f"\n  {'Column':<20} {'Stat Type':<25} {'Category':<16} {'Confidence'}")
    print("  " + "─" * 63)

    type_results = {}
    for col_name, col_data in named_columns:
        stat_type, category, confidence, note = guess_stat_type(col_data, col_name)
        type_results[col_name] = (stat_type, col_data)
        marker = "⚠ " if confidence == "Low" else "  "
        print(f"  {marker}{col_name:<18} {stat_type:<25} {category:<16} {confidence}")

    print()
    print("  ⚠ = low confidence — verify with domain knowledge")

    print("\n" + "=" * 65)
    print("  COLUMN SUMMARIES")
    print("=" * 65)
    for col_name, (stat_type, col_data) in type_results.items():
        column_summary(col_data, col_name, stat_type)


# ── Section 4: Demo Data ──────────────────────────────────────────────────────

student_dataset = [
    ("student_id",    [101, 102, 103, 104, 105, 106, 107, 108]),
    ("name",          ["Priya", "Rohan", "Meera", "Karan", "Ananya",
                       "Vihaan", "Ishaan", "Riya"]),
    ("city",          ["Mumbai", "Delhi", "Mumbai", "Bengaluru",
                       "Chennai", "Delhi", "Pune", "Mumbai"]),
    ("age",           [20, 21, 19, 22, 20, 21, 23, 19]),
    ("height_cm",     [162.5, 175.0, 158.3, 180.2, 163.0, 172.5, 168.8, 155.5]),
    ("score",         [88, 62, 45, 91, 74, 55, 38, 83]),
    ("grade",         ["A", "B", "C", "A", "B", "C", "F", "A"]),
    ("satisfaction",  ["Very Satisfied", "Neutral", "Dissatisfied",
                       "Very Satisfied", "Satisfied", "Neutral",
                       "Dissatisfied", "Satisfied"]),
    ("num_absences",  [2, 5, 9, 0, 3, 7, 12, 1]),
    ("is_hostel",     [True, False, True, False, True, True, False, True]),
]


if __name__ == "__main__":
    audit_dataset(student_dataset)

    print("\n" + "=" * 65)
    print("  QUICK REFERENCE — VALID OPERATIONS BY TYPE")
    print("=" * 65)
    reference = [
        ("Continuous",       "mean, median, std, min, max, percentile, histogram, scatter"),
        ("Discrete",         "sum, mean, median, count, mode, bar chart"),
        ("Nominal",          "count, mode, frequency table, bar chart, pie chart"),
        ("Nominal (binary)", "proportion, count, bar chart"),
        ("Ordinal",          "median, mode, frequency — mean is debatable, ordered bar chart"),
    ]
    print(f"\n  {'Type':<20} {'Valid Operations'}")
    print("  " + "─" * 62)
    for dtype, ops in reference:
        print(f"  {dtype:<20} {ops}")
    print()
