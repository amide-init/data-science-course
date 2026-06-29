"""
Variables and Data Types
Module 02, Lesson 01

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""

import keyword


# ── Section 1: Creating Variables ────────────────────────────────────────────

def section_variables():
    print("─" * 50)
    print("SECTION 1: Creating Variables")
    print("─" * 50)

    student_name  = "Priya"
    student_age   = 20
    student_score = 88.5
    is_enrolled   = True

    print(f"  student_name  = {student_name!r}")
    print(f"  student_age   = {student_age!r}")
    print(f"  student_score = {student_score!r}")
    print(f"  is_enrolled   = {is_enrolled!r}")

    # Updating a variable
    score = 75
    print(f"\n  score starts at: {score}")
    score = score + 5
    print(f"  score after +5: {score}")

    # Multiple assignment
    x, y, z = 10, 20, 30
    print(f"\n  x, y, z = {x}, {y}, {z}")
    print()


# ── Section 2: The Five Core Types ───────────────────────────────────────────

def section_int():
    print("─" * 50)
    print("SECTION 2a: int")
    print("─" * 50)
    num_students  = 42
    population    = 1_428_628_000

    print(f"  num_students = {num_students}  type: {type(num_students).__name__}")
    print(f"  population   = {population:,}  type: {type(population).__name__}")
    print(f"  10 + 3  = {10 + 3}")
    print(f"  10 // 3 = {10 // 3}  (floor division)")
    print(f"  10 % 3  = {10 % 3}   (modulo / remainder)")
    print(f"  10 ** 3 = {10 ** 3}  (exponentiation)")
    print()


def section_float():
    print("─" * 50)
    print("SECTION 2b: float")
    print("─" * 50)
    height_cm  = 162.5
    scientific = 1.5e6

    print(f"  height_cm  = {height_cm}   type: {type(height_cm).__name__}")
    print(f"  scientific = {scientific}  type: {type(scientific).__name__}")
    print(f"  10 / 3     = {10 / 3}  (always float)")

    # The floating-point trap
    print(f"\n  0.1 + 0.2       = {0.1 + 0.2}")
    print(f"  == 0.3?         = {0.1 + 0.2 == 0.3}  ← floating-point issue!")
    print(f"  round to 2dp    = {round(0.1 + 0.2, 2)}  ← use round() for display")
    print()


def section_str():
    print("─" * 50)
    print("SECTION 2c: str")
    print("─" * 50)
    name = "Priya Sharma"

    print(f"  name        = {name!r}")
    print(f"  type        = {type(name).__name__}")
    print(f"  len(name)   = {len(name)}")
    print(f"  upper()     = {name.upper()}")
    print(f"  title()     = {'priya sharma'.title()}")
    print(f"  strip()     = {'  Mumbai  '.strip()!r}")
    print(f"  split(' ')  = {name.split(' ')}")
    print(f"  name[0]     = {name[0]!r}")
    print(f"  name[-1]    = {name[-1]!r}")
    print(f"  name[:5]    = {name[:5]!r}")
    print(f"  f-string    = {f'Hello, {name}!'!r}")
    print()


def section_bool():
    print("─" * 50)
    print("SECTION 2d: bool")
    print("─" * 50)
    score      = 75
    attendance = 80

    print(f"  score > 60   : {score > 60}")
    print(f"  score == 100 : {score == 100}")
    print(f"  score != 100 : {score != 100}")

    passed     = score >= 40
    good_att   = attendance >= 75
    eligible   = passed and good_att
    print(f"\n  passed and good_att → eligible: {eligible}")

    # Bool as int
    scores     = [85, 42, 91, 38, 77]
    pass_count = sum(s >= 40 for s in scores)
    print(f"\n  Scores: {scores}")
    print(f"  Students who passed: {pass_count} / {len(scores)}")
    print()


def section_none():
    print("─" * 50)
    print("SECTION 2e: NoneType")
    print("─" * 50)
    email = None
    print(f"  email           = {email}")
    print(f"  type(email)     = {type(email).__name__}")
    print(f"  email is None   = {email is None}")
    print(f"  email is not None = {email is not None}")

    # None vs 0 vs empty string
    print(f"\n  None == 0   : {None == 0}   ← different things")
    print(f"  None == ''  : {None == ''}  ← different things")

    # Working with None values in a list
    student_scores = [88, None, 72, None, 91]
    valid          = [s for s in student_scores if s is not None]
    missing        = len(student_scores) - len(valid)
    avg            = sum(valid) / len(valid)
    print(f"\n  Raw scores : {student_scores}")
    print(f"  Missing    : {missing}")
    print(f"  Average    : {avg:.1f}  (excluding missing)")
    print()


# ── Section 3: type() and isinstance() ───────────────────────────────────────

def section_type_checking():
    print("─" * 50)
    print("SECTION 3: Checking Types")
    print("─" * 50)
    values = [42, 3.14, "hello", True, None, "42", "3.14"]
    print(f"  {'Value':<12}  {'type().__name__'}")
    print("  " + "─" * 28)
    for v in values:
        print(f"  {str(v):<12}  {type(v).__name__}")

    score = 88
    print(f"\n  isinstance(88, int)           = {isinstance(score, int)}")
    print(f"  isinstance(88, float)         = {isinstance(score, float)}")
    print(f"  isinstance(88, (int, float))  = {isinstance(score, (int, float))}")
    print()


# ── Section 4: Type Conversion ────────────────────────────────────────────────

def section_type_conversion():
    print("─" * 50)
    print("SECTION 4: Type Conversion")
    print("─" * 50)

    # str → int / float
    age_str   = "20"
    price_str = "1299.99"
    age       = int(age_str)
    price     = float(price_str)
    print(f"  int('20')     = {age}      type: {type(age).__name__}")
    print(f"  float('1299.99') = {price}  type: {type(price).__name__}")

    # int → float and back
    a = 3.9
    print(f"\n  int(3.9)    = {int(a)}   ← truncated, not rounded")
    print(f"  round(3.9)  = {round(a)}   ← rounded")

    # bool() truthiness
    test_values = [1, 0, -5, 3.14, 0.0, "hello", "", None]
    print(f"\n  {'Value':<10}  {'bool()':}")
    print("  " + "─" * 22)
    for v in test_values:
        print(f"  {str(v):<10}  {bool(v)}")

    # Conversion failures
    print("\n  Conversion failure examples:")
    bad_inputs = [("int('hello')", lambda: int("hello")),
                  ("int('42.5')", lambda: int("42.5")),
                  ("float('abc')", lambda: float("abc"))]
    for expr, fn in bad_inputs:
        try:
            print(f"    {expr} → {fn()}")
        except (ValueError, TypeError) as e:
            print(f"    {expr} → Error: {e}")
    print()


# ── Section 5: Naming Conventions ────────────────────────────────────────────

def section_naming():
    print("─" * 50)
    print("SECTION 5: Naming Conventions")
    print("─" * 50)
    print("  Python reserved keywords:")
    kws = keyword.kwlist
    for i in range(0, len(kws), 6):
        print("    " + "  ".join(f"{k:<12}" for k in kws[i:i+6]))

    print()
    print("  Conventions:")
    print("    variables  → snake_case         (student_name, total_amount)")
    print("    constants  → ALL_CAPS            (MAX_SCORE, PASSING_GRADE)")
    print("    classes    → PascalCase          (StudentRecord — covered later)")
    print()


# ── Section 6: Student Info Card ─────────────────────────────────────────────

def section_info_card():
    print("─" * 50)
    print("SECTION 6: Student Info Card (all types combined)")
    print("─" * 50)

    raw_name     = "  priya sharma  "
    raw_age      = "20"
    raw_score    = "88.5"
    raw_enrolled = "True"
    raw_email    = None
    PASSING_SCORE = 40

    name         = raw_name.strip().title()
    age          = int(raw_age)
    score        = float(raw_score)
    is_enrolled  = raw_enrolled == "True"
    email        = raw_email
    has_passed   = score >= PASSING_SCORE
    grade        = "A" if score >= 80 else "B" if score >= 60 else "C" if score >= 40 else "F"
    email_display = email if email is not None else "Not provided"

    print(f"  {'=' * 38}")
    print(f"         STUDENT INFORMATION CARD")
    print(f"  {'=' * 38}")
    print(f"  Name     : {name}")
    print(f"  Age      : {age} years")
    print(f"  Score    : {score:.1f} / 100")
    print(f"  Grade    : {grade}")
    print(f"  Passed   : {'Yes ✓' if has_passed else 'No ✗'}")
    print(f"  Enrolled : {'Yes' if is_enrolled else 'No'}")
    print(f"  Email    : {email_display}")
    print(f"  {'=' * 38}")

    print("\n  Types used:")
    fields = [("name", name), ("age", age), ("score", score),
              ("has_passed", has_passed), ("email", email)]
    for field, val in fields:
        print(f"    {field:<12} → {type(val).__name__:<10}  {val!r}")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 50)
    print("  MODULE 02 LESSON 01 — Variables and Data Types")
    print("=" * 50)
    print()

    section_variables()
    section_int()
    section_float()
    section_str()
    section_bool()
    section_none()
    section_type_checking()
    section_type_conversion()
    section_naming()
    section_info_card()

    print("=" * 50)
    print("  All sections complete.")
    print("=" * 50)
