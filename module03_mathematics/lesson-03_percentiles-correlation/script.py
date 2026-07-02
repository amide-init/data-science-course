"""
Percentiles and Correlation
Module 03, Lesson 03

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""

import math
import statistics


# ── Core Functions ────────────────────────────────────────────────────────────

def mean(data):
    if not data:
        raise ValueError("Cannot compute mean of an empty list")
    return sum(data) / len(data)

def percentile(data, p):
    """
    Compute the p-th percentile of data using linear interpolation.
    p must be between 0 and 100.
    """
    if not data:
        raise ValueError("Cannot compute percentile of an empty list")
    if not 0 <= p <= 100:
        raise ValueError("Percentile must be between 0 and 100")

    sorted_data = sorted(data)
    n = len(sorted_data)
    rank = (p / 100) * (n - 1)

    lower = int(rank)
    upper = min(lower + 1, n - 1)
    fraction = rank - lower

    return sorted_data[lower] + fraction * (sorted_data[upper] - sorted_data[lower])

def quartiles(data):
    """Return (Q1, Q2, Q3) for data."""
    return percentile(data, 25), percentile(data, 50), percentile(data, 75)

def five_number_summary(data):
    """Return (min, Q1, median, Q3, max)."""
    q1, q2, q3 = quartiles(data)
    return min(data), q1, q2, q3, max(data)

def find_outliers_iqr(data, k=1.5):
    """Detect outliers using Tukey's IQR method. Returns list of (index, value)."""
    q1, _, q3 = quartiles(data)
    iqr = q3 - q1
    lower_fence = q1 - k * iqr
    upper_fence = q3 + k * iqr
    return [(i, x) for i, x in enumerate(data) if x < lower_fence or x > upper_fence]

def box_plot(data, label="", width=60):
    """Draw a simple ASCII box plot for data."""
    lo, q1, med, q3, hi = five_number_summary(data)

    def pos(v):
        p = int((v - lo) / (hi - lo) * (width - 1)) if hi > lo else 0
        return max(0, min(width - 1, p))

    line = list("-" * width)
    p_lo, p_q1, p_med, p_q3, p_hi = pos(lo), pos(q1), pos(med), pos(q3), pos(hi)
    for i in range(p_q1, p_q3 + 1):
        line[i] = "="
    line[p_med] = "|"
    line[p_lo] = "<"
    line[p_hi] = ">"

    print(f"  {label}")
    print(f"  |{''.join(line)}|")
    print(f"   min={lo:.0f}   Q1={q1:.0f}   median={med:.0f}   Q3={q3:.0f}   max={hi:.0f}")
    print()

def correlation(x, y):
    """Compute the Pearson correlation coefficient between x and y."""
    if len(x) != len(y):
        raise ValueError("x and y must be the same length")
    if len(x) < 2:
        raise ValueError("Need at least 2 data points")

    mx, my = mean(x), mean(y)
    numerator = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y))
    denom_x = math.sqrt(sum((xi - mx) ** 2 for xi in x))
    denom_y = math.sqrt(sum((yi - my) ** 2 for yi in y))

    if denom_x == 0 or denom_y == 0:
        raise ValueError("Correlation is undefined when one variable has zero variance")

    return numerator / (denom_x * denom_y)

def interpret_correlation(r):
    """Return a plain-English interpretation of a correlation coefficient."""
    if r == 0:
        return "no correlation"
    strength = "strong" if abs(r) >= 0.8 else "moderate" if abs(r) >= 0.5 else "weak" if abs(r) >= 0.2 else "negligible"
    direction = "positive" if r > 0 else "negative"
    return f"{strength} {direction} correlation"

def ascii_scatter(x, y, width=50, height=15):
    """Rough ASCII scatter plot."""
    x_lo, x_hi = min(x), max(x)
    y_lo, y_hi = min(y), max(y)
    grid = [[" "] * width for _ in range(height)]
    for xi, yi in zip(x, y):
        col = int((xi - x_lo) / (x_hi - x_lo) * (width - 1)) if x_hi > x_lo else 0
        row = int((yi - y_lo) / (y_hi - y_lo) * (height - 1)) if y_hi > y_lo else 0
        grid[height - 1 - row][col] = "*"
    for row in grid:
        print("  |" + "".join(row) + "|")
    print(f"   low={x_lo} ... x ... high={x_hi}")


