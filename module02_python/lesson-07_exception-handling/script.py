"""
Exception Handling
Module 02, Lesson 07

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""

import random


# ── Section 1: Exception Types ────────────────────────────────────────────────

def section_exception_types():
    print("─" * 55)
    print("SECTION 1: Common Exception Types")
    print("─" * 55)

    demos = [
        ("ValueError",        lambda: int("abc")),
        ("TypeError",         lambda: "score" + 88),
        ("KeyError",          lambda: {}["name"]),
        ("IndexError",        lambda: [][0]),
        ("ZeroDivisionError", lambda: 1 / 0),
        ("AttributeError",    lambda: None.strip()),
    ]

    for exc_name, fn in demos:
        try:
            fn()
        except Exception as e:
            print(f"  {exc_name:<22} → {e}")
    print()


# ── Section 2: try / except ───────────────────────────────────────────────────

def section_try_except():
    print("─" * 55)
    print("SECTION 2: try / except")
    print("─" * 55)

    # Basic try/except
    def divide_safe(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return None

    print(f"  divide_safe(10, 2) → {divide_safe(10, 2)}")
    print(f"  divide_safe(10, 0) → {divide_safe(10, 0)!r}  (no crash)")

    # 'as e' to inspect the message
    print("\n  Conversion attempts:")
    test_values = ["42", "3.14", "abc", None, "", "99"]
    for val in test_values:
        try:
            result = int(float(val))
            print(f"    {str(val)!r:<8} → {result}")
        except (ValueError, TypeError) as e:
            print(f"    {str(val)!r:<8} → Failed: {e}")

    # Multiple separate except blocks
    def process_field(record, field):
        try:
            raw   = record[field]
            value = float(raw)
            return value / 100
        except KeyError:
            print(f"    Field '{field}' missing from record")
            return None
        except (ValueError, TypeError) as e:
            print(f"    Cannot convert {record.get(field)!r}: {e}")
            return None

    print("\n  process_field() with mixed records:")
    records = [
        {"name": "Priya", "score": "88"},
        {"name": "Rohan"},
        {"name": "Meera", "score": "N/A"},
        {"name": "Karan", "score": None},
    ]
    for r in records:
        result = process_field(r, "score")
        if result is not None:
            print(f"    {r['name']}: score/100 = {result:.2f}")
    print()


# ── Section 3: else and finally ───────────────────────────────────────────────

def section_else_finally():
    print("─" * 55)
    print("SECTION 3: else and finally")
    print("─" * 55)

    # else: success-only logic
    def parse_and_classify(raw_score):
        try:
            score = float(raw_score)
        except (ValueError, TypeError) as e:
            print(f"  Parse failed for {raw_score!r}: {e}")
            return None
        else:
            grade = "A" if score >= 80 else "B" if score >= 60 else "C" if score >= 40 else "F"
            print(f"  Parsed {raw_score!r} → {score} → Grade {grade}")
            return grade

    print("  else clause (parse_and_classify):")
    for inp in ["88", "72.5", "N/A", "", "95", None]:
        parse_and_classify(inp)

    # finally: always runs
    def load_data_simulation(source, should_fail=False):
        connection_open = False
        try:
            print(f"\n  [try]     Opening connection to '{source}'")
            connection_open = True
            if should_fail:
                raise ValueError("Source returned malformed data")
            data = [1, 2, 3, 4, 5]
            print(f"  [try]     Loaded {len(data)} records")
            return data
        except ValueError as e:
            print(f"  [except]  Error: {e}")
            return []
        finally:
            if connection_open:
                print(f"  [finally] Closing connection (always happens)")

    print("\n  finally clause:")
    print("  Case 1 — Success:")
    result = load_data_simulation("database.csv", should_fail=False)
    print(f"  Result: {result}")
    print("\n  Case 2 — Failure:")
    result = load_data_simulation("corrupt.csv", should_fail=True)
    print(f"  Result: {result}")
    print()


# ── Section 4: raise ──────────────────────────────────────────────────────────

def section_raise():
    print("─" * 55)
    print("SECTION 4: Raising Exceptions")
    print("─" * 55)

    def compute_mean(values):
        if not isinstance(values, list):
            raise TypeError(f"Expected a list, got {type(values).__name__}")
        if len(values) == 0:
            raise ValueError("Cannot compute mean of an empty list")
        return sum(values) / len(values)

    print(f"  compute_mean([85, 72, 91]) → {compute_mean([85, 72, 91]):.2f}")

    for bad_input, exc_type in [("not a list", TypeError), ([], ValueError)]:
        try:
            compute_mean(bad_input)
        except (TypeError, ValueError) as e:
            print(f"  {exc_type.__name__}: {e}")

    # validate_score with raise
    def validate_score(score, field_name="score"):
        if score is None:
            raise ValueError(f"{field_name}: value is None (required)")
        try:
            score = float(score)
        except (ValueError, TypeError):
            raise ValueError(f"{field_name}: cannot convert {score!r} to number")
        if not (0 <= score <= 100):
            raise ValueError(f"{field_name}: {score} is out of valid range [0, 100]")
        return score

    print("\n  validate_score() output:")
    for val in [88, "72.5", None, "abc", 115, 0, "100"]:
        try:
            print(f"    {str(val)!r:<10} → valid: {validate_score(val)}")
        except ValueError as e:
            print(f"    {str(val)!r:<10} → ✗ {e}")
    print()


# ── Section 5: Custom Exceptions ─────────────────────────────────────────────

class DataError(Exception):
    """Base class for all data pipeline errors."""
    pass

class MissingFieldError(DataError):
    """A required field is absent from the record."""
    def __init__(self, field, record_id=None):
        self.field     = field
        self.record_id = record_id
        super().__init__(
            f"Required field '{field}' is missing"
            + (f" (record id={record_id})" if record_id else "")
        )

class InvalidValueError(DataError):
    """A field contains a value that fails validation."""
    def __init__(self, field, value, reason):
        self.field  = field
        self.value  = value
        self.reason = reason
        super().__init__(f"Field '{field}' has invalid value {value!r}: {reason}")


def section_custom_exceptions():
    print("─" * 55)
    print("SECTION 5: Custom Exception Classes")
    print("─" * 55)

    def validate_record(record):
        if "name" not in record or not record["name"]:
            raise MissingFieldError("name", record_id=record.get("id"))
        score = record.get("score")
        if score is None:
            raise MissingFieldError("score", record_id=record.get("id"))
        if not isinstance(score, (int, float)) or not (0 <= score <= 100):
            raise InvalidValueError("score", score, "must be a number in [0, 100]")
        return True

    test_records = [
        {"id": 1, "name": "Priya",  "score": 88},
        {"id": 2, "name": "",       "score": 72},
        {"id": 3, "name": "Meera",  "score": None},
        {"id": 4, "name": "Karan",  "score": 115},
    ]

    for rec in test_records:
        try:
            validate_record(rec)
            print(f"  ID {rec['id']}: ✓ OK")
        except MissingFieldError as e:
            print(f"  ID {rec['id']}: ✗ MissingField  — {e}")
        except InvalidValueError as e:
            print(f"  ID {rec['id']}: ✗ InvalidValue  — {e}")
    print()


# ── Section 6: Three Core Data Science Patterns ───────────────────────────────

def safe_cast(value, target_type, default=None):
    """Convert value to target_type, returning default if conversion fails."""
    if value is None:
        return default
    try:
        if target_type == int:
            return int(float(value))
        return target_type(value)
    except (ValueError, TypeError):
        return default


def section_patterns():
    print("─" * 55)
    print("SECTION 6: Three Core Patterns")
    print("─" * 55)

    # Pattern 1: safe_cast
    print("  Pattern 1 — safe_cast:")
    cases = [
        ("42",   int,   None, 42),
        ("42.9", int,   None, 42),
        ("3.14", float, None, 3.14),
        (None,   float, 0.0,  0.0),
        ("",     int,   -1,   -1),
        ("abc",  float, None, None),
    ]
    for val, typ, default, expected in cases:
        result = safe_cast(val, typ, default)
        passed = result == expected
        print(f"    {str(val)!r:<8} → {str(result):<8} {'✓' if passed else '✗'}")

    # Pattern 2: batch processor
    def process_student_record(raw):
        name = str(raw.get("name") or "").strip().title()
        if not name:
            raise ValueError("name is empty or missing")
        age = safe_cast(raw.get("age"), int)
        if age is None or not (15 <= age <= 35):
            raise ValueError(f"age {raw.get('age')!r} is invalid (expected 15–35)")
        score = safe_cast(raw.get("score"), float)
        if score is None or not (0 <= score <= 100):
            raise ValueError(f"score {raw.get('score')!r} is invalid (expected 0–100)")
        return {"name": name, "age": age, "score": score,
                "grade": "A" if score >= 80 else "B" if score >= 60 else "C" if score >= 40 else "F"}

    def process_batch(raw_records):
        clean_records = []
        error_log     = []
        for i, raw in enumerate(raw_records):
            try:
                clean = process_student_record(raw)
                clean_records.append(clean)
            except ValueError as e:
                error_log.append({"row": i + 1, "error": str(e)})
        return clean_records, error_log

    raw_batch = [
        {"name": "  PRIYA SHARMA ", "age": "20",  "score": "88"},
        {"name": "rohan verma",     "age": "22",  "score": "72.5"},
        {"name": "",                "age": "19",  "score": "95"},
        {"name": "karan mehta",     "age": "abc", "score": "61"},
        {"name": "ananya singh",    "age": "22",  "score": "110"},
        {"name": "dev patel",       "age": "25",  "score": "77"},
        {"name": "riya joshi",      "age": "99",  "score": "82"},
        {"name": "arjun nair",      "age": "21",  "score": None},
        {"name": "divya rao",       "age": "23",  "score": "68"},
    ]

    clean, errors = process_batch(raw_batch)
    print(f"\n  Pattern 2 — Batch processor:")
    print(f"  {len(clean)} clean / {len(errors)} errors / {len(raw_batch)} total")
    print(f"\n  Clean records:")
    print(f"    {'Name':<16} {'Age':>4} {'Score':>6} {'Grade'}")
    print("    " + "─" * 33)
    for r in clean:
        print(f"    {r['name']:<16} {r['age']:>4} {r['score']:>6.1f} {r['grade']}")

    print(f"\n  Error log:")
    for err in errors:
        print(f"    Row {err['row']:>2}: {err['error']}")

    # Pattern 3: resilient pipeline with summary
    def run_pipeline(raw_records, processor_fn):
        results   = []
        error_log = []
        for i, raw in enumerate(raw_records):
            try:
                results.append(processor_fn(raw))
            except Exception as e:
                error_log.append({
                    "row"       : i + 1,
                    "error_type": type(e).__name__,
                    "message"   : str(e),
                })
        total  = len(raw_records)
        n_ok   = len(results)
        n_err  = len(error_log)
        err_types = {}
        for e in error_log:
            err_types[e["error_type"]] = err_types.get(e["error_type"], 0) + 1
        return {
            "results"     : results,
            "errors"      : error_log,
            "total"       : total,
            "success"     : n_ok,
            "failed"      : n_err,
            "success_rate": round(n_ok / total * 100, 1) if total else 0,
            "error_types" : err_types,
        }

    summary = run_pipeline(raw_batch, process_student_record)
    print(f"\n  Pattern 3 — Pipeline summary:")
    print(f"    Total   : {summary['total']}")
    print(f"    Success : {summary['success']} ({summary['success_rate']}%)")
    print(f"    Failed  : {summary['failed']}")
    if summary["results"]:
        scores = [r["score"] for r in summary["results"]]
        print(f"    Mean score (clean): {sum(scores)/len(scores):.1f}")
    print()


# ── Section 7: Common Mistakes ────────────────────────────────────────────────

def section_mistakes():
    print("─" * 55)
    print("SECTION 7: Common Mistakes")
    print("─" * 55)

    # Mistake 1: catching too broadly
    def bad_catch(data):
        try:
            result = data["score"] * 2
            return result
        except Exception:      # swallows all errors including bugs
            return None

    def good_catch(data):
        try:
            return data["score"] * 2
        except KeyError:       # only the specific error we expect
            return None

    print(f"  Mistake 1 — over-broad catch:")
    print(f"    bad_catch  : {bad_catch({'score': 5})} (hides NameError bugs)")
    print(f"    good_catch : {good_catch({'score': 5})} (specific)")

    # Mistake 2: silent except
    def silent_fail(value):
        try:
            return int(value)
        except:
            pass    # caller has no idea what happened

    def transparent_fail(value):
        try:
            return int(value), None
        except (ValueError, TypeError) as e:
            return None, str(e)

    val, err = transparent_fail("abc")
    print(f"\n  Mistake 2 — silent fail:")
    print(f"    silent    : {silent_fail('abc')!r}  (no context)")
    print(f"    transparent: value={val!r}, error={err!r}")

    # Mistake 3: exception order — specific before broad
    def right_order(value):
        try:
            return int(value)
        except ValueError as e:     # specific first
            return f"ValueError: {e}"
        except Exception as e:      # broad last
            return f"Unexpected: {e}"

    print(f"\n  Mistake 3 — wrong except order:")
    print(f"    right_order('abc') → {right_order('abc')}")
    print("    (always put most-specific except clause first)")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 02 LESSON 07 — Exception Handling")
    print("=" * 55)
    print()

    section_exception_types()
    section_try_except()
    section_else_finally()
    section_raise()
    section_custom_exceptions()
    section_patterns()
    section_mistakes()

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
