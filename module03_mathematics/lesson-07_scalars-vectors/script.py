"""
Scalars and Vectors
Module 03, Lesson 07

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""

import math
import random


# ── Core Functions ────────────────────────────────────────────────────────────

def vector_add(a, b):
    """Add two vectors component-wise. Both must be the same length."""
    if len(a) != len(b):
        raise ValueError(f"Cannot add vectors of different dimensions: {len(a)} vs {len(b)}")
    return [ai + bi for ai, bi in zip(a, b)]

def vector_subtract(a, b):
    """Subtract vector b from vector a, component-wise."""
    if len(a) != len(b):
        raise ValueError(f"Cannot subtract vectors of different dimensions: {len(a)} vs {len(b)}")
    return [ai - bi for ai, bi in zip(a, b)]

def scalar_multiply(k, v):
    """Multiply every component of vector v by scalar k."""
    return [k * vi for vi in v]

def magnitude(v):
    """Euclidean length (norm) of a vector."""
    return math.sqrt(sum(vi ** 2 for vi in v))

def distance(a, b):
    """Euclidean distance between two vectors."""
    return magnitude(vector_subtract(a, b))

def unit_vector(v):
    """Normalize v to a unit vector (magnitude 1), preserving direction."""
    m = magnitude(v)
    if m == 0:
        raise ValueError("Cannot normalize the zero vector (magnitude is 0)")
    return scalar_multiply(1 / m, v)

def ascii_vector_2d(vectors, labels, grid_size=21):
    """Plot 2D vectors as lines from the origin on a small ASCII grid."""
    half = grid_size // 2
    grid = [[" "] * grid_size for _ in range(grid_size)]
    grid[half][half] = "o"

    symbols = "ABCDEFG"
    for i, (vx, vy) in enumerate(vectors):
        steps = max(int(max(abs(vx), abs(vy)) * 4), 1)
        for s in range(steps + 1):
            t = s / steps
            col = half + round(vx * t)
            row = half - round(vy * t)
            if 0 <= row < grid_size and 0 <= col < grid_size and grid[row][col] == " ":
                grid[row][col] = symbols[i]
        end_col, end_row = half + round(vx), half - round(vy)
        if 0 <= end_row < grid_size and 0 <= end_col < grid_size:
            grid[end_row][end_col] = symbols[i]

    for row in grid:
        print("  " + "".join(row))
    for i, lab in enumerate(labels):
        print(f"  {symbols[i]} = {lab}")


# ── Section 1: Scalars vs Vectors ────────────────────────────────────────────

def section_scalars_vectors():
    print("─" * 55)
    print("SECTION 1: Scalars vs Vectors")
    print("─" * 55)

    priya = [8, 85, 92]
    print(f"  Vector (Priya's record) : {priya}")
    print(f"  Dimension                : {len(priya)}")
    print()


# ── Section 2: 2D Visualisation ──────────────────────────────────────────────

def section_visualisation():
    print("─" * 55)
    print("SECTION 2: Visualising Vectors")
    print("─" * 55)

    v1, v2 = [3, 4], [-4, 2]
    ascii_vector_2d([v1, v2], [f"{v1}", f"{v2}"])
    print()


# ── Section 3: Addition and Subtraction ──────────────────────────────────────

def section_add_subtract():
    print("─" * 55)
    print("SECTION 3: Vector Addition and Subtraction")
    print("─" * 55)

    v1, v2 = [3, 4], [-4, 2]
    print(f"  v1 + v2 = {vector_add(v1, v2)}")
    print(f"  v1 - v2 = {vector_subtract(v1, v2)}")
    print()


# ── Section 4: Scalar Multiplication ─────────────────────────────────────────

def section_scalar_mult():
    print("─" * 55)
    print("SECTION 4: Scalar Multiplication")
    print("─" * 55)

    v = [2, 3]
    print(f"  2*v  = {scalar_multiply(2, v)}")
    print(f"  0.5*v = {scalar_multiply(0.5, v)}")
    print(f"  -1*v = {scalar_multiply(-1, v)}")
    print()


# ── Section 5/6: Magnitude and Distance ──────────────────────────────────────

def section_magnitude_distance():
    print("─" * 55)
    print("SECTION 5-6: Magnitude and Distance")
    print("─" * 55)

    v1 = [3, 4]
    print(f"  ||{v1}|| = {magnitude(v1):.2f}")

    priya, rohan, meera = [8, 85, 92], [3, 55, 70], [7, 80, 88]
    print(f"  distance(Priya, Rohan) = {distance(priya, rohan):.2f}")
    print(f"  distance(Priya, Meera) = {distance(priya, meera):.2f}")
    print()


# ── Section 7: Unit Vectors ───────────────────────────────────────────────────

def section_unit_vector():
    print("─" * 55)
    print("SECTION 7: Unit Vectors")
    print("─" * 55)

    v = [3, 4]
    u = unit_vector(v)
    print(f"  unit({v}) = {[round(c, 4) for c in u]}   ||unit(v)||={magnitude(u):.4f}")
    print()


# ── Section 8: Applied — Nearest Neighbor ────────────────────────────────────

def section_nearest_neighbor():
    print("─" * 55)
    print("SECTION 8: Applied — Nearest Neighbor")
    print("─" * 55)

    students = {
        "Priya": [8, 85, 92],
        "Rohan": [3, 55, 70],
        "Meera": [7, 80, 88],
        "Karan": [2, 50, 65],
    }
    new_student = [7.5, 82, 90]

    distances = {name: distance(new_student, vec) for name, vec in students.items()}
    closest = min(distances, key=distances.get)
    for name, d in distances.items():
        print(f"    {name:<8}: distance = {d:.2f}")
    print(f"  Most similar: {closest}")
    print()


# ── Section 9: Built-in Verification ─────────────────────────────────────────

def section_verification():
    print("─" * 55)
    print("SECTION 9: Built-in Verification")
    print("─" * 55)

    v = [3, 4, 12]
    a, b = [8, 85, 92], [3, 55, 70]

    print(f"  magnitude: ours={magnitude(v):.4f}  stdlib={math.hypot(*v):.4f}")
    print(f"  distance : ours={distance(a, b):.4f}  stdlib={math.dist(a, b):.4f}")
    print()


# ── Section 10: Common Mistakes ───────────────────────────────────────────────

def section_mistakes():
    print("─" * 55)
    print("SECTION 10: Common Mistakes")
    print("─" * 55)

    try:
        vector_add([1, 2, 3], [4, 5])
    except ValueError as e:
        print(f"  Mistake 1 — {e}")

    print(f"  Mistake 2 — magnitude([3,4])={magnitude([3, 4])} is a SCALAR, not a vector")

    try:
        unit_vector([0, 0, 0])
    except ValueError as e:
        print(f"  Mistake 3 — {e}")

    a = [8, 85, 92]
    b_wrong = [92, 85, 8]
    print(f"  Mistake 4 — mismatched column order gives meaningless distance="
          f"{distance(a, b_wrong):.2f}")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 03 LESSON 07 — Scalars and Vectors")
    print("=" * 55)
    print()

    section_scalars_vectors()
    section_visualisation()
    section_add_subtract()
    section_scalar_mult()
    section_magnitude_distance()
    section_unit_vector()
    section_nearest_neighbor()
    section_verification()
    section_mistakes()

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
