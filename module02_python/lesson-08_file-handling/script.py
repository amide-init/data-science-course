"""
File Handling (TXT, CSV, JSON)
Module 02, Lesson 08

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""

import os
import csv
import json


# ── Helpers (reused across sections) ─────────────────────────────────────────

def safe_float(value, default=None):
    if value is None or str(value).strip() == "":
        return default
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

def safe_int(value, default=None):
    if value is None or str(value).strip() == "":
        return default
    try:
        return int(float(value))
    except (ValueError, TypeError):
        return default


# ── Section 1: Opening and Reading Text Files ─────────────────────────────────

def section_text_files():
    print("─" * 55)
    print("SECTION 1: Text Files (read / write)")
    print("─" * 55)

    # Write
    sample_text = "Student Report — Batch 2024\nName: Priya Sharma\nScore: 88\nCity: Mumbai\n"
    with open("sample.txt", "w", encoding="utf-8") as f:
        f.write(sample_text)
    print(f"  Written sample.txt ({os.path.getsize('sample.txt')} bytes)")

    # f.read() — entire file
    with open("sample.txt", "r", encoding="utf-8") as f:
        content = f.read()
    preview = repr(content[:60])
    print(f"\n  f.read(): {preview}...")

    # f.readlines() — list of lines
    with open("sample.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"\n  f.readlines() → {len(lines)} lines")

    # Iterate line by line
    print("\n  Line-by-line (stripped):")
    with open("sample.txt", "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if stripped:
                print(f"    {stripped}")

    # Write modes: w vs a
    with open("log.txt", "w", encoding="utf-8") as f:
        f.write("Session started\nLoaded 100 records\n")
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write("Processing complete\n3 errors found\n")
    with open("log.txt", "r", encoding="utf-8") as f:
        print(f"\n  log.txt after w then a:\n{f.read()}")

    # writelines
    entries = ["Priya: 88", "Rohan: 72", "Meera: 95"]
    with open("scores.txt", "w", encoding="utf-8") as f:
        f.writelines(line + "\n" for line in entries)
    with open("scores.txt", "r", encoding="utf-8") as f:
        print(f"  scores.txt:\n{f.read()}")


# ── Section 2: File Paths ─────────────────────────────────────────────────────

def section_paths():
    print("─" * 55)
    print("SECTION 2: File Paths (os.path)")
    print("─" * 55)

    file_path = os.path.join("data", "students.csv")
    print(f"  os.path.join   : {file_path}")
    print(f"  exists         : {os.path.exists(file_path)}")
    print(f"  dirname        : {os.path.dirname(file_path)}")
    print(f"  basename       : {os.path.basename(file_path)}")
    name, ext = os.path.splitext(file_path)
    print(f"  name / ext     : {name!r} / {ext!r}")

    os.makedirs("output", exist_ok=True)
    print(f"\n  output/ created: {os.path.isdir('output')}")

    if os.path.isdir("data"):
        print(f"\n  Files in data/:")
        for fn in sorted(os.listdir("data")):
            fp = os.path.join("data", fn)
            print(f"    {fn:<25} ({os.path.getsize(fp)} bytes)")
    print()


# ── Section 3: Reading CSV ────────────────────────────────────────────────────

def section_read_csv():
    print("─" * 55)
    print("SECTION 3: Reading CSV")
    print("─" * 55)

    CSV_PATH = os.path.join("data", "students.csv")

    # csv.reader
    rows = []
    with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            rows.append(row)

    print(f"  csv.reader — header: {header}")
    print(f"  Total rows: {len(rows)}")
    print(f"  Row[0] (positional): {rows[0]}")

    # csv.DictReader
    records = []
    with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(dict(row))

    print(f"\n  csv.DictReader — {len(records)} records")
    print(f"  Record[0] (named): {records[0]}")

    # Type conversion demo
    print(f"\n  {'Name':<16} {'Raw':>8} {'Converted':>10} {'Type':<8}")
    print("  " + "─" * 46)
    for r in records[:6]:
        raw  = r["score"]
        conv = safe_float(raw)
        print(f"  {r['name']:<16} {str(raw):>8} {str(conv):>10} {type(conv).__name__:<8}")

    # Parse all
    def parse_student(raw):
        return {
            "name"  : raw["name"].strip().title(),
            "age"   : safe_int(raw["age"]),
            "city"  : raw["city"].strip().title(),
            "dept"  : raw["dept"].strip().upper(),
            "score" : safe_float(raw["score"]),
            "valid" : safe_float(raw["score"]) is not None,
        }

    students = [parse_student(r) for r in records]
    valid    = [s for s in students if s["valid"]]
    invalid  = [s for s in students if not s["valid"]]

    print(f"\n  Parsed: {len(valid)} valid | {len(invalid)} missing score")
    print(f"  Missing: {[s['name'] for s in invalid]}")
    print()
    return valid, invalid


# ── Section 4: Writing CSV ────────────────────────────────────────────────────

def section_write_csv(students):
    print("─" * 55)
    print("SECTION 4: Writing CSV")
    print("─" * 55)

    os.makedirs("output", exist_ok=True)

    # Dept summary with csv.writer
    dept_groups = {}
    for s in students:
        dept_groups.setdefault(s["dept"], []).append(s["score"])

    summary_rows = []
    for dept, scores in sorted(dept_groups.items()):
        avg = sum(scores) / len(scores)
        summary_rows.append([dept, len(scores), round(avg, 1), min(scores), max(scores)])

    out_path = os.path.join("output", "dept_summary.csv")
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["dept", "count", "avg_score", "min_score", "max_score"])
        writer.writerows(summary_rows)
    print(f"  csv.writer → {out_path}")

    # Full records with DictWriter
    def add_grade(s):
        sc = s["score"]
        g  = "A" if sc >= 80 else "B" if sc >= 60 else "C" if sc >= 40 else "F"
        return {**s, "grade": g}

    graded   = [add_grade(s) for s in students]
    out_path = os.path.join("output", "students_clean.csv")
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f,
                                fieldnames=["name", "age", "city", "dept", "score", "grade"],
                                extrasaction="ignore")
        writer.writeheader()
        writer.writerows(graded)

    print(f"  DictWriter  → {out_path} ({len(graded)} rows)")

    # Verify
    with open(out_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        sample = list(reader)[:3]
    print(f"\n  Preview (first 3 rows):")
    for row in sample:
        print(f"    {row['name']:<16} {row['dept']:<4} {float(row['score']):>6.1f} {row['grade']}")
    print()
    return dept_groups


# ── Section 5: JSON Files ─────────────────────────────────────────────────────

def section_json():
    print("─" * 55)
    print("SECTION 5: JSON Files")
    print("─" * 55)

    os.makedirs("output", exist_ok=True)

    # Write JSON
    config = {
        "app": "Student Analytics v1.0",
        "settings": {
            "passing_score": 40,
            "grade_thresholds": {"A": 80, "B": 60, "C": 40},
            "valid_depts": ["CS", "ME", "IT", "EE"],
        },
        "output_dir": "output",
    }
    config_path = os.path.join("output", "config.json")
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)
    print(f"  json.dump → {config_path}")

    # Read JSON
    with open(config_path, "r", encoding="utf-8") as f:
        loaded = json.load(f)
    print(f"  json.load → app: {loaded['app']}")
    print(f"             pass mark: {loaded['settings']['passing_score']}")

    # json.dumps / json.loads (string roundtrip)
    student_dict = {"name": "Priya Sharma", "score": 88, "dept": "CS"}
    s = json.dumps(student_dict)
    back = json.loads(s)
    print(f"\n  json.dumps → {s!r}")
    print(f"  json.loads → score+10 = {back['score'] + 10}")
    print()


# ── Section 6: File Exception Handling ───────────────────────────────────────

def section_file_exceptions():
    print("─" * 55)
    print("SECTION 6: Exception Handling for Files")
    print("─" * 55)

    def safe_read_file(path, encoding="utf-8"):
        try:
            with open(path, "r", encoding=encoding) as f:
                return f.read(), None
        except FileNotFoundError:
            return None, f"File not found: {path}"
        except PermissionError:
            return None, f"Permission denied: {path}"
        except UnicodeDecodeError as e:
            return None, f"Encoding error: {e}"

    def load_csv(path):
        try:
            with open(path, "r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f)
                if reader.fieldnames is None:
                    return [], "File appears to be empty"
                return [dict(row) for row in reader], None
        except FileNotFoundError:
            return [], f"File not found: {path}"
        except Exception as e:
            return [], f"Unexpected error: {e}"

    for path in ["sample.txt", "no_such_file.txt", "data/students.csv"]:
        content, error = safe_read_file(path)
        if error:
            print(f"  ✗ {error}")
        else:
            first_line = content.split("\n")[0]
            print(f"  ✓ {path} — first line: {first_line!r}")

    data, err = load_csv("data/students.csv")
    print(f"\n  load_csv('students.csv') → {len(data)} rows, error={err!r}")
    data2, err2 = load_csv("data/missing.csv")
    print(f"  load_csv('missing.csv')  → {len(data2)} rows, error={err2!r}")
    print()


# ── Section 7: Complete File Pipeline ────────────────────────────────────────

def section_pipeline():
    print("─" * 55)
    print("SECTION 7: Complete File Pipeline")
    print("─" * 55)

    os.makedirs("output", exist_ok=True)

    def load_csv(path):
        try:
            with open(path, "r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f)
                if reader.fieldnames is None:
                    return [], "File appears to be empty"
                return [dict(row) for row in reader], None
        except FileNotFoundError:
            return [], f"File not found: {path}"
        except Exception as e:
            return [], f"Unexpected error: {e}"

    def clean_record(raw, row_num):
        name  = str(raw.get("name") or "").strip().title()
        if not name:
            return None, f"Row {row_num}: name is blank"
        age   = safe_int(raw.get("age"))
        city  = str(raw.get("city") or "").strip().title()
        dept  = str(raw.get("dept") or "").strip().upper()
        score = safe_float(raw.get("score"))
        if score is None:
            return None, f"Row {row_num}: {name!r} — missing/invalid score"
        if not (0 <= score <= 100):
            return None, f"Row {row_num}: {name!r} — score {score} out of range"
        grade = "A" if score >= 80 else "B" if score >= 60 else "C" if score >= 40 else "F"
        return {"name": name, "age": age, "city": city, "dept": dept,
                "score": score, "grade": grade}, None

    def compute_stats(values):
        if not values: return {}
        n = len(values)
        mean = sum(values) / n
        sv   = sorted(values)
        mid  = n // 2
        med  = sv[mid] if n % 2 else (sv[mid-1] + sv[mid]) / 2
        std  = (sum((x-mean)**2 for x in values) / n) ** 0.5
        return {"count": n, "mean": round(mean, 1), "median": round(med, 1),
                "std": round(std, 1), "min": min(values), "max": max(values)}

    # Step 1: Load
    raw_records, err = load_csv(os.path.join("data", "students.csv"))
    if err:
        print(f"  ERROR: {err}")
        return
    print(f"  Step 1: Loaded {len(raw_records)} raw records")

    # Step 2: Clean
    clean_records, error_log = [], []
    for i, raw in enumerate(raw_records):
        cleaned, error = clean_record(raw, i + 2)
        if cleaned:
            clean_records.append(cleaned)
        else:
            error_log.append(error)
    print(f"  Step 2: {len(clean_records)} clean | {len(error_log)} errors")

    # Step 3: Analyse
    all_scores   = [s["score"] for s in clean_records]
    overall      = compute_stats(all_scores)
    dept_groups  = {}
    for s in clean_records:
        dept_groups.setdefault(s["dept"], []).append(s["score"])
    dept_analysis = {d: compute_stats(sc) for d, sc in sorted(dept_groups.items())}
    grade_count   = {}
    for s in clean_records:
        grade_count[s["grade"]] = grade_count.get(s["grade"], 0) + 1

    # Step 4: Write output CSV
    out_csv = os.path.join("output", "pipeline_output.csv")
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age", "city", "dept", "score", "grade"])
        writer.writeheader()
        writer.writerows(clean_records)
    print(f"  Step 4: Wrote {len(clean_records)} rows → {out_csv}")

    # Step 5: Write summary report
    total = len(clean_records)
    lines = [
        "=" * 50, "STUDENT ANALYTICS REPORT", "=" * 50, "",
        f"Total records loaded  : {len(raw_records)}",
        f"Clean records         : {len(clean_records)}",
        f"Records with errors   : {len(error_log)}", "",
        "OVERALL STATISTICS", "-" * 30,
        f"Count   : {overall['count']}",
        f"Mean    : {overall['mean']}",
        f"Median  : {overall['median']}",
        f"Std Dev : {overall['std']}",
        f"Min     : {overall['min']}",
        f"Max     : {overall['max']}",
        f"Pass rate (>=40): {sum(1 for x in all_scores if x>=40)/len(all_scores)*100:.0f}%",
        "", "BY DEPARTMENT", "-" * 30,
    ]
    for dept, stats in dept_analysis.items():
        lines.append(f"  {dept:<4}  n={stats['count']}  mean={stats['mean']}  "
                     f"min={stats['min']}  max={stats['max']}")
    lines += ["", "GRADE DISTRIBUTION", "-" * 30]
    for grade in ["A", "B", "C", "F"]:
        count = grade_count.get(grade, 0)
        bar   = "█" * int(count / total * 20)
        lines.append(f"  {grade}: {count:>3}  {count/total*100:>5.1f}%  {bar}")
    lines += ["", "ERRORS", "-" * 30]
    for err in error_log:
        lines.append(f"  {err}")
    lines.append("=" * 50)

    report_path = os.path.join("output", "summary_report.txt")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  Step 5: Report written → {report_path}")

    print()
    with open(report_path, "r", encoding="utf-8") as f:
        print(f.read())


# ── Section 8: Common Mistakes ────────────────────────────────────────────────

def section_mistakes():
    print("─" * 55)
    print("SECTION 8: Common Mistakes")
    print("─" * 55)

    # Mistake 2: 'w' overwrites silently
    with open("important.txt", "w", encoding="utf-8") as f:
        f.write("Important data!\n")
    with open("important.txt", "w", encoding="utf-8") as f:
        f.write("Overwritten — data is gone.\n")
    with open("important.txt", "r", encoding="utf-8") as f:
        print(f"  Mistake 2 (w overwrites): {f.read()!r}")

    with open("important.txt", "a", encoding="utf-8") as f:
        f.write("Appended safely.\n")
    with open("important.txt", "r", encoding="utf-8") as f:
        print(f"  Fixed with 'a':           {f.read()!r}")

    # Mistake 5: missing \n
    with open("noeol.txt", "w", encoding="utf-8") as f:
        f.write("line one")
        f.write("line two")
    with open("noeol.txt", "r", encoding="utf-8") as f:
        print(f"\n  Mistake 5 (no \\n): {f.read()!r}")

    with open("noeol.txt", "w", encoding="utf-8") as f:
        f.write("line one\n")
        f.write("line two\n")
    with open("noeol.txt", "r", encoding="utf-8") as f:
        print(f"  Fixed (with \\n): {f.read()!r}")

    print("\n  Mistake 1: Always use 'with open()' — never open()/close() manually.")
    print("  Mistake 3: Always pass newline='' to csv.writer/DictWriter.")
    print("  Mistake 4: Always pass encoding='utf-8' to open().")
    print()


# ── Cleanup: remove temp files created during demo ────────────────────────────

def cleanup():
    for f in ["sample.txt", "log.txt", "scores.txt", "important.txt", "noeol.txt"]:
        try:
            os.remove(f)
        except FileNotFoundError:
            pass


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 02 LESSON 08 — File Handling")
    print("=" * 55)
    print()

    section_text_files()
    section_paths()
    valid, invalid = section_read_csv()
    dept_groups = section_write_csv(valid)
    section_json()
    section_file_exceptions()
    section_pipeline()
    section_mistakes()
    cleanup()

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
