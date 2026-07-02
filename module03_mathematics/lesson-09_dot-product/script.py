"""
Dot Product and Its Applications
Module 03, Lesson 09

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""

import math


# ── Core Functions ────────────────────────────────────────────────────────────

def dot_product(a, b):
    """Compute the dot product of two same-length vectors."""
    if len(a) != len(b):
        raise ValueError(f"Cannot dot vectors of different dimensions: {len(a)} vs {len(b)}")
    return sum(ai * bi for ai, bi in zip(a, b))

def magnitude(v):
    """Euclidean length of a vector, built directly from the dot product."""
    return math.sqrt(dot_product(v, v))

def angle_between(a, b):
    """Angle (in degrees) between two vectors, using the dot product formula."""
    cos_theta = dot_product(a, b) / (magnitude(a) * magnitude(b))
    cos_theta = max(-1.0, min(1.0, cos_theta))
    return math.degrees(math.acos(cos_theta))

def is_orthogonal(a, b, tol=1e-9):
    """True if a and b are perpendicular (dot product is ~0)."""
    return abs(dot_product(a, b)) < tol

def cosine_similarity(a, b):
    """Cosine of the angle between a and b -- direction similarity, ignoring scale."""
    mag_a, mag_b = magnitude(a), magnitude(b)
    if mag_a == 0 or mag_b == 0:
        raise ValueError("Cosine similarity is undefined when a vector has zero magnitude")
    return dot_product(a, b) / (mag_a * mag_b)

def word_count_vector(text, vocabulary):
    """Turn text into a vector of word counts, one count per vocabulary word."""
    words = text.lower().split()
    return [words.count(w) for w in vocabulary]

def predict(weights, bias, features):
    """A linear model's prediction: dot(weights, features) + bias."""
    return dot_product(weights, features) + bias

def perceptron_predict(weights, bias, features):
    """A simplified binary classifier: 1 if the linear score is positive, else 0."""
    return 1 if predict(weights, bias, features) > 0 else 0


# ── Section 1/2: Dot Product and Magnitude ───────────────────────────────────

def section_dot_product_basics():
    print("─" * 55)
    print("SECTION 1-2: Dot Product and Magnitude")
    print("─" * 55)

    a, b = [1, 2, 3], [4, 5, 6]
    print(f"  dot_product(a, b) = {dot_product(a, b)}")

    v = [3, 4]
    print(f"  magnitude([3,4]) via dot product = {magnitude(v)}")
    print()


# ── Section 3/4: Angle and Orthogonality ─────────────────────────────────────

def section_angle_orthogonal():
    print("─" * 55)
    print("SECTION 3-4: Angle and Orthogonal Vectors")
    print("─" * 55)

    east, northeast, north = [1, 0], [1, 1], [0, 1]
    print(f"  angle(east, northeast) = {angle_between(east, northeast):.1f} deg")
    print(f"  angle(east, north)     = {angle_between(east, north):.1f} deg")

    print(f"  is_orthogonal([1,0],[0,1]) = {is_orthogonal([1, 0], [0, 1])}")
    print()


# ── Section 5: Cosine Similarity ──────────────────────────────────────────────

def section_cosine_similarity():
    print("─" * 55)
    print("SECTION 5: Cosine Similarity")
    print("─" * 55)

    alice = [5, 4, 1, 5]
    bob = [1, 1, 0, 1]
    print(f"  raw dot product   : {dot_product(alice, bob)}")
    print(f"  cosine similarity : {cosine_similarity(alice, bob):.4f}")
    print()


# ── Section 6: Document Similarity ───────────────────────────────────────────

def section_document_similarity():
    print("─" * 55)
    print("SECTION 6: Applied — Document Similarity")
    print("─" * 55)

    doc1 = "the cat sat on the mat"
    doc2 = "the dog sat on the rug"
    doc3 = "quantum physics explains subatomic particle behavior"
    vocabulary = sorted(set(doc1.split()) | set(doc2.split()) | set(doc3.split()))

    v1 = word_count_vector(doc1, vocabulary)
    v2 = word_count_vector(doc2, vocabulary)
    v3 = word_count_vector(doc3, vocabulary)

    print(f"  similarity(doc1, doc2) = {cosine_similarity(v1, v2):.4f}")
    print(f"  similarity(doc1, doc3) = {cosine_similarity(v1, v3):.4f}")
    print()


# ── Section 7: Linear Model Prediction ───────────────────────────────────────

def section_linear_prediction():
    print("─" * 55)
    print("SECTION 7: The Dot Product as a Linear Model")
    print("─" * 55)

    weights = [45.0, 12.0, -1.5]
    bias = 20.0
    house_a = [18, 3, 10]
    house_b = [12, 2, 25]

    print(f"  Predicted price A: {predict(weights, bias, house_a):.1f}")
    print(f"  Predicted price B: {predict(weights, bias, house_b):.1f}")
    print()


# ── Section 8: Verification ──────────────────────────────────────────────────

def section_verification():
    print("─" * 55)
    print("SECTION 8: Verification")
    print("─" * 55)

    v = [3, 4, 12]
    print(f"  magnitude via dot={math.sqrt(dot_product(v, v)):.6f}  "
          f"via math.hypot={math.hypot(*v):.6f}")

    a, b = [3, 1], [1, 2]
    theta = angle_between(a, b)
    print(f"  cos(angle)={math.cos(math.radians(theta)):.4f}  "
          f"cosine_similarity={cosine_similarity(a, b):.4f}")
    print()


# ── Section 9: Common Mistakes ────────────────────────────────────────────────

def section_mistakes():
    print("─" * 55)
    print("SECTION 9: Common Mistakes")
    print("─" * 55)

    a, b = [1, 2, 3], [4, 5, 6]
    elementwise = [ai * bi for ai, bi in zip(a, b)]
    print(f"  Mistake 1 — elementwise={elementwise} (vector) vs dot={dot_product(a, b)} (scalar)")

    try:
        dot_product([1, 2, 3], [1, 2])
    except ValueError as e:
        print(f"  Mistake 2 — {e}")

    short_review, long_review = [1, 1, 0], [5, 5, 0]
    print(f"  Mistake 3 — raw dot={dot_product(short_review, long_review)} vs "
          f"cosine={cosine_similarity(short_review, long_review):.4f}")

    opp_a, opp_b = [1, 2, 3], [-1, -2, -3]
    print(f"  Mistake 4 — cosine similarity can be negative: "
          f"{cosine_similarity(opp_a, opp_b):.4f}")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 03 LESSON 09 — Dot Product and Its Applications")
    print("=" * 55)
    print()

    section_dot_product_basics()
    section_angle_orthogonal()
    section_cosine_similarity()
    section_document_similarity()
    section_linear_prediction()
    section_verification()
    section_mistakes()

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
