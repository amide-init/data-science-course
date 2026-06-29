"""
Operators and Conditions
Module 02, Lesson 02

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""


# ── Section 1: Arithmetic Operators ──────────────────────────────────────────

def section_arithmetic():
    print("─" * 55)
    print("SECTION 1: Arithmetic Operators")
    print("─" * 55)

    a, b = 17, 5
    print(f"  a = {a}, b = {b}")
    print(f"  a + b  = {a + b}   addition")
    print(f"  a - b  = {a - b}   subtraction")
    print(f"  a * b  = {a * b}   multiplication")
    print(f"  a / b  = {a / b}   division (always float)")
    print(f"  a // b = {a // b}   floor division")
    print(f"  a % b  = {a % b}   modulo (remainder)")
    print(f"  a ** b = {a ** b}  exponentiation")

    # Floor division + modulo in practice
    total_minutes = 137
    hours   = total_minutes // 60
    minutes = total_minutes % 60
    print(f"\n  {total_minutes} minutes = {hours}h {minutes}m")

    # Augmented assignment
    total = 0
    total += 450
    total += 299
    total += 1199
    print(f"\n  Augmented assignment: 450 + 299 + 1199 = {total}")

    # Precedence example
    scores = [80, 92, 71, 88]
    wrong   = scores[0] + scores[1] + scores[2] + scores[3] / 4   # bug!
    correct = (scores[0] + scores[1] + scores[2] + scores[3]) / 4
    print(f"\n  Wrong average (missing parentheses)  : {wrong}")
    print(f"  Correct average (with parentheses)   : {correct}")
    print()


# ── Section 2: Comparison Operators ──────────────────────────────────────────

def section_comparison():
    print("─" * 55)
    print("SECTION 2: Comparison Operators")
    print("─" * 55)

    score = 72
    print(f"  score = {score}")
    print(f"  == 72  → {score == 72}")
    print(f"  != 72  → {score != 72}")
    print(f"  >  60  → {score > 60}")
    print(f"  <  60  → {score < 60}")
    print(f"  >= 72  → {score >= 72}")
    print(f"  <= 70  → {score <= 70}")

    # Chained comparisons
    print(f"\n  Chained comparison  60 <= score < 80 : {60 <= score < 80}")

    age          = 25
    salary       = 55000
    credit_score = 710
    print(f"\n  Age in working range (18–60)  : {18 <= age <= 60}")
    print(f"  Salary in middle band         : {30000 <= salary <= 80000}")
    print(f"  Credit score is good (700+)   : {credit_score >= 700}")

    # String comparison (case-sensitive)
    city_input = "MUMBAI"
    print(f"\n  'MUMBAI' == 'mumbai'         : {'MUMBAI' == 'mumbai'}")
    print(f"  normalised comparison        : {city_input.lower() == 'mumbai'}")
    print()


# ── Section 3: Logical Operators ─────────────────────────────────────────────

def section_logical():
    print("─" * 55)
    print("SECTION 3: Logical Operators")
    print("─" * 55)

    # Truth table
    combos = [(True, True), (True, False), (False, True), (False, False)]
    print(f"  {'A':<7} {'B':<7} {'A and B':<10} {'A or B':<10} {'not A'}")
    print("  " + "─" * 44)
    for a, b in combos:
        print(f"  {str(a):<7} {str(b):<7} {str(a and b):<10} {str(a or b):<10} {str(not a)}")

    # Loan eligibility
    age          = 32
    income       = 65000
    credit_score = 720
    employment   = "salaried"
    existing_loans = 1

    age_ok    = 21 <= age <= 60
    income_ok = income >= 25000
    credit_ok = credit_score >= 650
    employ_ok = employment in ("salaried", "self-employed")
    loans_ok  = existing_loans < 3
    eligible  = age_ok and income_ok and credit_ok and employ_ok and loans_ok

    print(f"\n  Loan eligibility:")
    print(f"    Age OK      : {age_ok}  ({age})")
    print(f"    Income OK   : {income_ok}  (₹{income:,})")
    print(f"    Credit OK   : {credit_ok}  ({credit_score})")
    print(f"    Employment  : {employ_ok}  ({employment})")
    print(f"    Loans OK    : {loans_ok}  ({existing_loans})")
    print(f"    Eligible    : {eligible}")

    # Short-circuit + default value
    user_city    = None
    default_city = "Mumbai"
    city = user_city or default_city
    print(f"\n  Short-circuit default: city = {city!r}")
    print()


# ── Section 4: Membership and Identity ───────────────────────────────────────

def section_membership_identity():
    print("─" * 55)
    print("SECTION 4: Membership (in/not in) and Identity (is/is not)")
    print("─" * 55)

    # Membership
    email = "priya@gmail.com"
    print(f"  '@' in '{email}'     : {'@' in email}")
    print(f"  'yahoo' in '{email}' : {'yahoo' in email}")

    VALID_GRADES      = {"A", "B", "C", "D", "F"}
    VALID_DEPARTMENTS = {"CS", "EC", "ME", "CE", "IT"}

    student_records = [
        {"name": "Priya",  "grade": "A", "dept": "CS"},
        {"name": "Meera",  "grade": "X", "dept": "CS"},  # invalid grade
        {"name": "Karan",  "grade": "C", "dept": "BA"},  # invalid dept
    ]

    print(f"\n  {'Name':<10} {'Grade':<8} {'Dept':<6} {'Status'}")
    print("  " + "─" * 48)
    for s in student_records:
        grade_ok = s["grade"] in VALID_GRADES
        dept_ok  = s["dept"]  in VALID_DEPARTMENTS
        issues   = []
        if not grade_ok: issues.append(f"invalid grade '{s['grade']}'")
        if not dept_ok:  issues.append(f"invalid dept '{s['dept']}'")
        status = "✓ OK" if not issues else "✗ " + ", ".join(issues)
        print(f"  {s['name']:<10} {s['grade']:<8} {s['dept']:<6} {status}")

    # Identity
    value = None
    print(f"\n  value is None     : {value is None}")
    print(f"  value is not None : {value is not None}")
    print(f"  Rule: use 'is'/'is not' only for None, True, False")
    print()


# ── Section 5: if / elif / else ───────────────────────────────────────────────

def section_conditions():
    print("─" * 55)
    print("SECTION 5: Conditions — if / elif / else")
    print("─" * 55)

    def get_grade(score):
        if score >= 90:   return "A+", "Distinction"
        elif score >= 80: return "A",  "First Class"
        elif score >= 70: return "B",  "Second Class"
        elif score >= 60: return "C",  "Pass Class"
        elif score >= 40: return "D",  "Pass"
        else:             return "F",  "Fail"

    test_scores = [95, 82, 74, 61, 45, 32]
    print(f"  {'Score':>6}  {'Grade':<5}  {'Category'}")
    print("  " + "─" * 28)
    for s in test_scores:
        grade, cat = get_grade(s)
        print(f"  {s:>6}  {grade:<5}  {cat}")

    # Wrong order demo
    def get_grade_wrong(score):
        if score >= 40:   return "D"   # too broad — catches 95 too
        elif score >= 60: return "C"
        elif score >= 80: return "A"

    print(f"\n  Wrong grader (score 95) → '{get_grade_wrong(95)}' (should be A+)")
    print(f"  Correct grader (score 95) → '{get_grade(95)[0]}'")

    # Ternary
    score = 75
    status = "Pass" if score >= 40 else "Fail"
    print(f"\n  Ternary: {score} → '{status}'")
    email = None
    display = email if email is not None else "Not provided"
    print(f"  Ternary None fallback: email = {display!r}")
    print()


# ── Section 6: Applied — Data Quality Checker ────────────────────────────────

def section_data_quality():
    print("─" * 55)
    print("SECTION 6: Data Quality Checker")
    print("─" * 55)

    def check_row_quality(row):
        issues = []
        if not isinstance(row.get("name"), str) or not row["name"].strip():
            issues.append("missing/empty name")
        age = row.get("age")
        if age is None:
            issues.append("missing age")
        elif not isinstance(age, int) or not (15 <= age <= 35):
            issues.append(f"age out of range ({age})")
        score = row.get("score")
        if score is None:
            issues.append("missing score")
        elif not isinstance(score, (int, float)) or not (0 <= score <= 100):
            issues.append(f"score out of range ({score})")
        email = row.get("email")
        if email is not None and "@" not in str(email):
            issues.append(f"invalid email ({email})")
        return issues

    dataset = [
        {"name": "Priya",  "age": 20, "score": 88.5, "email": "priya@gmail.com"},
        {"name": "",       "age": 21, "score": 72.0, "email": "rohan@gmail.com"},
        {"name": "Meera",  "age": 19, "score": 115,  "email": "meera@gmail.com"},
        {"name": "Karan",  "age": 99, "score": 60.0, "email": None},
        {"name": "Ananya", "age": 22, "score": 91.0, "email": "ananya_no_at_sign"},
    ]

    print(f"  {'Name':<10}  {'Status'}")
    print("  " + "─" * 55)
    clean = dirty = 0
    for row in dataset:
        name   = row.get("name") or "(no name)"
        issues = check_row_quality(row)
        if issues:
            print(f"  {name:<10}  ✗ {'; '.join(issues)}")
            dirty += 1
        else:
            print(f"  {name:<10}  ✓ OK")
            clean += 1
    print(f"\n  Clean: {clean}  Dirty: {dirty}  Total: {len(dataset)}")
    print()


# ── Section 7: Applied — Discount Engine ─────────────────────────────────────

def section_discount_engine():
    print("─" * 55)
    print("SECTION 7: Discount Engine")
    print("─" * 55)

    def calculate_discount(order_amount, is_premium, coupon_code, first_order):
        valid_coupons = {"SAVE20": 20, "FLAT10": 10, "YTV15": 15}
        if first_order:
            return 25, "First order discount"
        if coupon_code in valid_coupons:
            pct = valid_coupons[coupon_code]
            return pct, f"Coupon '{coupon_code}'"
        if is_premium and order_amount >= 1000:
            return 15, "Premium member + large order"
        elif is_premium:
            return 10, "Premium member"
        if order_amount >= 5000:
            return 12, "Bulk order (₹5000+)"
        elif order_amount >= 2000:
            return 8, "Large order (₹2000+)"
        return 0, "No discount"

    orders = [
        (800,  False, None,     True),
        (1500, True,  None,     False),
        (3000, False, "SAVE20", False),
        (6000, False, None,     False),
        (500,  False, "NOPE99", False),
        (2500, True,  "YTV15",  False),
    ]

    print(f"  {'Amount':>8}  {'Disc%':>6}  {'Saves':>8}  {'Reason'}")
    print("  " + "─" * 55)
    for amount, premium, coupon, first in orders:
        pct, reason = calculate_discount(amount, premium, coupon, first)
        savings     = amount * pct / 100
        print(f"  ₹{amount:>7,}  {pct:>5}%  ₹{savings:>6.0f}  {reason}")
    print()


# ── Section 8: Applied — Fraud Rule Engine ────────────────────────────────────

def section_fraud_engine():
    print("─" * 55)
    print("SECTION 8: Transaction Fraud Rule Engine")
    print("─" * 55)

    def assess_fraud_risk(txn):
        rules_triggered = []
        risk_score      = 0
        if txn["amount"] > txn["account_avg"] * 3:
            rules_triggered.append("Amount 3× avg")
            risk_score += 40
        if 1 <= txn["hour"] <= 5:
            rules_triggered.append("Unusual hour")
            risk_score += 25
        if txn["merchant_country"] != txn["home_country"]:
            rules_triggered.append("Foreign merchant")
            risk_score += 20
        HIGH_RISK = {"crypto", "gambling", "wire_transfer"}
        if txn["category"] in HIGH_RISK:
            rules_triggered.append(f"High-risk category")
            risk_score += 35
        if txn.get("impossible_travel", False):
            rules_triggered.append("Impossible travel")
            risk_score += 60
        if risk_score >= 70:   level = "HIGH — BLOCK"
        elif risk_score >= 40: level = "MEDIUM — FLAG"
        elif risk_score > 0:   level = "LOW — MONITOR"
        else:                  level = "CLEAR"
        return risk_score, level, rules_triggered

    transactions = [
        {"id": "T001", "amount": 500,   "account_avg": 400,  "hour": 14,
         "merchant_country": "IN", "home_country": "IN", "category": "food"},
        {"id": "T002", "amount": 45000, "account_avg": 3000, "hour": 3,
         "merchant_country": "US", "home_country": "IN", "category": "electronics"},
        {"id": "T003", "amount": 2000,  "account_avg": 4000, "hour": 21,
         "merchant_country": "IN", "home_country": "IN", "category": "gambling"},
        {"id": "T004", "amount": 800,   "account_avg": 600,  "hour": 11,
         "merchant_country": "AE", "home_country": "IN", "category": "shopping",
         "impossible_travel": True},
    ]

    for txn in transactions:
        score, level, rules = assess_fraud_risk(txn)
        rules_str = ", ".join(rules) if rules else "none"
        amt_str = f"{txn['amount']:,}"
        print(f"  {txn['id']}  ₹{amt_str:<9}  Score:{score:>3}  {level:<18}  Rules: {rules_str}")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 02 LESSON 02 — Operators and Conditions")
    print("=" * 55)
    print()

    section_arithmetic()
    section_comparison()
    section_logical()
    section_membership_identity()
    section_conditions()
    section_data_quality()
    section_discount_engine()
    section_fraud_engine()

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
