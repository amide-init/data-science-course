"""
Loops
Module 02, Lesson 03

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""


# ── Section 1: for Loop Basics ────────────────────────────────────────────────

def section_for_basics():
    print("─" * 55)
    print("SECTION 1: for Loop Basics")
    print("─" * 55)

    # Iterate over a list
    scores = [85, 42, 91, 38, 77, 60]
    total  = 0
    for score in scores:
        total += score
    print(f"  Scores  : {scores}")
    print(f"  Total   : {total}")
    print(f"  Average : {total / len(scores):.1f}")

    # Iterate over a string
    sentence = "Data Science is the future"
    vowels   = 0
    for char in sentence.lower():
        if char in "aeiou":
            vowels += 1
    print(f"\n  Vowels in '{sentence}': {vowels}")

    # Iterate over a dictionary
    student = {"name": "Priya", "age": 20, "score": 88.5}
    print("\n  Student record:")
    for key, value in student.items():
        print(f"    {key:<8}: {value}")
    print()


# ── Section 2: range() ───────────────────────────────────────────────────────

def section_range():
    print("─" * 55)
    print("SECTION 2: range()")
    print("─" * 55)

    print(f"  range(5)        : {list(range(5))}")
    print(f"  range(1, 6)     : {list(range(1, 6))}")
    print(f"  range(0, 20, 5) : {list(range(0, 20, 5))}")
    print(f"  range(10, 0, -1): {list(range(10, 0, -1))}")
    print(f"  range(0, 10, 2) : {list(range(0, 10, 2))}")

    # Multiplication table
    n = 5
    print(f"\n  {n}× table:")
    for i in range(1, 11):
        print(f"    {n} × {i:>2} = {n * i:>3}")
    print()


# ── Section 3: enumerate() ───────────────────────────────────────────────────

def section_enumerate():
    print("─" * 55)
    print("SECTION 3: enumerate()")
    print("─" * 55)

    students = ["Priya", "Rohan", "Meera", "Karan", "Ananya"]

    print("  Rank list:")
    for rank, name in enumerate(students, start=1):
        print(f"    {rank}. {name}")

    # Find rows with missing values
    dataset = [
        {"name": "Priya",  "score": 88},
        {"name": "Rohan",  "score": None},
        {"name": "Meera",  "score": 72},
        {"name": None,     "score": 65},
        {"name": "Karan",  "score": 91},
    ]
    print("\n  Rows with missing values:")
    for row_num, row in enumerate(dataset, start=1):
        missing = [k for k, v in row.items() if v is None]
        if missing:
            print(f"    Row {row_num}: missing {missing}")
    print()


# ── Section 4: zip() ─────────────────────────────────────────────────────────

def section_zip():
    print("─" * 55)
    print("SECTION 4: zip()")
    print("─" * 55)

    names  = ["Priya", "Rohan", "Meera", "Karan"]
    scores = [88,      72,      95,      61     ]
    cities = ["Mumbai", "Delhi", "Pune", "Chennai"]

    print("  Names + Scores + Cities:")
    for name, score, city in zip(names, scores, cities):
        grade = "Pass" if score >= 40 else "Fail"
        print(f"    {name:<8} ({city}): {score}  {grade}")

    # Assemble records from split columns
    student_ids = [1001, 1002, 1003, 1004]
    records = [{"id": sid, "name": n, "score": s}
               for sid, n, s in zip(student_ids, names, scores)]
    print("\n  Assembled records:")
    for r in records:
        print(f"    {r}")
    print()


# ── Section 5: Nested Loops ───────────────────────────────────────────────────

def section_nested():
    print("─" * 55)
    print("SECTION 5: Nested Loops")
    print("─" * 55)

    # Multiplication table grid
    size = 5
    print(f"  {size}×{size} multiplication table:")
    print("     ", end="")
    for j in range(1, size + 1):
        print(f"{j:>4}", end="")
    print()
    print("     " + "─" * (size * 4))
    for i in range(1, size + 1):
        print(f"  {i} |", end="")
        for j in range(1, size + 1):
            print(f"{i * j:>4}", end="")
        print()

    # Cross-tabulation
    data = [
        {"city": "Mumbai", "grade": "A"},
        {"city": "Delhi",  "grade": "B"},
        {"city": "Mumbai", "grade": "A"},
        {"city": "Pune",   "grade": "C"},
        {"city": "Delhi",  "grade": "A"},
        {"city": "Mumbai", "grade": "B"},
    ]
    cities = ["Mumbai", "Delhi", "Pune"]
    grades = ["A", "B", "C"]
    print(f"\n  Cross-tabulation (city × grade):")
    print(f"  {'City':<10}", end="")
    for g in grades:
        print(f"  Grade {g}", end="")
    print()
    print("  " + "─" * 30)
    for city in cities:
        print(f"  {city:<10}", end="")
        for grade in grades:
            count = sum(1 for r in data if r["city"] == city and r["grade"] == grade)
            print(f"  {count:>7}", end="")
        print()
    print()


# ── Section 6: while Loop ────────────────────────────────────────────────────

def section_while():
    print("─" * 55)
    print("SECTION 6: while Loop")
    print("─" * 55)

    # Countdown
    count = 5
    print("  Countdown:", end=" ")
    while count > 0:
        print(count, end=" ")
        count -= 1
    print("→ Launch!")

    # Sentinel value
    records = [
        {"id": 1, "value": 100},
        {"id": 2, "value": 250},
        {"id": 3, "value": -99},
        {"id": 4, "value": 180},
    ]
    i     = 0
    total = 0
    while i < len(records) and records[i]["value"] != -99:
        total += records[i]["value"]
        i += 1
    print(f"\n  Sentinel read: processed {i} records, total = {total}")

    # Binary search
    def binary_search(lst, target):
        low, high, steps = 0, len(lst) - 1, 0
        while low <= high:
            mid    = (low + high) // 2
            steps += 1
            if lst[mid] == target:   return mid, steps
            elif lst[mid] < target:  low  = mid + 1
            else:                    high = mid - 1
        return -1, steps

    data = sorted([42, 55, 61, 72, 78, 83, 88, 91, 95, 99])
    print(f"\n  Binary search on {data}:")
    for t in [83, 72, 50]:
        idx, steps = binary_search(data, t)
        if idx != -1:
            print(f"    Found {t} at index {idx} in {steps} step(s)")
        else:
            print(f"    {t} not found ({steps} step(s))")
    print()


# ── Section 7: break and continue ────────────────────────────────────────────

def section_break_continue():
    print("─" * 55)
    print("SECTION 7: break and continue")
    print("─" * 55)

    # break: stop at first match
    students = [
        {"name": "Priya",  "score": 88},
        {"name": "Rohan",  "score": 72},
        {"name": "Meera",  "score": 95},
        {"name": "Karan",  "score": 61},
    ]
    top = None
    for s in students:
        if s["score"] > 90:
            top = s
            break
    print(f"  First student scoring > 90: {top['name']} ({top['score']})")

    # continue: skip invalid values
    raw_scores   = [88, None, -5, 72, None, 95, 110, 61]
    valid_scores = []
    skipped      = 0
    for score in raw_scores:
        if score is None or not (0 <= score <= 100):
            skipped += 1
            continue
        valid_scores.append(score)

    print(f"\n  Raw    : {raw_scores}")
    print(f"  Valid  : {valid_scores}")
    print(f"  Skipped: {skipped}")

    # break + continue together
    transactions = [250, 1800, 500, -1, 3000, 750]
    total = flagged = 0
    for txn in transactions:
        if txn < 0:
            print(f"\n  Sentinel hit — stopping at txn = {txn}")
            break
        if txn > 1000:
            print(f"  ⚠ Flagged: ₹{txn:,}")
            flagged += 1
            continue
        total += txn
    print(f"  Normal total: ₹{total:,}  Flagged: {flagged}")
    print()


# ── Section 8: List Comprehensions ───────────────────────────────────────────

def section_comprehensions():
    print("─" * 55)
    print("SECTION 8: List Comprehensions")
    print("─" * 55)

    scores = [88, 42, 72, 95, 61, 38, 80]

    bonus   = [s + 5 for s in scores]
    passing = [s for s in scores if s >= 40]
    failing = [s for s in scores if s < 40]

    print(f"  Original : {scores}")
    print(f"  +5 bonus : {bonus}")
    print(f"  Passing  : {passing}")
    print(f"  Failing  : {failing}")

    # String cleaning
    names   = ["  priya  ", "ROHAN", "meera ", "  KARAN", "Ananya"]
    cleaned = [n.strip().title() for n in names if len(n.strip()) > 4]
    print(f"\n  Raw names    : {names}")
    print(f"  Cleaned (>4) : {cleaned}")

    # Dataset operations
    dataset = [
        {"name": "Priya", "score": 88, "city": "Mumbai"},
        {"name": "Rohan", "score": 42, "city": "Delhi"},
        {"name": "Meera", "score": 95, "city": "Mumbai"},
        {"name": "Karan", "score": 61, "city": "Pune"},
    ]
    mumbai_names = [r["name"] for r in dataset if r["city"] == "Mumbai"]
    print(f"\n  Mumbai students: {mumbai_names}")
    print()


# ── Section 9: Computing Statistics ──────────────────────────────────────────

def section_statistics():
    print("─" * 55)
    print("SECTION 9: Computing Statistics with Loops")
    print("─" * 55)

    def summarise(values, label="values"):
        valid = [v for v in values if v is not None]
        if not valid:
            print(f"  {label}: no valid data")
            return

        n       = len(valid)
        missing = len(values) - n
        total   = sum(valid)
        mean    = total / n
        minimum = min(valid)
        maximum = max(valid)

        sorted_v = sorted(valid)
        mid      = n // 2
        median   = sorted_v[mid] if n % 2 == 1 else (sorted_v[mid - 1] + sorted_v[mid]) / 2
        variance = sum((v - mean) ** 2 for v in valid) / n
        std_dev  = variance ** 0.5

        print(f"  {label}:")
        print(f"    n={n} (missing={missing})  mean={mean:.1f}  median={median:.1f}")
        print(f"    std={std_dev:.1f}  min={minimum}  max={maximum}")

    summarise([85, None, 72, 91, 38, 60, None, 77, 55, 88], "Exam Scores")
    summarise([45000, 62000, 38000, 75000, 55000, 90000, 48000], "Salaries (₹)")
    print()


# ── Section 10: Frequency Counter ────────────────────────────────────────────

def section_frequency():
    print("─" * 55)
    print("SECTION 10: Frequency Counter")
    print("─" * 55)

    def frequency_table(data, label=""):
        counts = {}
        for item in data:
            counts[item] = counts.get(item, 0) + 1
        total  = sum(counts.values())
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        print(f"  {label} (n={total}):")
        print(f"    {'Category':<18}  {'Count':>5}  {'%':>6}  Bar")
        for cat, cnt in sorted_counts:
            pct = cnt / total * 100
            bar = "█" * int(pct / 5)
            print(f"    {str(cat):<18}  {cnt:>5}  {pct:>5.1f}%  {bar}")

    grades = ["A", "B", "A", "C", "B", "A", "F", "B", "C", "A",
              "B", "C", "A", "B", "D", "C", "A", "B", "A", "C"]
    frequency_table(grades, "Grade Distribution")
    print()

    expenses = ["Food", "Transport", "Food", "Shopping", "Food", "Entertainment",
                "Transport", "Food", "Health", "Food", "Shopping", "Transport",
                "Food", "Food", "Shopping"]
    frequency_table(expenses, "Expense Categories")
    print()


# ── Section 11: Outlier Detection ────────────────────────────────────────────

def section_outliers():
    print("─" * 55)
    print("SECTION 11: Outlier Detection (IQR Method)")
    print("─" * 55)

    def find_outliers_iqr(values, label="values"):
        valid = sorted([v for v in values if v is not None])
        n     = len(valid)
        q1    = valid[n // 4]
        q3    = valid[(3 * n) // 4]
        iqr   = q3 - q1
        lo    = q1 - 1.5 * iqr
        hi    = q3 + 1.5 * iqr
        outliers = [v for v in valid if v < lo or v > hi]
        normal   = [v for v in valid if lo <= v <= hi]
        print(f"  {label}:")
        print(f"    Q1={q1}  Q3={q3}  IQR={iqr}  fences=[{lo}, {hi}]")
        print(f"    Outliers ({len(outliers)}): {outliers}")
        print(f"    Normal   ({len(normal)}): {normal}")

    salaries = [35000, 40000, 42000, 45000, 47000, 50000,
                52000, 55000, 60000, 65000, 70000, 150000, 5000]
    find_outliers_iqr(salaries, "Monthly Salary (₹)")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 02 LESSON 03 — Loops")
    print("=" * 55)
    print()

    section_for_basics()
    section_range()
    section_enumerate()
    section_zip()
    section_nested()
    section_while()
    section_break_continue()
    section_comprehensions()
    section_statistics()
    section_frequency()
    section_outliers()

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
