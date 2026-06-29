"""
Functions
Module 02, Lesson 04

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""


# ── Section 1: Defining and Calling Functions ─────────────────────────────────

def section_basics():
    print("─" * 55)
    print("SECTION 1: Defining and Calling Functions")
    print("─" * 55)

    def get_grade(score):
        """Return letter grade for a numeric score (0–100)."""
        if score >= 80:   return "A"
        elif score >= 60: return "B"
        elif score >= 40: return "C"
        else:             return "F"

    scores = [88, 55, 72, 32, 91, 65]
    grades = [get_grade(s) for s in scores]
    print("  score → grade:")
    for s, g in zip(scores, grades):
        print(f"    {s:>3} → {g}")
    print()


# ── Section 2: Parameters and Arguments ──────────────────────────────────────

def section_parameters():
    print("─" * 55)
    print("SECTION 2: Parameters and Arguments")
    print("─" * 55)

    # Positional
    def compute_bmi(weight_kg, height_m):
        """Return BMI = weight / height²."""
        return round(weight_kg / height_m ** 2, 1)

    print(f"  BMI (positional) : {compute_bmi(70, 1.75)}")
    print(f"  BMI (keyword)    : {compute_bmi(height_m=1.75, weight_kg=70)}")
    print(f"  BMI (wrong order): {compute_bmi(1.75, 70)}  ← nonsensical")

    # Default values
    def format_currency(amount, currency="₹", decimals=2):
        """Format a number as a currency string."""
        return f"{currency}{amount:,.{decimals}f}"

    print(f"\n  format_currency(1299.5)            : {format_currency(1299.5)}")
    print(f"  format_currency(49.99, '$')        : {format_currency(49.99, '$')}")
    print(f"  format_currency(1500, '€', 0)      : {format_currency(1500, '€', 0)}")

    # *args and **kwargs
    def total_score(*subject_scores):
        """Sum scores across any number of subjects."""
        return sum(subject_scores)

    print(f"\n  total_score(85, 72)           : {total_score(85, 72)}")
    print(f"  total_score(85, 72, 91)       : {total_score(85, 72, 91)}")
    print(f"  total_score(85, 72, 91, 68)   : {total_score(85, 72, 91, 68)}")

    def create_record(**fields):
        return fields

    r = create_record(name="Priya", age=20, score=88.5)
    print(f"\n  create_record(kwargs)          : {r}")
    print()


# ── Section 3: Return Values ──────────────────────────────────────────────────

def section_return_values():
    print("─" * 55)
    print("SECTION 3: Return Values")
    print("─" * 55)

    def min_max_mean(values):
        """Return (minimum, maximum, mean)."""
        valid = [v for v in values if v is not None]
        if not valid:
            return None, None, None
        return min(valid), max(valid), sum(valid) / len(valid)

    scores = [85, None, 72, 91, 38, 60, None, 77]
    lo, hi, avg = min_max_mean(scores)
    print(f"  Scores: {scores}")
    print(f"  Min={lo}  Max={hi}  Mean={avg:.1f}")

    # validate_age returns 3 values
    def validate_age(value):
        """Return (is_valid, cleaned_value, message)."""
        if value is None or str(value).strip() == "":
            return False, None, "Missing"
        try:
            age = int(float(value))
        except (ValueError, TypeError):
            return False, None, f"Not a number: {value!r}"
        if not (0 <= age <= 120):
            return False, None, f"Out of range: {age}"
        return True, age, "OK"

    test_inputs = ["20", "25.0", None, "", "abc", "150"]
    print(f"\n  {'Input':<10}  {'Valid':<6}  {'Value':<8}  {'Message'}")
    print("  " + "─" * 40)
    for inp in test_inputs:
        ok, val, msg = validate_age(inp)
        print(f"  {str(inp):<10}  {str(ok):<6}  {str(val):<8}  {msg}")
    print()


# ── Section 4: Scope ──────────────────────────────────────────────────────────

def section_scope():
    print("─" * 55)
    print("SECTION 4: Variable Scope")
    print("─" * 55)

    def compute_total(scores):
        total = sum(scores)    # local to this function
        return total

    result = compute_total([85, 72, 91])
    print(f"  compute_total([85, 72, 91]) = {result}")

    try:
        print(total)   # NameError — total is local
    except NameError as e:
        print(f"  NameError: {e}")

    # Global constant — reading is fine
    PASSING_SCORE = 40

    def has_passed(score):
        return score >= PASSING_SCORE

    print(f"\n  has_passed(55) = {has_passed(55)}")
    print(f"  has_passed(35) = {has_passed(35)}")

    # Pure function vs impure
    def process_good(score, current_count):
        return score * 2, current_count + 1

    count = 0
    _, count = process_good(50, count)
    _, count = process_good(75, count)
    print(f"\n  Pure function count after 2 calls: {count}")
    print()


# ── Section 5: Docstrings ─────────────────────────────────────────────────────

def section_docstrings():
    print("─" * 55)
    print("SECTION 5: Docstrings and compute_stats")
    print("─" * 55)

    def compute_stats(values, label="column"):
        """
        Return descriptive statistics for a list of numbers.

        Parameters
        ----------
        values : list — numeric values (None entries ignored)
        label  : str  — column name for display

        Returns
        -------
        dict with keys: label, count, missing, mean, median, std, min, max
        """
        valid = [v for v in values if v is not None and isinstance(v, (int, float))]
        if not valid:
            return {"label": label, "count": 0, "missing": len(values)}
        n        = len(valid)
        mean     = sum(valid) / n
        sorted_v = sorted(valid)
        mid      = n // 2
        median   = sorted_v[mid] if n % 2 == 1 else (sorted_v[mid-1] + sorted_v[mid]) / 2
        variance = sum((v - mean) ** 2 for v in valid) / n
        return {
            "label"  : label,
            "count"  : n,
            "missing": len(values) - n,
            "mean"   : round(mean, 2),
            "median" : median,
            "std"    : round(variance ** 0.5, 2),
            "min"    : min(valid),
            "max"    : max(valid),
        }

    scores   = [85, None, 72, 91, 38, 60, None, 77, 55, 88]
    salaries = [45000, 62000, 38000, 75000, 55000, 90000, 48000]

    for d in [compute_stats(scores, "Exam Scores"),
              compute_stats(salaries, "Salary (₹)")]:
        print(f"  {d['label']}:")
        for k, v in d.items():
            if k != "label":
                print(f"    {k:<8}: {v}")
    print()


# ── Section 6: Lambda Functions ───────────────────────────────────────────────

def section_lambda():
    print("─" * 55)
    print("SECTION 6: Lambda Functions")
    print("─" * 55)

    students = [
        {"name": "Priya",  "score": 88, "age": 20},
        {"name": "Rohan",  "score": 72, "age": 22},
        {"name": "Meera",  "score": 95, "age": 19},
        {"name": "Karan",  "score": 61, "age": 21},
        {"name": "Ananya", "score": 88, "age": 20},
    ]

    by_score = sorted(students, key=lambda s: s["score"], reverse=True)
    print("  Sorted by score (desc):")
    for s in by_score:
        print(f"    {s['name']:<10} {s['score']}")

    by_score_name = sorted(students, key=lambda s: (-s["score"], s["name"]))
    print("\n  Sorted by score desc, name asc (tie-break):")
    for s in by_score_name:
        print(f"    {s['name']:<10} {s['score']}")

    scores  = [85, 42, 72, 95, 61, 38, 80, 55]
    passing = list(filter(lambda s: s >= 40, scores))
    scaled  = list(map(lambda s: round(s * 0.9, 1), scores))
    print(f"\n  filter (>= 40) : {passing}")
    print(f"  map (*0.9)     : {scaled}")
    print()


# ── Section 7: Data Science Toolkit ──────────────────────────────────────────

def section_toolkit():
    print("─" * 55)
    print("SECTION 7: Data Science Toolkit")
    print("─" * 55)

    # ── clean_string ──────────────────────────────────────────────────────────
    def clean_string(value, default=None, case="title"):
        if value is None:
            return default
        cleaned = str(value).strip()
        if not cleaned:
            return default
        if case == "title": return cleaned.title()
        if case == "upper": return cleaned.upper()
        if case == "lower": return cleaned.lower()
        return cleaned

    messy = ["  PRIYA SHARMA  ", "rohan verma", "", None, "  meera PILLAI"]
    print("  clean_string:")
    for raw in messy:
        print(f"    {str(raw):<22} → {str(clean_string(raw))!r}")

    # ── safe_to_number ────────────────────────────────────────────────────────
    def safe_to_number(value, target_type=float, default=None):
        if value is None or str(value).strip() == "":
            return default
        try:
            return target_type(float(value))
        except (ValueError, TypeError):
            return default

    cases = [("88", int, None), ("72.5", float, None),
             (None, float, 0.0), ("abc", float, None)]
    print("\n  safe_to_number:")
    for val, typ, default in cases:
        result = safe_to_number(val, typ, default)
        print(f"    ({str(val)!r}, {typ.__name__}, {default!r}) → {result!r}")

    # ── classify ─────────────────────────────────────────────────────────────
    def classify(value, thresholds, below_label="Unknown"):
        if value is None:
            return below_label
        for threshold, label in sorted(thresholds, key=lambda x: x[0], reverse=True):
            if value >= threshold:
                return label
        return below_label

    GRADE_THRESHOLDS = [(80, "A"), (60, "B"), (40, "C"), (0, "F")]
    print("\n  classify (grade thresholds):")
    for s in [95, 72, 45, 30, None]:
        print(f"    score {str(s):<5} → {classify(s, GRADE_THRESHOLDS, 'N/A')}")

    # ── validate_row ──────────────────────────────────────────────────────────
    def validate_row(row, schema):
        issues = []
        for field, rules in schema.items():
            value = row.get(field)
            if rules.get("required", False) and (value is None or value == ""):
                issues.append(f"{field}: required but missing")
                continue
            if value is None:
                continue
            expected_type = rules.get("type")
            if expected_type and not isinstance(value, expected_type):
                issues.append(f"{field}: expected {expected_type.__name__}, got {type(value).__name__}")
                continue
            if "min" in rules and value < rules["min"]:
                issues.append(f"{field}: {value} < min {rules['min']}")
            if "max" in rules and value > rules["max"]:
                issues.append(f"{field}: {value} > max {rules['max']}")
            if "allowed" in rules and value not in rules["allowed"]:
                issues.append(f"{field}: '{value}' not in {rules['allowed']}")
        return len(issues) == 0, issues

    SCHEMA = {
        "name" : {"type": str,  "required": True},
        "age"  : {"type": int,  "required": True, "min": 15, "max": 35},
        "score": {"type": (int, float), "min": 0, "max": 100},
        "dept" : {"allowed": ["CS", "EC", "ME", "CE", "IT"]},
    }

    rows = [
        {"name": "Priya",  "age": 20,  "score": 88.5, "dept": "CS"},
        {"name": "",       "age": 21,  "score": 72.0, "dept": "ME"},
        {"name": "Meera",  "age": 19,  "score": 115,  "dept": "CS"},
        {"name": "Karan",  "age": 99,  "score": 60.0, "dept": "CS"},
    ]

    print("\n  validate_row:")
    for row in rows:
        ok, issues = validate_row(row, SCHEMA)
        name = row.get("name") or "(empty)"
        status = "✓ OK" if ok else "✗ " + "; ".join(issues)
        print(f"    {name:<10} → {status}")

    # ── Mini pipeline ─────────────────────────────────────────────────────────
    raw_data = [
        {"name": "  PRIYA  ", "age": "20", "score": "88",  "dept": "CS"},
        {"name": "rohan",     "age": "22", "score": "72",  "dept": "ME"},
        {"name": "",          "age": "19", "score": "95",  "dept": "CS"},   # invalid
        {"name": "karan",     "age": "25", "score": "61",  "dept": "IT"},
    ]

    clean_recs, rejected = [], []
    for raw in raw_data:
        cleaned = {
            "name" : clean_string(raw.get("name")),
            "age"  : safe_to_number(raw.get("age"), int, None),
            "score": safe_to_number(raw.get("score"), float, None),
            "dept" : clean_string(raw.get("dept"), case="upper"),
        }
        ok, issues = validate_row(cleaned, SCHEMA)
        if ok:
            cleaned["grade"] = classify(cleaned["score"], GRADE_THRESHOLDS, "N/A")
            clean_recs.append(cleaned)
        else:
            rejected.append({"name": cleaned.get("name"), "issues": issues})

    print(f"\n  Pipeline: {len(clean_recs)} clean, {len(rejected)} rejected")
    for r in clean_recs:
        print(f"    ✓ {r['name']:<12}  score={r['score']}  grade={r['grade']}")
    for r in rejected:
        print(f"    ✗ {str(r['name']):<12}  {'; '.join(r['issues'])}")
    print()


# ── Section 8: Common Mistakes ────────────────────────────────────────────────

def section_mistakes():
    print("─" * 55)
    print("SECTION 8: Common Mistakes")
    print("─" * 55)

    # Mistake 1: forgetting return
    def get_grade_broken(score):
        if score >= 80: grade = "A"
        elif score >= 60: grade = "B"
        else: grade = "C"
        # no return!

    print(f"  Broken (no return): {get_grade_broken(88)!r}  ← None!")

    def get_grade_fixed(score):
        if score >= 80: return "A"
        elif score >= 60: return "B"
        else: return "C"

    print(f"  Fixed (with return): {get_grade_fixed(88)!r}")

    # Mistake 2: mutable default argument
    def add_score_bad(score, results=[]):
        results.append(score)
        return results

    def add_score_good(score, results=None):
        if results is None:
            results = []
        results.append(score)
        return results

    print(f"\n  Mutable default (bad):")
    print(f"    call 1: {add_score_bad(88)}")
    print(f"    call 2: {add_score_bad(72)}  ← should be [72], not [88, 72]!")
    print(f"  None default (good):")
    print(f"    call 1: {add_score_good(88)}")
    print(f"    call 2: {add_score_good(72)}  ← correct: [72]")

    # Mistake 3: print instead of return
    def double_print(n):
        print(f"    double_print output: {n * 2}")

    def double_return(n):
        return n * 2

    print(f"\n  double_print(5) return value: {double_print(5)!r}  ← None")
    print(f"  double_return(5) return value: {double_return(5)!r}  ← usable")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 02 LESSON 04 — Functions")
    print("=" * 55)
    print()

    section_basics()
    section_parameters()
    section_return_values()
    section_scope()
    section_docstrings()
    section_lambda()
    section_toolkit()
    section_mistakes()

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
