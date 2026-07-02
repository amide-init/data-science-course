"""
Basic Probability
Module 03, Lesson 04

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""

import random


# ── Core Functions ────────────────────────────────────────────────────────────

def probability(favorable, sample_space):
    """Classical probability: favorable outcomes / total outcomes."""
    return len(favorable) / len(sample_space)

def flip_coin():
    return random.choice(["H", "T"])

def experimental_probability(n_flips):
    """Simulate n_flips coin tosses and return the proportion of heads."""
    flips = [flip_coin() for _ in range(n_flips)]
    return flips.count("H") / n_flips

def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):
    """
    Compute P(A | B) given P(A), P(B|A), and P(B|not A).
    Returns P(A|B).
    """
    p_not_a = 1 - p_a
    p_b = (p_b_given_a * p_a) + (p_b_given_not_a * p_not_a)
    return (p_b_given_a * p_a) / p_b


DECK_RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
DECK_SUITS = ["Hearts","Diamonds","Clubs","Spades"]

def build_deck():
    return [(r, s) for s in DECK_SUITS for r in DECK_RANKS]


# ── Section 1: What Is Probability? ──────────────────────────────────────────

def section_probability_basics():
    print("─" * 55)
    print("SECTION 1: What Is Probability?")
    print("─" * 55)

    sample_space = [1, 2, 3, 4, 5, 6]
    p_four = probability([4], sample_space)
    evens = [x for x in sample_space if x % 2 == 0]
    p_even = probability(evens, sample_space)
    gt_four = [x for x in sample_space if x > 4]
    p_gt_four = probability(gt_four, sample_space)

    print(f"  P(rolling a 4)   : {p_four:.3f}")
    print(f"  P(rolling even)  : {p_even:.3f}")
    print(f"  P(rolling > 4)   : {p_gt_four:.3f}")
    print()


# ── Section 2: Compound Sample Spaces ────────────────────────────────────────

def section_compound_events():
    print("─" * 55)
    print("SECTION 2: Sample Space and Events")
    print("─" * 55)

    two_dice_space = [(d1, d2) for d1 in range(1, 7) for d2 in range(1, 7)]
    sum_to_7 = [(d1, d2) for d1, d2 in two_dice_space if d1 + d2 == 7]
    doubles = [(d1, d2) for d1, d2 in two_dice_space if d1 == d2]

    print(f"  P(sum == 7) : {probability(sum_to_7, two_dice_space):.3f}")
    print(f"  P(double)   : {probability(doubles, two_dice_space):.3f}")
    print()


# ── Section 3: Theoretical vs Experimental Probability ───────────────────────

def section_law_of_large_numbers():
    print("─" * 55)
    print("SECTION 3: Theoretical vs Experimental Probability")
    print("─" * 55)

    random.seed(42)
    for n in [10, 100, 1000, 10000, 100000]:
        p_exp = experimental_probability(n)
        print(f"  n={n:>7}  P(Heads)={p_exp:.4f}  (theoretical=0.5000)")
    print()


# ── Section 4: Addition Rule ──────────────────────────────────────────────────

def section_addition_rule():
    print("─" * 55)
    print("SECTION 4: The Addition Rule")
    print("─" * 55)

    deck = build_deck()
    kings = [c for c in deck if c[0] == "K"]
    hearts = [c for c in deck if c[1] == "Hearts"]
    king_of_hearts = [c for c in deck if c[0] == "K" and c[1] == "Hearts"]

    p_king = probability(kings, deck)
    p_heart = probability(hearts, deck)
    p_king_and_heart = probability(king_of_hearts, deck)
    p_king_or_heart = p_king + p_heart - p_king_and_heart

    print(f"  P(King OR Heart) = {p_king:.4f} + {p_heart:.4f} - {p_king_and_heart:.4f} = {p_king_or_heart:.4f}")

    queens = [c for c in deck if c[0] == "Q"]
    p_queen = probability(queens, deck)
    print(f"  P(King OR Queen) (mutually exclusive) = {p_king + p_queen:.4f}")
    print()


# ── Section 5: Multiplication Rule ────────────────────────────────────────────

def section_multiplication_rule():
    print("─" * 55)
    print("SECTION 5: The Multiplication Rule")
    print("─" * 55)

    p_heads = 0.5
    p_six = 1 / 6
    print(f"  P(heads, then heads)    : {p_heads * p_heads:.4f}")
    print(f"  P(6, then 6)            : {p_six * p_six:.4f}")
    print()


# ── Section 6: Independent vs Dependent Events ───────────────────────────────

def section_independent_vs_dependent():
    print("─" * 55)
    print("SECTION 6: Independent vs Dependent Events")
    print("─" * 55)

    p_indep = (4 / 52) * (4 / 52)
    p_dep = (4 / 52) * (3 / 51)
    print(f"  WITH replacement (independent)   : {p_indep:.4f}")
    print(f"  WITHOUT replacement (dependent)  : {p_dep:.4f}")
    print()


# ── Section 7: Conditional Probability ───────────────────────────────────────

def section_conditional_probability():
    print("─" * 55)
    print("SECTION 7: Conditional Probability")
    print("─" * 55)

    total_students, studied_and_passed, studied, passed = 100, 42, 50, 60
    p_studied = studied / total_students
    p_studied_and_passed = studied_and_passed / total_students
    p_passed_given_studied = p_studied_and_passed / p_studied

    print(f"  P(Passed)             : {passed/total_students:.2f}")
    print(f"  P(Passed | Studied)   : {p_passed_given_studied:.2f}")
    print()


# ── Section 8/9: Bayes' Theorem + Simulation ─────────────────────────────────

def section_bayes():
    print("─" * 55)
    print("SECTION 8-9: Bayes' Theorem + Simulation")
    print("─" * 55)

    p_disease = 0.01
    p_positive_given_disease = 0.95
    p_positive_given_no_disease = 0.05

    p_disease_given_positive = bayes_theorem(
        p_disease, p_positive_given_disease, p_positive_given_no_disease
    )
    print(f"  P(Disease | Positive test) = {p_disease_given_positive:.4f}")

    random.seed(1)
    n_people = 200_000
    infected_and_positive = 0
    total_positive = 0
    for _ in range(n_people):
        has_disease = random.random() < p_disease
        if has_disease:
            tested_positive = random.random() < p_positive_given_disease
        else:
            tested_positive = random.random() < p_positive_given_no_disease
        if tested_positive:
            total_positive += 1
            if has_disease:
                infected_and_positive += 1

    simulated = infected_and_positive / total_positive
    print(f"  Monte Carlo simulation     = {simulated:.4f}")
    print()


# ── Section 10: Common Mistakes ───────────────────────────────────────────────

def section_mistakes():
    print("─" * 55)
    print("SECTION 10: Common Mistakes")
    print("─" * 55)

    print("  Mistake 1 — P(A|B) != P(B|A): 95% test accuracy != 95% disease chance")

    deck = build_deck()
    kings = [c for c in deck if c[0] == "K"]
    hearts = [c for c in deck if c[1] == "Hearts"]
    wrong = len(kings) / 52 + len(hearts) / 52
    correct = wrong - (1 / 52)
    print(f"  Mistake 2 — double counting: wrong={wrong:.4f} vs correct={correct:.4f}")

    p_wrong = (4 / 52) * (4 / 52)
    p_correct = (4 / 52) * (3 / 51)
    print(f"  Mistake 3 — wrong independence assumption: {p_wrong:.4f} vs {p_correct:.4f}")

    random.seed(7)
    small_sample = [flip_coin() for _ in range(10)]
    p_small = small_sample.count("H") / 10
    print(f"  Mistake 4 — small sample noise: P(Heads) from 10 flips = {p_small:.2f}")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 03 LESSON 04 — Basic Probability")
    print("=" * 55)
    print()

    section_probability_basics()
    section_compound_events()
    section_law_of_large_numbers()
    section_addition_rule()
    section_multiplication_rule()
    section_independent_vs_dependent()
    section_conditional_probability()
    section_bayes()
    section_mistakes()

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