# ── Section 1: Percentile vs Percentage ──────────────────────────────────────

def section_percentile_vs_percentage():
    print("─" * 55)
    print("SECTION 1: Percentile vs Percentage")
    print("─" * 55)

    exam_easy = [60, 65, 68, 70, 72, 75, 78, 80, 82, 85, 88, 90, 92, 94, 95, 96, 97, 98, 99, 100]
    exam_hard = [20, 25, 30, 32, 35, 38, 40, 42, 45, 48, 50, 52, 55, 58, 60, 62, 65, 68, 70, 72]
    priya_score = 65
    n = len(exam_easy)

    rank_easy = sum(1 for x in exam_easy if x < priya_score)
    rank_hard = sum(1 for x in exam_hard if x < priya_score)

    print(f"  Priya scored {priya_score} on both exams.")
    print(f"  Easy exam -> ~{rank_easy/n*100:.0f}th percentile")
    print(f"  Hard exam -> ~{rank_hard/n*100:.0f}th percentile")
    print("  Same raw score, very different standing.")
    print()


# ── Section 2: Percentiles From Scratch ──────────────────────────────────────

def section_percentiles():
    print("─" * 55)
    print("SECTION 2: Computing Percentiles")
    print("─" * 55)

    scores = [55, 60, 62, 65, 68, 70, 72, 75, 78, 80, 82, 85, 88, 90, 95]
    print(f"  Scores: {sorted(scores)}")
    for p in [0, 25, 50, 75, 90, 95, 100]:
        print(f"    {p:>3}th percentile : {percentile(scores, p):.1f}")
    print()


# ── Section 3: Quartiles and Five-Number Summary ─────────────────────────────

def section_quartiles():
    print("─" * 55)
    print("SECTION 3: Quartiles and Five-Number Summary")
    print("─" * 55)

    salaries = [28000, 32000, 35000, 38000, 40000, 42000, 45000,
                48000, 50000, 55000, 60000, 65000, 72000, 250000]
    lo, q1, med, q3, hi = five_number_summary(salaries)
    print(f"  min={lo:,.0f}  Q1={q1:,.0f}  median={med:,.0f}  Q3={q3:,.0f}  max={hi:,.0f}")
    print(f"  IQR={q3-q1:,.0f}")
    print()


# ── Section 4: IQR Outlier Detection ─────────────────────────────────────────

def section_iqr_outliers():
    print("─" * 55)
    print("SECTION 4: IQR Outlier Detection")
    print("─" * 55)

    salaries = [28000, 32000, 35000, 38000, 40000, 42000, 45000,
                48000, 50000, 55000, 60000, 65000, 72000, 250000]
    outliers = find_outliers_iqr(salaries)
    print(f"  Outliers found: {[(i, f'{v:,.0f}') for i, v in outliers]}")
    print()


# ── Section 5: ASCII Box Plot ─────────────────────────────────────────────────

def section_box_plot():
    print("─" * 55)
    print("SECTION 5: ASCII Box Plot")
    print("─" * 55)

    exam_a = [60, 65, 68, 70, 72, 74, 75, 78, 80, 85, 90]
    exam_b = [40, 55, 60, 65, 68, 70, 72, 75, 90, 95, 99]
    box_plot(exam_a, "Exam A")
    box_plot(exam_b, "Exam B")


# ── Section 6/7: Correlation ──────────────────────────────────────────────────

def section_correlation():
    print("─" * 55)
    print("SECTION 6-7: Correlation")
    print("─" * 55)

    study_hours = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9]
    exam_scores = [42, 50, 48, 55, 60, 63, 68, 72, 75, 80, 85, 92]
    price = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    qty_sold = [500, 470, 430, 410, 380, 340, 300, 270, 230, 200]

    r_study = correlation(study_hours, exam_scores)
    r_price = correlation(price, qty_sold)
    print(f"  Study hours vs exam score : r = {r_study:+.3f}")
    print(f"  Price vs quantity sold    : r = {r_price:+.3f}")
    print()


# ── Section 8: Interpretation and Causation Trap ─────────────────────────────

