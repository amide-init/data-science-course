"""
Variance and Standard Deviation
Module 03, Lesson 02

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

def variance(data, population=False):
    """
    Compute variance.
    population=True  → divide by N   (you have ALL data)
    population=False → divide by N-1 (your data is a sample)  [default]
    """
    if not data:
        raise ValueError("Cannot compute variance of an empty list")
    if len(data) < 2:
        raise ValueError("Need at least 2 data points")
    m           = mean(data)
    sq_devs     = [(x - m) ** 2 for x in data]
    denominator = len(data) if population else len(data) - 1
    return sum(sq_devs) / denominator

def std_dev(data, population=False):
    """Compute standard deviation (square root of variance)."""
    return math.sqrt(variance(data, population=population))

def cv(data):
    """Coefficient of Variation — std dev as % of mean."""
    m = mean(data)
    if m == 0:
        raise ValueError("CV is undefined when mean is zero")
    return (std_dev(data) / m) * 100

def z_scores(data):
    """Compute z-score for every value in data."""
    m   = mean(data)
    std = std_dev(data)
    if std == 0:
        raise ValueError("Cannot compute z-scores: std dev is 0 (all values identical)")
    return [(x - m) / std for x in data]

def find_outliers_zscore(data, threshold=3.0):
    """Return list of (index, value, z_score) for values where |z| > threshold."""
    m   = mean(data)
    std = std_dev(data)
    return [(i, x, round((x - m) / std, 2))
            for i, x in enumerate(data)
            if abs((x - m) / std) > threshold]


# ── Section 1: Why Mean Isn't Enough ─────────────────────────────────────────

def section_why_mean_isnt_enough():
    print("─" * 55)
    print("SECTION 1: Why Mean Alone Isn't Enough")
    print("─" * 55)

    class_a = [73, 74, 75, 75, 76, 76, 77, 74, 75, 75]
    class_b = [50, 50, 55, 60, 100, 100, 95, 90, 50, 50]

    print(f"  Class A: {class_a}  → mean={mean(class_a):.1f}")
    print(f"  Class B: {class_b} → mean={mean(class_b):.1f}")
    print()
    print("  Same mean. Very different distributions.")
    print("  We need a measure of SPREAD.")
    print()

    # ASCII dot plot
    def dot_plot(data, label, lo=40, hi=110, width=50):
        line = ["-"] * width
        for v in data:
            pos = int((v - lo) / (hi - lo) * (width - 1))
            pos = max(0, min(width - 1, pos))
            line[pos] = "●"
        m_pos = int((mean(data) - lo) / (hi - lo) * (width - 1))
        if 0 <= m_pos < width:
            line[m_pos] = "▲"
        print(f"  {label}")
        print(f"  |{''.join(line)}|")
        print(f"  {lo}{' '*(width//2-4)}mean≈{mean(data):.0f}{' '*(width//2-4)}{hi}")
        print()

    dot_plot(class_a, "Class A (consistent)")
    dot_plot(class_b, "Class B (polarised)")
    print("  ▲ = mean   ● = score")
    print()


# ── Section 2: Deviation from the Mean ───────────────────────────────────────

def section_deviation():
    print("─" * 55)
    print("SECTION 2: Deviation from the Mean")
    print("─" * 55)

    scores = [60, 70, 75, 80, 90]
    m      = mean(scores)
    devs   = [x - m for x in scores]

    print(f"  Scores: {scores}   Mean: {m}")
    print()
    print(f"  {'Score':>7} {'Deviation':>12}")
    print("  " + "─" * 22)
    for x, d in zip(scores, devs):
        print(f"  {x:>7}   {d:>+10.1f}")
    print(f"  {'Sum':>7}   {sum(devs):>+10.1f}  ← always 0")
    print()
    print("  Deviations cancel out → can't use their average as spread.")
    print("  Solution: square them first.")
    print()


# ── Section 3: Variance ───────────────────────────────────────────────────────

def section_variance():
    print("─" * 55)
    print("SECTION 3: Variance")
    print("─" * 55)

    scores = [60, 70, 75, 80, 90]
    m      = mean(scores)

    print(f"  Scores: {scores}   Mean: {m}")
    print()
    print(f"  {'Score':>7} {'Dev':>9} {'Dev²':>10}")
    print("  " + "─" * 32)
    for x in scores:
        d  = x - m
        d2 = d ** 2
        print(f"  {x:>7}  {d:>+8.1f}  {d2:>9.1f}")

    sq_devs = [(x - m) ** 2 for x in scores]
    print(f"  {'Sum(Dev²)':>16}: {sum(sq_devs):.1f}")
    print()
    print(f"  Population variance (÷{len(scores)})  : {variance(scores, True):.2f}  (ALL data)")
    print(f"  Sample variance     (÷{len(scores)-1})  : {variance(scores, False):.2f}  (sample — default)")

    class_a = [73, 74, 75, 75, 76, 76, 77, 74, 75, 75]
    class_b = [50, 50, 55, 60, 100, 100, 95, 90, 50, 50]
    var_a   = variance(class_a)
    var_b   = variance(class_b)
    print()
    print(f"  Class A variance: {var_a:.2f}")
    print(f"  Class B variance: {var_b:.2f}  ({var_b/var_a:.0f}× larger)")
    print()


# ── Section 4: Standard Deviation ────────────────────────────────────────────

def section_std_dev():
    print("─" * 55)
    print("SECTION 4: Standard Deviation")
    print("─" * 55)

    class_a = [73, 74, 75, 75, 76, 76, 77, 74, 75, 75]
    class_b = [50, 50, 55, 60, 100, 100, 95, 90, 50, 50]

    for label, data in [("Class A", class_a), ("Class B", class_b)]:
        m   = mean(data)
        var = variance(data)
        std = std_dev(data)
        print(f"  {label}:")
        print(f"    Mean     : {m:.1f} points")
        print(f"    Variance : {var:.2f} points²")
        print(f"    Std dev  : {std:.2f} points  ← typical spread from mean")
        print()

    # Empirical rule
    exam = [65, 70, 72, 73, 74, 75, 75, 76, 76, 77,
            78, 78, 79, 80, 80, 81, 82, 83, 85, 88]
    m   = mean(exam)
    std = std_dev(exam)
    n   = len(exam)
    w1  = sum(1 for x in exam if abs(x - m) <= 1 * std)
    w2  = sum(1 for x in exam if abs(x - m) <= 2 * std)
    w3  = sum(1 for x in exam if abs(x - m) <= 3 * std)
    print(f"  68-95-99.7 Rule (mean={m:.1f}, std={std:.1f}):")
    print(f"    ±1σ  [{m-std:>5.1f},{m+std:>6.1f}]: {w1}/{n} = {w1/n*100:.0f}%  (expect ~68%)")
    print(f"    ±2σ  [{m-2*std:>5.1f},{m+2*std:>6.1f}]: {w2}/{n} = {w2/n*100:.0f}%  (expect ~95%)")
    print(f"    ±3σ  [{m-3*std:>5.1f},{m+3*std:>6.1f}]: {w3}/{n} = {w3/n*100:.0f}%  (expect ~99.7%)")
    print()


# ── Section 5: Coefficient of Variation ──────────────────────────────────────

def section_cv():
    print("─" * 55)
    print("SECTION 5: Coefficient of Variation")
    print("─" * 55)

    rohit = [0, 12, 5, 150, 8, 120, 2, 65, 140, 3, 50, 90]
    virat = [38, 45, 40, 52, 41, 48, 55, 37, 44, 50, 43, 47]
    dhoni = [30, 55, 28, 70, 40, 62, 20, 75, 33, 58, 45, 50]

    print(f"  Cricket Consistency Analysis")
    print(f"  {'Batsman':<10} {'Mean':>8} {'Std':>10} {'CV':>8}  {'Style'}")
    print("  " + "─" * 58)
    for name, scores in [("Rohit", rohit), ("Virat", virat), ("Dhoni", dhoni)]:
        m   = mean(scores)
        std = std_dev(scores)
        c   = cv(scores)
        style = "Explosive/inconsistent" if c > 60 else "Moderate" if c > 35 else "Very consistent"
        print(f"  {name:<10} {m:>8.1f} {std:>10.1f} {c:>7.1f}%  {style}")

    print()
    fund_a = [2.1, 2.3, 1.9, 2.4, 2.0, 2.2, 1.8, 2.5, 2.1, 2.3, 2.0, 2.2]
    fund_b = [-3.0, 5.5, -1.5, 8.2, -2.0, 6.0, 1.0, -4.5, 7.0, 3.5, -2.5, 5.3]

    print(f"  Investment Fund Comparison (monthly returns %)")
    print(f"  {'Fund':<10} {'Avg':>8} {'Std':>8} {'CV':>8}  {'Risk'}")
    print("  " + "─" * 52)
    for name, returns in [("Fund A", fund_a), ("Fund B", fund_b)]:
        m   = mean(returns)
        std = std_dev(returns)
        c   = abs(cv(returns))
        risk = "Low (stable)" if std < 1 else "High (volatile)"
        print(f"  {name:<10} {m:>8.2f} {std:>8.2f} {c:>7.1f}%  {risk}")
    print()


# ── Section 6: Z-Scores ───────────────────────────────────────────────────────

def section_zscores():
    print("─" * 55)
    print("SECTION 6: Z-Scores (Standardisation)")
    print("─" * 55)

    class_scores = [55, 58, 60, 62, 63, 65, 65, 66, 68, 70,
                    72, 74, 75, 78, 80, 82, 88, 90, 52, 69]
    m   = mean(class_scores)
    std = std_dev(class_scores)

    priya_score = 88
    priya_z     = (priya_score - m) / std
    print(f"  Class mean={m:.1f}, std={std:.1f}")
    print(f"  Priya score={priya_score}, z={priya_z:+.2f} (top ~3% of class)")

    zs = z_scores(class_scores)
    print()
    print(f"  {'Score':>7} {'Z-score':>9}  Category")
    print("  " + "─" * 36)
    for score, z in sorted(zip(class_scores, zs), reverse=True)[:8]:
        cat = "★ Exceptional" if z > 2 else "↑ Above avg" if z > 1 else "Average range"
        print(f"  {score:>7}   {z:>+7.2f}  {cat}")
    print("  ... (top 8 shown)")

    zs = z_scores(class_scores)
    print()
    print(f"  After z-scoring: mean≈{mean(zs):.8f}, std≈{std_dev(zs):.8f}")
    print("  → mean=0, std=1. This is what StandardScaler does in scikit-learn.")
    print()


# ── Section 7: Outlier Detection ─────────────────────────────────────────────

def section_outliers():
    print("─" * 55)
    print("SECTION 7: Outlier Detection with Z-Scores")
    print("─" * 55)

    temperatures = [
        22.1, 22.3, 22.0, 22.4, 22.2, 21.9, 22.1, 22.3,
        22.0, 22.2, 85.7,
        22.1, 22.2, 22.3, 22.0, 22.1, -15.3,
        22.2, 22.1, 22.0,
    ]

    outliers = find_outliers_zscore(temperatures, threshold=3.0)
    print(f"  Temperature readings — {len(temperatures)} values")
    print(f"  Mean: {mean(temperatures):.2f}°C   Std: {std_dev(temperatures):.2f}°C")
    print(f"\n  Outliers (|z| > 3):")
    for idx, val, z in outliers:
        direction = "HIGH spike" if z > 0 else "LOW dropout"
        print(f"    Index {idx:>2}: {val:>7.1f}°C  z={z:>+6.2f}  ({direction})")

    clean_idx   = {i for i, _, _ in outliers}
    clean_temps = [v for i, v in enumerate(temperatures) if i not in clean_idx]
    print(f"\n  After removing {len(outliers)} outliers:")
    print(f"    Mean: {mean(clean_temps):.2f}°C   Std: {std_dev(clean_temps):.4f}°C")
    print()


# ── Section 8: Stdlib Verification ───────────────────────────────────────────

def section_builtin():
    print("─" * 55)
    print("SECTION 8: Verification vs statistics Module")
    print("─" * 55)

    data = [72, 85, 68, 91, 76, 88, 55, 79, 83, 67]
    checks = [
        ("variance (sample)",  variance(data, False),    statistics.variance(data)),
        ("variance (pop)",     variance(data, True),     statistics.pvariance(data)),
        ("std dev (sample)",   std_dev(data, False),     statistics.stdev(data)),
        ("std dev (pop)",      std_dev(data, True),      statistics.pstdev(data)),
    ]
    print(f"  {'Measure':<22} {'Ours':>10} {'stdlib':>10} {'Match?'}")
    print("  " + "─" * 48)
    for label, ours, lib in checks:
        match = abs(ours - lib) < 1e-9
        print(f"  {label:<22} {ours:>10.4f} {lib:>10.4f} {'✓' if match else '✗'}")
    print()


# ── Section 9: Common Mistakes ────────────────────────────────────────────────

def section_mistakes():
    print("─" * 55)
    print("SECTION 9: Common Mistakes")
    print("─" * 55)

    data = [10, 20, 30, 40, 50]
    pop_v = variance(data, True)
    sam_v = variance(data, False)
    print(f"  Mistake 1 — Population vs Sample:")
    print(f"    Population var (÷{len(data)})  : {pop_v:.2f}")
    print(f"    Sample var     (÷{len(data)-1}) : {sam_v:.2f}")
    print(f"    Difference                : {sam_v - pop_v:.2f}")
    print(f"    → Use sample (n-1) by default in data science.")

    scores = [60, 70, 75, 80, 90]
    print(f"\n  Mistake 2 — Squared Units:")
    print(f"    Variance = {variance(scores):.1f} points²  ← hard to interpret")
    print(f"    Std dev  = {std_dev(scores):.1f} points   ← report this to stakeholders")

    skewed = [1, 2, 2, 3, 3, 3, 4, 4, 10, 15]
    zs     = z_scores(skewed)
    print(f"\n  Mistake 3 — Z-scores don't fix skew:")
    print(f"    Original: mean={mean(skewed):.2f}")
    print(f"    Z-scored: mean≈{mean(zs):.8f}  (shape unchanged, only scale)")

    constant = [5, 5, 5, 5, 5]
    print(f"\n  Mistake 4 — Std dev of zero ({constant}):")
    print(f"    std = {std_dev(constant)} → feature has no info → drop it before ML")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 03 LESSON 02 — Variance & Std Dev")
    print("=" * 55)
    print()

    section_why_mean_isnt_enough()
    section_deviation()
    section_variance()
    section_std_dev()
    section_cv()
    section_zscores()
    section_outliers()
    section_builtin()
    section_mistakes()

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
