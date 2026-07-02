"""
Random Variables and Distributions
Module 03, Lesson 05

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""

import itertools
import math
import random
from collections import Counter


# ── Core Functions ────────────────────────────────────────────────────────────

def expected_value(pmf):
    """Compute E[X] given a PMF dict {value: probability}."""
    return sum(x * p for x, p in pmf.items())

def variance_rv(pmf):
    """Compute Var(X) given a PMF dict {value: probability}."""
    mu = expected_value(pmf)
    return sum((x - mu) ** 2 * p for x, p in pmf.items())

def bernoulli_pmf(p):
    """PMF for a single Bernoulli(p) trial."""
    return {0: 1 - p, 1: p}

def binomial_pmf(n, p, k):
    """P(X = k) for X ~ Binomial(n, p)."""
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

def binomial_distribution(n, p):
    """Full PMF dict for X ~ Binomial(n, p), for k = 0..n."""
    return {k: binomial_pmf(n, p, k) for k in range(n + 1)}

def simulate_binomial(n, p, trials=100_000):
    """Simulate `trials` repeats of n Bernoulli(p) trials, return experimental PMF."""
    results = []
    for _ in range(trials):
        successes = sum(1 for _ in range(n) if random.random() < p)
        results.append(successes)
    counts = Counter(results)
    return {k: count / trials for k, count in sorted(counts.items())}

def normal_like_density(x, mean=170, std=7):
    """A bell-curve-shaped density function (preview of Lesson 06)."""
    coeff = 1 / (std * math.sqrt(2 * math.pi))
    exponent = -((x - mean) ** 2) / (2 * std ** 2)
    return coeff * math.exp(exponent)


# ── Section 1/2: Random Variables ────────────────────────────────────────────

def section_random_variables():
    print("─" * 55)
    print("SECTION 1-2: What Is a Random Variable?")
    print("─" * 55)

    dice_outcomes = list(itertools.product(range(1, 7), range(1, 7)))
    X_dice = [d1 + d2 for d1, d2 in dice_outcomes]

    coin_outcomes = list(itertools.product(["H", "T"], repeat=3))
    Y_heads = [outcome.count("H") for outcome in coin_outcomes]

    print(f"  X = sum of two dice, first 5 values : {X_dice[:5]}")
    print(f"  Y = number of heads in 3 flips      : {Y_heads}")
    print()


# ── Section 3: PMF ────────────────────────────────────────────────────────────

def section_pmf():
    print("─" * 55)
    print("SECTION 3: The Probability Mass Function")
    print("─" * 55)

    coin_outcomes = list(itertools.product(["H", "T"], repeat=3))
    Y_heads = [outcome.count("H") for outcome in coin_outcomes]
    counts = Counter(Y_heads)
    total = len(Y_heads)
    pmf = {y: count / total for y, count in sorted(counts.items())}

    print(f"  PMF: {pmf}")
    print(f"  Sum: {sum(pmf.values()):.4f}")
    print()
    return pmf


# ── Section 4/5: Expected Value and Variance ─────────────────────────────────

def section_expectation_variance(pmf):
    print("─" * 55)
    print("SECTION 4-5: Expected Value and Variance")
    print("─" * 55)

    e_y = expected_value(pmf)
    var_y = variance_rv(pmf)
    std_y = math.sqrt(var_y)

    print(f"  E[Y]       : {e_y:.3f}")
    print(f"  Var(Y)     : {var_y:.3f}")
    print(f"  Std dev(Y) : {std_y:.3f}")
    print()


# ── Section 6: Bernoulli ──────────────────────────────────────────────────────

def section_bernoulli():
    print("─" * 55)
    print("SECTION 6: The Bernoulli Distribution")
    print("─" * 55)

    p_click = 0.12
    pmf_click = bernoulli_pmf(p_click)
    print(f"  Bernoulli(p={p_click}): E[X]={expected_value(pmf_click):.3f}  "
          f"Var(X)={variance_rv(pmf_click):.4f}")
    print()


# ── Section 7/8: Binomial + Simulation ───────────────────────────────────────

def section_binomial():
    print("─" * 55)
    print("SECTION 7-8: Binomial Distribution + Simulation")
    print("─" * 55)

    n_emails, p_spam = 10, 0.20
    pmf_spam = binomial_distribution(n_emails, p_spam)
    print(f"  X ~ Binomial(n={n_emails}, p={p_spam})")
    for k, p in pmf_spam.items():
        print(f"    P(X={k}) = {p:.4f}")
    print(f"  E[X] = n*p = {n_emails * p_spam:.1f}")

    random.seed(3)
    simulated_pmf = simulate_binomial(n_emails, p_spam)
    print()
    print(f"  {'k':>3} {'Theoretical':>12} {'Simulated':>12}")
    for k in range(n_emails + 1):
        print(f"  {k:>3} {pmf_spam.get(k, 0):>12.4f} {simulated_pmf.get(k, 0):>12.4f}")
    print()
    return pmf_spam, n_emails, p_spam


# ── Section 9: Continuous Random Variables ───────────────────────────────────

def section_continuous():
    print("─" * 55)
    print("SECTION 9: A First Look at Continuous Random Variables")
    print("─" * 55)

    bin_width = 0.01
    n_bins = int((172 - 168) / bin_width)
    heights = [168 + i * bin_width for i in range(n_bins)]
    area = sum(normal_like_density(h) * bin_width for h in heights)

    print(f"  P(168 <= height <= 172) approx {area:.4f}")
    print("  A single exact value has ~0 probability in a continuous distribution.")
    print()


# ── Section 10: Verification ─────────────────────────────────────────────────

def section_verification(pmf_spam, n_emails, p_spam):
    print("─" * 55)
    print("SECTION 10: Built-in Verification")
    print("─" * 55)

    e_ours = expected_value(pmf_spam)
    var_ours = variance_rv(pmf_spam)
    e_formula = n_emails * p_spam
    var_formula = n_emails * p_spam * (1 - p_spam)

    print(f"  E[X]   ours={e_ours:.4f}  formula={e_formula:.4f}  "
          f"match={abs(e_ours - e_formula) < 1e-9}")
    print(f"  Var(X) ours={var_ours:.4f}  formula={var_formula:.4f}  "
          f"match={abs(var_ours - var_formula) < 1e-9}")
    print()


# ── Section 11: Common Mistakes ───────────────────────────────────────────────

def section_mistakes():
    print("─" * 55)
    print("SECTION 11: Common Mistakes")
    print("─" * 55)

    print("  Mistake 1 — 'P(X)' is meaningless; use 'P(X = x)'")

    buggy_pmf = {0: 0.5, 1: 0.3}
    print(f"  Mistake 2 — PMF sum should be 1.0, got {sum(buggy_pmf.values()):.2f}")

    wrong_binomial_p = binomial_pmf(2, 4 / 52, 2)
    correct_p = (4 / 52) * (3 / 51)
    print(f"  Mistake 3 — Binomial (wrong, assumes replacement)={wrong_binomial_p:.4f} "
          f"vs correct (no replacement)={correct_p:.4f}")

    density_at_peak = normal_like_density(170, mean=170, std=2)
    print(f"  Mistake 4 — density value {density_at_peak:.4f} is NOT a probability")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 03 LESSON 05 — Random Variables & Distributions")
    print("=" * 55)
    print()

    section_random_variables()
    pmf = section_pmf()
    section_expectation_variance(pmf)
    section_bernoulli()
    pmf_spam, n_emails, p_spam = section_binomial()
    section_continuous()
    section_verification(pmf_spam, n_emails, p_spam)
    section_mistakes()

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