def section_causation_trap():
    print("─" * 55)
    print("SECTION 8: Correlation vs Causation")
    print("─" * 55)

    month_temp = [10, 12, 18, 24, 30, 34, 35, 33, 28, 20, 14, 11]
    ice_cream_sold = [200, 220, 350, 500, 800, 1000, 1050, 980, 700, 400, 250, 210]
    drownings = [1, 1, 2, 4, 7, 10, 11, 9, 6, 3, 1, 1]

    r_ice_drown = correlation(ice_cream_sold, drownings)
    r_temp_ice = correlation(month_temp, ice_cream_sold)
    r_temp_drown = correlation(month_temp, drownings)

    print(f"  Ice cream vs drownings : r = {r_ice_drown:+.3f}  ({interpret_correlation(r_ice_drown)})")
    print(f"  Temp vs ice cream      : r = {r_temp_ice:+.3f}  ({interpret_correlation(r_temp_ice)})")
    print(f"  Temp vs drownings      : r = {r_temp_drown:+.3f}  ({interpret_correlation(r_temp_drown)})")
    print("  Temperature is the confounding variable driving both.")
    print()


# ── Section 9: Nonlinear Relationships ───────────────────────────────────────

def section_nonlinear():
    print("─" * 55)
    print("SECTION 9: Nonlinear Relationships")
    print("─" * 55)

    x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    y = [v ** 2 for v in x]
    r = correlation(x, y)
    print(f"  y = x^2 -> Pearson r = {r:+.3f} (near zero despite a perfect relationship)")
    print()


# ── Section 10: Stdlib Verification ──────────────────────────────────────────

def section_builtin():
    print("─" * 55)
    print("SECTION 10: Verification vs statistics Module")
    print("─" * 55)

    data = [55, 60, 62, 65, 68, 70, 72, 75, 78, 80, 82, 85, 88, 90, 95]
    x = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9]
    y = [42, 50, 48, 55, 60, 63, 68, 72, 75, 80, 85, 92]

    stdlib_quartiles = statistics.quantiles(data, n=4)
    our_quartiles = quartiles(data)
    print(f"  Quartiles ours   : {[round(v, 2) for v in our_quartiles]}")
    print(f"  Quartiles stdlib : {[round(v, 2) for v in stdlib_quartiles]}")

    stdlib_r = statistics.correlation(x, y)
    our_r = correlation(x, y)
    match = abs(our_r - stdlib_r) < 1e-9
    print(f"  Correlation ours={our_r:.6f}  stdlib={stdlib_r:.6f}  match={match}")
    print()


# ── Section 11: Common Mistakes ───────────────────────────────────────────────

def section_mistakes():
    print("─" * 55)
    print("SECTION 11: Common Mistakes")
    print("─" * 55)

    class_scores = [40, 45, 50, 55, 60, 62, 65, 68, 70, 72, 75, 78, 80, 85, 90]
    my_score = 65
    my_percentile = sum(1 for x in class_scores if x < my_score) / len(class_scores) * 100
    print(f"  Mistake 1 — score={my_score} is a percentage; percentile rank is ~{my_percentile:.0f}th")

    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"  Mistake 2 — our percentile() matches NumPy/pandas defaults: p50={percentile(data, 50)}")

    firefighters = [5, 10, 15, 20, 25, 30, 35, 40]
    damage = [10000, 25000, 45000, 60000, 80000, 95000, 115000, 130000]
    r = correlation(firefighters, damage)
    print(f"  Mistake 3 — firefighters vs damage r={r:+.3f} (confounded by fire size, not causal)")

    x_clean = [1, 2, 3, 4, 5, 6, 7, 8]
    y_clean = [2, 3, 5, 4, 6, 5, 7, 8]
    x_outlier = x_clean + [50]
    y_outlier = y_clean + [1]
    r_clean = correlation(x_clean, y_clean)
    r_outlier = correlation(x_outlier, y_outlier)
    print(f"  Mistake 4 — r without outlier={r_clean:+.3f}, with outlier={r_outlier:+.3f}")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 03 LESSON 03 — Percentiles & Correlation")
    print("=" * 55)
    print()

    section_percentile_vs_percentage()
    section_percentiles()
    section_quartiles()
    section_iqr_outliers()
    section_box_plot()
    section_correlation()
    section_causation_trap()
    section_nonlinear()
    section_builtin()
    section_mistakes()

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
