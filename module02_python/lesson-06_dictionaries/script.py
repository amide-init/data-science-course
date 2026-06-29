"""
Dictionaries
Module 02, Lesson 06

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""


# ── Section 1: Creating Dictionaries ─────────────────────────────────────────

def section_creation():
    print("─" * 55)
    print("SECTION 1: Creating Dictionaries")
    print("─" * 55)

    # Literal
    student = {
        "name"  : "Priya",
        "age"   : 20,
        "score" : 88.5,
        "city"  : "Mumbai",
        "dept"  : "CS",
    }
    print(f"  Literal : {student}")
    print(f"  Type    : {type(student).__name__}")
    print(f"  Length  : {len(student)}")

    # dict() constructor
    city = dict(name="Mumbai", population=20_667_000, state="Maharashtra")
    print(f"\n  dict()  : {city}")

    # From zip
    keys   = ["name", "age", "score", "city"]
    values = ["Priya",  20,    88.5,   "Mumbai"]
    from_zip = dict(zip(keys, values))
    print(f"\n  zip()   : {from_zip}")

    # Comprehension
    squares = {n: n**2 for n in range(1, 6)}
    print(f"\n  Comprehension: {squares}")
    print()


# ── Section 2: Accessing Values ───────────────────────────────────────────────

def section_access():
    print("─" * 55)
    print("SECTION 2: Accessing Values")
    print("─" * 55)

    student = {"name": "Priya", "age": 20, "score": 88.5, "city": "Mumbai"}

    # d[key] — raises KeyError if missing
    print(f"  student['name']  : {student['name']}")
    print(f"  student['score'] : {student['score']}")

    try:
        _ = student["email"]
    except KeyError as e:
        print(f"  KeyError on missing key: {e}")

    # .get() — safe
    print(f"\n  .get('name')         : {student.get('name')}")
    print(f"  .get('email')        : {student.get('email')!r}")
    print(f"  .get('email', 'N/A') : {student.get('email', 'N/A')}")

    # Membership
    print(f"\n  'name' in student   : {'name' in student}")
    print(f"  'email' in student  : {'email' in student}")
    print(f"  'Priya' in student  : {'Priya' in student}  ← checks keys, not values")
    print(f"  'Priya' in .values(): {'Priya' in student.values()}")
    print()


# ── Section 3: Modifying Dictionaries ────────────────────────────────────────

def section_modify():
    print("─" * 55)
    print("SECTION 3: Modifying Dictionaries")
    print("─" * 55)

    student = {"name": "Priya", "age": 20, "score": 88.5}

    student["city"] = "Mumbai"           # add
    print(f"  After add    : {student}")
    student["score"] = 91.0              # update
    print(f"  After update : {student}")
    del student["age"]                   # delete
    print(f"  After del    : {student}")
    score = student.pop("score")         # pop
    print(f"  Popped score : {score}")
    print(f"  After pop    : {student}")

    # Merging
    base    = {"name": "Priya", "age": 20}
    overlay = {"score": 88.5, "city": "Mumbai"}
    merged  = {**base, **overlay}
    print(f"\n  Unpack merge : {merged}")

    # Enrich with derived column
    s = {"name": "Priya", "score": 88.5}
    enriched = {**s, "grade": "A" if s["score"] >= 80 else "B"}
    print(f"  Enriched     : {enriched}")
    print()


# ── Section 4: Iterating ──────────────────────────────────────────────────────

def section_iteration():
    print("─" * 55)
    print("SECTION 4: Iterating")
    print("─" * 55)

    student = {"name": "Priya", "age": 20, "score": 88.5, "city": "Mumbai"}

    print("  .items():")
    for key, value in student.items():
        print(f"    {key:<8}: {value}")

    # Aggregate by group
    students = [
        {"name": "Priya",  "score": 88, "dept": "CS"},
        {"name": "Rohan",  "score": 72, "dept": "ME"},
        {"name": "Meera",  "score": 95, "dept": "CS"},
        {"name": "Karan",  "score": 61, "dept": "IT"},
        {"name": "Ananya", "score": 38, "dept": "ME"},
        {"name": "Dev",    "score": 77, "dept": "CS"},
    ]

    dept_scores = {}
    for s in students:
        dept = s["dept"]
        if dept not in dept_scores:
            dept_scores[dept] = []
        dept_scores[dept].append(s["score"])

    print(f"\n  {'Dept':<6}  {'Scores':<25}  {'Avg':>6}")
    print("  " + "─" * 42)
    for dept, scores in sorted(dept_scores.items()):
        avg = sum(scores) / len(scores)
        print(f"  {dept:<6}  {str(scores):<25}  {avg:>6.1f}")
    print()


# ── Section 5: Nested Dictionaries ───────────────────────────────────────────

def section_nested():
    print("─" * 55)
    print("SECTION 5: Nested Dictionaries")
    print("─" * 55)

    student = {
        "id"       : 1001,
        "name"     : "Priya Sharma",
        "contact"  : {"email": "priya@example.com", "phone": "9876543210", "city": "Mumbai"},
        "academics": {"dept": "CS", "year": 2,
                      "scores": {"maths": 88, "science": 92, "english": 79}},
    }

    print(f"  name             : {student['name']}")
    print(f"  city             : {student['contact']['city']}")
    print(f"  maths score      : {student['academics']['scores']['maths']}")

    scores = student["academics"]["scores"]
    avg    = sum(scores.values()) / len(scores)
    print(f"  average score    : {avg:.1f}")

    # Safe chained .get()
    incomplete = {"id": 1002, "name": "Rohan"}
    email = incomplete.get("contact", {}).get("email", "Not provided")
    print(f"\n  Safe access on incomplete record: {email}")

    # DB-like lookup
    database = {
        1001: {"name": "Priya",  "score": 88, "dept": "CS"},
        1002: {"name": "Rohan",  "score": 72, "dept": "ME"},
        1003: {"name": "Meera",  "score": 95, "dept": "CS"},
    }
    for sid in [1002, 1099]:
        rec = database.get(sid)
        if rec:
            print(f"  ID {sid}: {rec['name']} — {rec['score']}")
        else:
            print(f"  ID {sid}: not found")
    print()


# ── Section 6: Dict Comprehensions ───────────────────────────────────────────

def section_comprehensions():
    print("─" * 55)
    print("SECTION 6: Dict Comprehensions")
    print("─" * 55)

    students_list = [
        {"id": 1001, "name": "Priya",  "score": 88},
        {"id": 1002, "name": "Rohan",  "score": 72},
        {"id": 1003, "name": "Meera",  "score": 95},
    ]

    # Build lookup
    id_to_name = {s["id"]: s["name"] for s in students_list}
    print(f"  ID lookup: {id_to_name}")
    print(f"  Who is 1002? {id_to_name.get(1002)}")

    # Filter
    scores  = {"Priya": 88, "Rohan": 42, "Meera": 95, "Karan": 61, "Ananya": 38}
    passing = {n: s for n, s in scores.items() if s >= 40}
    print(f"\n  Passing (>= 40): {passing}")

    # Clean keys + convert values
    raw = {"  PRIYA  ": "88", "ROHAN": "72", "meera ": "95"}
    clean = {k.strip().title(): int(v) for k, v in raw.items()}
    print(f"\n  Raw    : {raw}")
    print(f"  Cleaned: {clean}")

    # Invert
    grade_map    = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
    gpa_to_grade = {gpa: letter for letter, gpa in grade_map.items()}
    print(f"\n  Original inverted: {gpa_to_grade}")
    print()


# ── Section 7: Classic Patterns ───────────────────────────────────────────────

def section_patterns():
    print("─" * 55)
    print("SECTION 7: Classic Dictionary Patterns")
    print("─" * 55)

    # Frequency counter
    def count_frequencies(items):
        freq = {}
        for item in items:
            freq[item] = freq.get(item, 0) + 1
        return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

    grades = ["A", "B", "A", "C", "B", "A", "F", "B", "C", "A",
              "B", "C", "A", "B", "D", "C", "A", "B", "A", "C"]
    freq  = count_frequencies(grades)
    total = sum(freq.values())
    print("  Grade distribution:")
    for grade, count in freq.items():
        bar = "█" * int(count / total * 30)
        print(f"    {grade}: {count:>3}  {count/total*100:>5.1f}%  {bar}")

    # GroupBy
    def group_by(records, key):
        groups = {}
        for record in records:
            gv = record.get(key)
            if gv not in groups:
                groups[gv] = []
            groups[gv].append(record)
        return groups

    employees = [
        {"name": "Priya",  "dept": "Engineering", "salary": 85000},
        {"name": "Rohan",  "dept": "Marketing",   "salary": 62000},
        {"name": "Meera",  "dept": "Engineering", "salary": 92000},
        {"name": "Karan",  "dept": "HR",          "salary": 55000},
        {"name": "Ananya", "dept": "Marketing",   "salary": 70000},
    ]
    by_dept = group_by(employees, "dept")
    print(f"\n  GroupBy dept:")
    print(f"  {'Dept':<15}  {'Count':>6}  {'Avg Salary':>12}")
    print("  " + "─" * 38)
    for dept, members in sorted(by_dept.items()):
        salaries = [m["salary"] for m in members]
        avg      = sum(salaries) / len(salaries)
        print(f"  {dept:<15}  {len(members):>6}  ₹{avg:>10,.0f}")

    # Label encoder
    def build_label_encoder(categories):
        unique = sorted(set(categories))
        return {cat: idx for idx, cat in enumerate(unique)}

    cities  = ["Mumbai", "Delhi", "Mumbai", "Pune", "Delhi", "Chennai"]
    encoder = build_label_encoder(cities)
    encoded = [encoder.get(c, -1) for c in cities]
    print(f"\n  Label encoder: {encoder}")
    print(f"  Encoded: {encoded}")

    # Aggregation
    def aggregate(records, group_key, value_key):
        groups = {}
        for r in records:
            grp, val = r.get(group_key), r.get(value_key)
            if val is None: continue
            if grp not in groups: groups[grp] = []
            groups[grp].append(val)
        return {g: {"count": len(v), "mean": round(sum(v)/len(v), 1),
                    "min": min(v), "max": max(v)}
                for g, v in groups.items()}

    results = [
        {"dept": "CS", "score": 88}, {"dept": "ME", "score": 72},
        {"dept": "CS", "score": 95}, {"dept": "IT", "score": 61},
        {"dept": "ME", "score": 38}, {"dept": "CS", "score": 77},
    ]
    agg = aggregate(results, "dept", "score")
    print(f"\n  Aggregation by dept:")
    print(f"  {'Dept':<6}  {'Count':>6}  {'Mean':>6}  {'Min':>5}  {'Max':>5}")
    print("  " + "─" * 36)
    for dept, stats in sorted(agg.items()):
        print(f"  {dept:<6}  {stats['count']:>6}  {stats['mean']:>6}  "
              f"{stats['min']:>5}  {stats['max']:>5}")
    print()


# ── Section 8: Common Mistakes ────────────────────────────────────────────────

def section_mistakes():
    print("─" * 55)
    print("SECTION 8: Common Mistakes")
    print("─" * 55)

    # Mistake 1: KeyError
    record = {"name": "Priya", "score": 88}
    try:
        _ = record["email"]
    except KeyError:
        print("  Mistake 1: KeyError — use .get() for optional fields")
    print(f"    .get('email', 'N/A') → {record.get('email', 'N/A')}")

    # Mistake 2: modify while iterating
    scores = {"Priya": 88, "Rohan": 42, "Meera": 95, "Ananya": 38}
    try:
        for name in scores:
            if scores[name] < 40:
                del scores[name]
    except RuntimeError as e:
        print(f"\n  Mistake 2: RuntimeError — {e}")

    scores = {"Priya": 88, "Rohan": 42, "Meera": 95, "Ananya": 38}
    to_remove = [n for n, s in scores.items() if s < 40]
    for name in to_remove:
        del scores[name]
    print(f"    Fixed — remove after collecting keys: {scores}")

    # Mistake 3: duplicate keys
    d = {"name": "Priya", "score": 88, "name": "Rohan"}
    print(f"\n  Mistake 3: duplicate key → last wins: {d}")

    # Mistake 4: mutable key
    try:
        bad = {[1, 2]: "value"}
    except TypeError as e:
        print(f"\n  Mistake 4: {e}")
    good = {(1, 2): "tuple key works"}
    print(f"    Tuple key: {good}")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 02 LESSON 06 — Dictionaries")
    print("=" * 55)
    print()

    section_creation()
    section_access()
    section_modify()
    section_iteration()
    section_nested()
    section_comprehensions()
    section_patterns()
    section_mistakes()

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
