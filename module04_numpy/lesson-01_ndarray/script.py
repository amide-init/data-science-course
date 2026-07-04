"""
The ndarray (N-dimensional Array)
Module 04, Lesson 01

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""

import time

import numpy as np


# ── Section 1: Creating Your First Array ─────────────────────────────────────

def section_first_array():
    print("─" * 55)
    print("SECTION 1: Creating Your First Array")
    print("─" * 55)

    scores_list = [88, 92, 79, 95, 61]
    scores = np.array(scores_list)

    print(f"  scores_list : {scores_list}  (type: {type(scores_list)})")
    print(f"  scores      : {scores}       (type: {type(scores)})")
    print()


# ── Section 2: Lists vs Arrays ────────────────────────────────────────────────

def section_lists_vs_arrays():
    print("─" * 55)
    print("SECTION 2: Why Not Just Use a List?")
    print("─" * 55)

    mixed_list = [1, "two", 3.0, True]
    print(f"  mixed_list: {mixed_list}")

    numbers = np.array([1, 2, 3, 4])
    print(f"  numbers.dtype: {numbers.dtype}")
    print()


# ── Section 3: 2D and 3D Arrays ───────────────────────────────────────────────

def section_higher_dimensions():
    print("─" * 55)
    print("SECTION 3: Beyond 1D — Matrices and Higher Dimensions")
    print("─" * 55)

    grades = np.array([
        [88, 92, 79, 95],
        [61, 70, 85, 90],
        [77, 82, 91, 68],
    ])
    print("  grades (2D array):")
    print(grades)
    print(f"  ndim: {grades.ndim}")
    print()

    images = np.array([
        [[10, 20, 30], [40, 50, 60], [70, 80, 90]],
        [[15, 25, 35], [45, 55, 65], [75, 85, 95]],
    ])
    print("  images (3D array):")
    print(images)
    print(f"  ndim: {images.ndim}   shape: {images.shape}")
    print()

    return grades


# ── Section 4: Inspecting Array Properties ───────────────────────────────────

def section_inspect_properties(grades):
    print("─" * 55)
    print("SECTION 4: Inspecting an Array")
    print("─" * 55)

    print(f"  grades.shape    : {grades.shape}")
    print(f"  grades.dtype    : {grades.dtype}")
    print(f"  grades.ndim     : {grades.ndim}")
    print(f"  grades.size     : {grades.size}")
    print(f"  grades.itemsize : {grades.itemsize} bytes")
    print(f"  grades.nbytes   : {grades.nbytes} bytes")
    print()


# ── Section 5: dtype Control ──────────────────────────────────────────────────

def section_dtype_control():
    print("─" * 55)
    print("SECTION 5: dtype — Choosing and Controlling the Type")
    print("─" * 55)

    ints = np.array([1, 2, 3])
    floats = np.array([1.0, 2.5, 3.0])
    forced_float = np.array([1, 2, 3], dtype=np.float64)
    smaller_int = np.array([1, 2, 3], dtype=np.int8)

    print(f"  ints.dtype        : {ints.dtype}")
    print(f"  floats.dtype       : {floats.dtype}")
    print(f"  forced_float.dtype : {forced_float.dtype}")
    print(f"  smaller_int.dtype  : {smaller_int.dtype}")
    print(f"  ints memory: {ints.nbytes} bytes | smaller_int memory: {smaller_int.nbytes} bytes")
    print()


# ── Section 6: Reshaping ──────────────────────────────────────────────────────

def section_reshaping():
    print("─" * 55)
    print("SECTION 6: Reshaping — Same Data, Different Shape")
    print("─" * 55)

    flat = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    print(f"  flat (shape {flat.shape}): {flat}")

    as_3x4 = flat.reshape(3, 4)
    print(f"  reshape(3, 4):\n{as_3x4}")

    as_2x6 = flat.reshape(2, 6)
    print(f"  reshape(2, 6):\n{as_2x6}")

    as_4xN = flat.reshape(4, -1)
    print(f"  reshape(4, -1):\n{as_4xN}")
    print()


# ── Section 7: Speed Preview ──────────────────────────────────────────────────

def section_speed_preview():
    print("─" * 55)
    print("SECTION 7: A Preview — Why Arrays Are Faster")
    print("─" * 55)

    n = 2_000_000
    python_list = list(range(n))
    numpy_array = np.arange(n)

    start = time.time()
    result_list = sum(x * x for x in python_list)
    list_time = time.time() - start

    start = time.time()
    result_array = np.sum(numpy_array ** 2)
    array_time = time.time() - start

    print(f"  Python loop : {list_time:.4f} sec   (result: {result_list})")
    print(f"  NumPy array : {array_time:.4f} sec   (result: {result_array})")
    print(f"  NumPy was about {list_time / array_time:.1f}x faster")
    print()


# ── Section 8: Common Mistakes ────────────────────────────────────────────────

def section_mistakes():
    print("─" * 55)
    print("SECTION 8: Common Mistakes")
    print("─" * 55)

    mixed = np.array([1, 2, "three", 4.0])
    print(f"  Mistake 1 — mixed dtype upcast to: {mixed.dtype} ({mixed})")

    vector_1d = np.array([1, 2, 3])
    column_2d = np.array([[1], [2], [3]])
    row_2d = np.array([[1, 2, 3]])
    print(f"  Mistake 2 — shapes: 1D={vector_1d.shape}  column={column_2d.shape}  row={row_2d.shape}")

    flat = np.array([1, 2, 3, 4, 5, 6])
    try:
        flat.reshape(3, 3)
    except ValueError as e:
        print(f"  Mistake 3 — {e}")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 04 LESSON 01 — The ndarray")
    print("=" * 55)
    print()

    section_first_array()
    section_lists_vs_arrays()
    grades = section_higher_dimensions()
    section_inspect_properties(grades)
    section_dtype_control()
    section_reshaping()
    section_speed_preview()
    section_mistakes()

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
