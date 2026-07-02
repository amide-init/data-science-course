"""
Matrices and Matrix Multiplication
Module 03, Lesson 08

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""


# ── Core Functions ────────────────────────────────────────────────────────────

def shape(M):
    """Return (num_rows, num_cols) for a matrix M."""
    return (len(M), len(M[0]) if M else 0)

def matrix_add(A, B):
    """Add two matrices element-wise. Must have identical shapes."""
    if shape(A) != shape(B):
        raise ValueError(f"Cannot add matrices of shape {shape(A)} and {shape(B)}")
    return [[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(A, B)]

def matrix_subtract(A, B):
    """Subtract matrix B from matrix A, element-wise. Must have identical shapes."""
    if shape(A) != shape(B):
        raise ValueError(f"Cannot subtract matrices of shape {shape(A)} and {shape(B)}")
    return [[a - b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(A, B)]

def scalar_multiply_matrix(k, M):
    """Multiply every entry of matrix M by scalar k."""
    return [[k * x for x in row] for row in M]

def transpose(M):
    """Flip a matrix's rows and columns."""
    rows, cols = shape(M)
    return [[M[r][c] for r in range(rows)] for c in range(cols)]

def matrix_multiply(A, B):
    """Multiply matrix A by matrix B. Requires cols(A) == rows(B)."""
    rows_a, cols_a = shape(A)
    rows_b, cols_b = shape(B)
    if cols_a != rows_b:
        raise ValueError(
            f"Cannot multiply {shape(A)} by {shape(B)}: "
            f"inner dimensions must match ({cols_a} != {rows_b})"
        )
    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            value = sum(A[i][k] * B[k][j] for k in range(cols_a))
            row.append(value)
        result.append(row)
    return result

def elementwise_multiply(A, B):
    """Multiply two SAME-SHAPE matrices entry-by-entry (NOT true matrix multiplication)."""
    if shape(A) != shape(B):
        raise ValueError(f"Cannot elementwise-multiply shapes {shape(A)} and {shape(B)}")
    return [[a * b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(A, B)]

def identity_matrix(n):
    """An n x n identity matrix: 1s on the diagonal, 0s elsewhere."""
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def print_matrix(M, label=""):
    """Pretty-print a matrix with aligned columns."""
    if label:
        print(f"  {label}")
    for row in M:
        print("   [" + "  ".join(f"{x:>6}" for x in row) + "]")
    print()


# ── Section 1/2: What Is a Matrix? ───────────────────────────────────────────

def section_matrix_basics():
    print("─" * 55)
    print("SECTION 1-2: What Is a Matrix?")
    print("─" * 55)

    students_matrix = [[8, 85, 92], [3, 55, 70], [7, 80, 88]]
    print_matrix(students_matrix, f"students_matrix, shape {shape(students_matrix)}")
    return students_matrix


# ── Section 3: Shape ──────────────────────────────────────────────────────────

def section_shape():
    print("─" * 55)
    print("SECTION 3: Matrix Shape")
    print("─" * 55)

    rectangular = [[1, 2, 3], [4, 5, 6]]
    print(f"  rectangular shape: {shape(rectangular)}")
    print()


# ── Section 4: Addition, Subtraction, Scalar Multiplication ─────────────────

def section_arithmetic():
    print("─" * 55)
    print("SECTION 4: Matrix Addition/Subtraction/Scalar Mult")
    print("─" * 55)

    attempt_1 = [[70, 65], [80, 75], [60, 55]]
    attempt_2 = [[75, 70], [85, 80], [65, 60]]
    combined = matrix_add(attempt_1, attempt_2)
    print_matrix(combined, "attempt_1 + attempt_2")


# ── Section 5: Transpose ──────────────────────────────────────────────────────

def section_transpose(students_matrix):
    print("─" * 55)
    print("SECTION 5: The Transpose")
    print("─" * 55)

    students_T = transpose(students_matrix)
    print_matrix(students_T, f"transpose(students_matrix), shape {shape(students_T)}")


# ── Section 6/7: Matrix Multiplication ───────────────────────────────────────

def section_multiplication():
    print("─" * 55)
    print("SECTION 6-7: Matrix Multiplication")
    print("─" * 55)

    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    C = matrix_multiply(A, B)
    print_matrix(C, f"A @ B, shape {shape(C)}")


# ── Section 8: Element-wise vs Matrix Multiplication ─────────────────────────

def section_elementwise_vs_matmul():
    print("─" * 55)
    print("SECTION 8: Element-wise vs Matrix Multiplication")
    print("─" * 55)

    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    print(f"  elementwise: {elementwise_multiply(A, B)}")
    print(f"  matmul     : {matrix_multiply(A, B)}")
    print()


# ── Section 9: Identity Matrix ────────────────────────────────────────────────

def section_identity(students_matrix):
    print("─" * 55)
    print("SECTION 9: The Identity Matrix")
    print("─" * 55)

    I3 = identity_matrix(3)
    result = matrix_multiply(students_matrix, I3)
    print(f"  students_matrix @ I3 == students_matrix : {result == students_matrix}")
    print()


# ── Section 10: Applied — Weighted Scores ────────────────────────────────────

def section_weighted_scores():
    print("─" * 55)
    print("SECTION 10: Applied — Weighted Scores")
    print("─" * 55)

    students_scores = [[80, 85, 90], [60, 70, 75], [95, 90, 88], [70, 65, 72]]
    weights = [[0.20], [0.20], [0.60]]
    final_grades = matrix_multiply(students_scores, weights)

    names = ["Aisha", "Vikram", "Sara", "Dev"]
    for name, row in zip(names, final_grades):
        print(f"    {name:<8}: {row[0]:.1f}")
    print()


# ── Section 11: Sanity-Check Property ────────────────────────────────────────

def section_property_check():
    print("─" * 55)
    print("SECTION 11: Sanity-Check (A@B)^T == B^T@A^T")
    print("─" * 55)

    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    left = transpose(matrix_multiply(A, B))
    right = matrix_multiply(transpose(B), transpose(A))
    print(f"  Property holds: {left == right}")
    print()


# ── Section 12: Common Mistakes ───────────────────────────────────────────────

def section_mistakes():
    print("─" * 55)
    print("SECTION 12: Common Mistakes")
    print("─" * 55)

    try:
        matrix_add([[1, 2], [3, 4]], [[1, 2, 3], [4, 5, 6]])
    except ValueError as e:
        print(f"  Mistake 1 — {e}")

    A, B = [[1, 2], [3, 4]], [[5, 6], [7, 8]]
    print(f"  Mistake 2 — elementwise={elementwise_multiply(A, B)} vs "
          f"matmul={matrix_multiply(A, B)}")

    try:
        matrix_multiply([[1, 2, 3]], [[1, 2, 3]])
    except ValueError as e:
        print(f"  Mistake 3 — {e}")

    AB = matrix_multiply([[1, 2], [3, 4]], [[2, 0], [1, 2]])
    BA = matrix_multiply([[2, 0], [1, 2]], [[1, 2], [3, 4]])
    print(f"  Mistake 4 — A@B == B@A : {AB == BA}")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 03 LESSON 08 — Matrices and Matrix Multiplication")
    print("=" * 55)
    print()

    students_matrix = section_matrix_basics()
    section_shape()
    section_arithmetic()
    section_transpose(students_matrix)
    section_multiplication()
    section_elementwise_vs_matmul()
    section_identity(students_matrix)
    section_weighted_scores()
    section_property_check()
    section_mistakes()

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
