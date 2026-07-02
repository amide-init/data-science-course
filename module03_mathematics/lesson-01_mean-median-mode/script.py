"""
Mean, Median, Mode
Module 03, Lesson 01

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""

import random
import statistics


# ── Core Functions ────────────────────────────────────────────────────────────

def mean(data):
    """Compute the arithmetic mean of a non-empty list of numbers."""
    if not data:
        raise ValueError("Cannot compute mean of an empty list")
    return sum(data) / len(data)

def weighted_mean(values, weights):
    """Compute the weighted mean of values using given weights."""
    if len(values) != len(weights):
        raise ValueError("values and weights must have the same length")
    total_weight = sum(weights)
    if total_weight == 0:
        raise ValueError("Weights must not all be zero")
    return sum(v * w for v, w in zip(values, weights)) / total_weight

def median(data):
    """Compute the median of a non-empty list of numbers."""
    if not data:
        raise ValueError("Cannot compute median of an empty list")
    sorted_data = sorted(data)
    n   = len(sorted_data)
    mid = n // 2
    if n % 2 == 1:
        return sorted_data[mid]
    return (sorted_data[mid - 1] + sorted_data[mid]) / 2

def mode(data):
    """Return all modes (most frequent values) of data as a sorted list."""
    if not data:
        return []
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    max_count = max(freq.values())
    return sorted(k for k, v in freq.items() if v == max_count)

def frequency_distribution(data, bar_width=25):
    """Print an ASCII frequency bar chart for data."""
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    max_count = max(freq.values())
    total     = len(data)
    print(f"  {'Value':<10} {'Count':>6} {'%':>6}  Bar")
    print("  " + "─" * (bar_width + 26))
    for value, count in sorted(freq.items(), key=lambda x: -x[1]):
        bar = "█" * int(count / max_count * bar_width)
        print(f"  {str(value):<10} {count:>6} {count/total*100:>5.1f}%  {bar}")

def describe(data, label="data"):
    """Print and return a summary of descriptive statistics."""
    if not data:
        print(f"  {label}: (empty)")
        return {}
    n          = len(data)
    data_mean  = mean(data)
    data_med   = median(data)
    data_mode  = mode(data)
    data_min   = min(data)
    data_max   = max(data)
    data_range = data_max - data_min
    sorted_d   = sorted(data)
    q1  = sorted_d[n // 4]
    q3  = sorted_d[3 * n // 4]
    gap = data_mean - data_med
    skew = "right-skewed" if gap > 1 else "left-skewed" if gap < -1 else "roughly symmetric"
    print(f"  ── {label} ──")
    print(f"  count  : {n}")
    print(f"  mean   : {data_mean:.2f}")
    print(f"  median : {data_med}")
    print(f"  mode   : {data_mode}")
    print(f"  min    : {data_min}")
    print(f"  max    : {data_max}")
    print(f"  range  : {data_range}")
    print(f"  Q1     : {q1}")
    print(f"  Q3     : {q3}")
    print(f"  skew   : {skew}")
    return {"count": n, "mean": round(data_mean, 2), "median": data_med,
            "mode": data_mode, "min": data_min, "max": data_max,
            "range": data_range, "q1": q1, "q3": q3, "skew": skew}


# ── Section 1: Mean ───────────────────────────────────────────────────────────

def section_mean():
    print("─" * 55)
    print("SECTION 1: Mean")
    print("─" * 55)

    scores = [72, 85, 68, 91, 76, 88, 55, 79, 83, 67]
    print(f"  Scores: {scores}")
    print(f"  Count : {len(scores)}")
    print(f"  Sum   : {sum(scores)}")
    print(f"  Mean  : {mean(scores):.1f}")

    # Outlier effect
    salaries = [35000, 42000, 38000, 45000, 40000,
                37000, 43000, 39000, 41000, 1_200_000]
    print(f"\n  Salary mean (10 incl. founder) : ₹{mean(salaries):>10,.0f}")
    print(f"  Salary mean (9 employees only) : ₹{mean(salaries[:-1]):>10,.0f}")
    print(f"  → Founder's salary inflates mean by ₹{mean(salaries)-mean(salaries[:-1]):,.0f}")

    # Weighted mean
    components = ["Assignments", "Mid-sem", "Practicals", "End-sem"]
    scores_pct = [82, 74, 90, 68]
    weightages = [20, 20, 10, 50]
    print(f"\n  Priya's semester (weighted):")
    print(f"  {'Component':<14} {'Score':>7} {'Weight':>8} {'Contribution':>14}")
    print("  " + "─" * 47)
    for comp, sc, wt in zip(components, scores_pct, weightages):
        print(f"  {comp:<14} {sc:>7}   {wt:>5}%   {sc*wt/100:>12.1f}")
    print(f"\n  Simple mean   : {mean(scores_pct):.1f}")
    print(f"  Weighted mean : {weighted_mean(scores_pct, weightages):.1f}  ← real final score")
    print()


# ── Section 2: Median ─────────────────────────────────────────────────────────

def section_median():
    print("─" * 55)
    print("SECTION 2: Median")
    print("─" * 55)

    odd_data  = [15, 22, 8, 31, 19]
    even_data = [15, 22, 8, 31, 19, 25]
    print(f"  Odd  {odd_data}  → sorted {sorted(odd_data)}  → median={median(odd_data)}")
    print(f"  Even {even_data} → sorted {sorted(even_data)} → median={median(even_data)}")

    salaries = [35000, 42000, 38000, 45000, 40000,
                37000, 43000, 39000, 41000, 1_200_000]
    print(f"\n  {'Measure':<10} {'With outlier':>16} {'Without':>16}")
    print("  " + "─" * 46)
    print(f"  {'Mean':<10} ₹{mean(salaries):>14,.0f} ₹{mean(salaries[:-1]):>14,.0f}")
    print(f"  {'Median':<10} ₹{median(salaries):>14,.0f} ₹{median(salaries[:-1]):>14,.0f}")
    print("  → Mean swings by ₹1.3 lakh; median barely moves.")
    print()


# ── Section 3: Mode ───────────────────────────────────────────────────────────

def section_mode():
    print("─" * 55)
    print("SECTION 3: Mode")
    print("─" * 55)

    grades = ["B", "A", "C", "B", "B", "A", "C", "B", "A", "B"]
    scores = [70, 85, 70, 90, 85, 75, 60, 85, 70, 80]
    sizes  = ["M", "L", "S", "M", "XL", "M", "L", "M", "S", "L", "M", "XXL", "L", "M"]

    print(f"  Grades (unimodal) : mode={mode(grades)}")
    print(f"  Scores (bimodal)  : mode={mode(scores)}")
    print(f"  Shirt sizes       : mode={mode(sizes)}  ← stock this most")

    departments = ["CS", "ME", "CS", "EE", "CS", "IT", "ME", "CS",
                   "EE", "IT", "CS", "ME", "CS", "IT", "EE"]
    cities = ["Mumbai", "Delhi", "Pune", "Mumbai", "Bangalore", "Mumbai",
              "Delhi", "Pune", "Mumbai", "Chennai", "Mumbai", "Delhi"]
    print(f"\n  Most common dept : {mode(departments)}")
    print(f"  Most common city : {mode(cities)}")
    print()


# ── Section 4: Frequency Distribution ────────────────────────────────────────

def section_frequency():
    print("─" * 55)
    print("SECTION 4: Frequency Distribution")
    print("─" * 55)

    random.seed(42)
    raw_scores = [random.randint(40, 100) for _ in range(40)]
    grade_data = []
    for s in raw_scores:
        if s >= 80:   grade_data.append("A")
        elif s >= 60: grade_data.append("B")
        elif s >= 40: grade_data.append("C")
        else:         grade_data.append("F")

    print("  Grade distribution (40 students):")
    frequency_distribution(grade_data)
    print(f"  Mode (most common grade): {mode(grade_data)}")
    print()


# ── Section 5: Skew Detection ─────────────────────────────────────────────────

def section_skew():
    print("─" * 55)
    print("SECTION 5: Skew Detection — Mean vs Median Gap")
    print("─" * 55)

    datasets = {
        "Symmetric (exam scores)" : [55, 60, 65, 70, 72, 74, 75, 76, 78, 80, 82, 85, 90],
        "Right-skewed (salaries)" : [30000, 32000, 35000, 38000, 40000, 42000, 45000, 300000],
        "Left-skewed (easy test)" : [55, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98],
    }

    print(f"  {'Dataset':<28} {'Mean':>8} {'Median':>8} {'Gap':>8} {'Skew'}")
    print("  " + "─" * 68)
    for label, data in datasets.items():
        m   = mean(data)
        med = median(data)
        gap = m - med
        skew = "right →" if gap > 1 else "← left" if gap < -1 else "symmetric"
        print(f"  {label:<28} {m:>8.1f} {med:>8.1f} {gap:>8.1f} {skew}")
    print()


# ── Section 6: describe() + Group Stats ──────────────────────────────────────

def section_describe():
    print("─" * 55)
    print("SECTION 6: describe() + Group Analysis")
    print("─" * 55)

    maths   = [72, 85, 68, 91, 76, 88, 55, 79, 83, 67, 90, 74, 62, 88, 95]
    science = [65, 78, 82, 70, 88, 61, 74, 90, 55, 77, 83, 69, 94, 72, 80]

    for subject, marks in [("Maths", maths), ("Science", science)]:
        describe(marks, label=subject)
        print()

    # Group-level stats
    students = [
        {"name": "Priya",     "dept": "CS", "score": 88},
        {"name": "Rohan",     "dept": "ME", "score": 72},
        {"name": "Meera",     "dept": "CS", "score": 95},
        {"name": "Karan",     "dept": "IT", "score": 61},
        {"name": "Ananya",    "dept": "CS", "score": 38},
        {"name": "Dev",       "dept": "ME", "score": 77},
        {"name": "Riya",      "dept": "IT", "score": 82},
        {"name": "Arjun",     "dept": "CS", "score": 91},
        {"name": "Divya",     "dept": "EE", "score": 68},
        {"name": "Siddharth", "dept": "ME", "score": 55},
        {"name": "Pooja",     "dept": "CS", "score": 79},
        {"name": "Kavya",     "dept": "EE", "score": 92},
        {"name": "Shreya",    "dept": "CS", "score": 76},
        {"name": "Aditya",    "dept": "ME", "score": 63},
        {"name": "Tanvi",     "dept": "EE", "score": 88},
    ]
    dept_scores = {}
    for s in students:
        dept_scores.setdefault(s["dept"], []).append(s["score"])

    print(f"  Department Analysis")
    print(f"  {'Dept':<6} {'n':>3} {'Mean':>7} {'Median':>8} {'Mode':>12} {'Min':>5} {'Max':>5}")
    print("  " + "─" * 52)
    for dept, sc in sorted(dept_scores.items()):
        print(f"  {dept:<6} {len(sc):>3} {mean(sc):>7.1f} {median(sc):>8.1f} "
              f"{str(mode(sc)):>12} {min(sc):>5} {max(sc):>5}")
    print()


# ── Section 7: Built-in statistics module ────────────────────────────────────

def section_builtin():
    print("─" * 55)
    print("SECTION 7: Python's statistics Module")
    print("─" * 55)

    scores = [72, 85, 68, 91, 76, 88, 55, 79, 83, 67]
    print(f"  statistics.mean()      : {statistics.mean(scores)}")
    print(f"  statistics.median()    : {statistics.median(scores)}")
    print(f"  statistics.multimode() : {statistics.multimode(scores)}")
    print(f"\n  Our mean()   == stdlib : {mean(scores) == statistics.mean(scores)}")
    print(f"  Our median() == stdlib : {median(scores) == statistics.median(scores)}")
    print()


# ── Section 8: Common Mistakes ────────────────────────────────────────────────

def section_mistakes():
    print("─" * 55)
    print("SECTION 8: Common Mistakes")
    print("─" * 55)

    # Mistake 1: unsorted median
    data = [91, 55, 83, 67, 72]
    wrong = data[len(data) // 2]
    right = median(data)
    print(f"  Mistake 1 — unsorted median:")
    print(f"    Wrong (no sort) : {wrong}")
    print(f"    Correct         : {right}")

    # Mistake 2: in-place sort
    original = [91, 55, 83, 67, 72]
    sorted_copy = sorted(original)
    print(f"\n  Mistake 2 — in-place sort:")
    print(f"    original unchanged : {original}")
    print(f"    sorted() copy      : {sorted_copy}")

    # Mistake 3: mode returns a list
    bimodal = [1, 2, 2, 3, 3, 4]
    modes = mode(bimodal)
    print(f"\n  Mistake 3 — mode returns a list: {modes}")
    if len(modes) == 1:
        print(f"    Single mode: {modes[0]}")
    else:
        print(f"    Multiple modes: {modes}")

    # Mistake 4: mean on categorical
    grades_numeric = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
    student_grades = ["A", "B", "B", "A", "C", "B", "A", "F", "B", "A"]
    nums = [grades_numeric[g] for g in student_grades]
    print(f"\n  Mistake 4 — mean on categorical:")
    print(f"    Mean of encoded grades : {mean(nums):.2f}  (hard to interpret)")
    print(f"    Mode of grades         : {mode(student_grades)}  (immediately useful)")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 03 LESSON 01 — Mean, Median, Mode")
    print("=" * 55)
    print()

    section_mean()
    section_median()
    section_mode()
    section_frequency()
    section_skew()
    section_describe()
    section_builtin()
    section_mistakes()

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
