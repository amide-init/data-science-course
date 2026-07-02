"""
The Normal Distribution
Module 03, Lesson 06

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""

import math
import random
from statistics import NormalDist


# ── Core Functions ────────────────────────────────────────────────────────────

def normal_pdf(x, mu, sigma):
    """Normal probability density function at point x."""
    coeff = 1 / (sigma * math.sqrt(2 * math.pi))
    exponent = -((x - mu) ** 2) / (2 * sigma ** 2)
    return coeff * math.exp(exponent)

def cdf_numeric(x, mu, sigma, dx=0.001):
    """Approximate P(X <= x) by summing pdf * dx from far left up to x."""
    lo = mu - 8 * sigma
    total = 0.0
    point = lo
    while point < x:
        total += normal_pdf(point, mu, sigma) * dx
        point += dx
    return total

def cdf_exact(x, mu, sigma):
    """Exact P(X <= x) using the error function."""
    return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))

def inverse_cdf(p, mu, sigma, tol=1e-6):
    """Binary search for the x where cdf_exact(x, mu, sigma) == p."""
    lo, hi = mu - 10 * sigma, mu + 10 * sigma
    while hi - lo > tol:
        mid = (lo + hi) / 2
        if cdf_exact(mid, mu, sigma) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

def mean(data):
    return sum(data) / len(data)

def std_dev(data):
    m = mean(data)
    return math.sqrt(sum((x - m) ** 2 for x in data) / (len(data) - 1))

def median(data):
    s = sorted(data)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2

def skewed_sample():
    """A deliberately NON-normal, right-skewed random variable (values in [0, 1])."""
    return random.random() ** 3

def sample_means(n_trials, sample_size):
    return [mean([skewed_sample() for _ in range(sample_size)]) for _ in range(n_trials)]

def ascii_histogram(data, bins=16, width=40, label=""):
    lo, hi = min(data), max(data)
    bin_width = (hi - lo) / bins
    counts = [0] * bins
    for v in data:
        idx = min(int((v - lo) / bin_width), bins - 1)
        counts[idx] += 1
    max_count = max(counts)
    print(f"  {label}")
    for i, c in enumerate(counts):
        bar_len = int(c / max_count * width) if max_count else 0
        print(f"    {lo + i*bin_width:6.3f} | {'#' * bar_len}")
    print()

def ascii_curve(pdf_func, mu, sigma, width=60, height=12, spread=4):
    """Draw a rough ASCII plot of a PDF curve."""
    lo, hi = mu - spread * sigma, mu + spread * sigma
    xs = [lo + i * (hi - lo) / (width - 1) for i in range(width)]
    ys = [pdf_func(x, mu, sigma) for x in xs]
    y_max = max(ys)
    grid = [[" "] * width for _ in range(height)]
    for col, y in enumerate(ys):
        row = height - 1 - int((y / y_max) * (height - 1))
        grid[row][col] = "*"
    for row in grid:
        print("  |" + "".join(row) + "|")
    print(f"   {lo:.0f}{' '*(width//2 - 6)}mu={mu:.0f}{' '*(width//2 - 6)}{hi:.0f}")


# ── Section 1: PDF and Shape ──────────────────────────────────────────────────

def section_pdf():
    print("─" * 55)
    print("SECTION 1: The Normal PDF")
    print("─" * 55)
    ascii_curve(normal_pdf, mu=70, sigma=10)
    print()


# ── Section 2: Standardization ───────────────────────────────────────────────

def section_standardization():
    print("─" * 55)
    print("SECTION 2: Standardization (z-scores)")
    print("─" * 55)

    priya_score, mu_a, sigma_a = 88, 70, 10
    rohan_score, mu_b, sigma_b = 650, 500, 100
    z_priya = (priya_score - mu_a) / sigma_a
    z_rohan = (rohan_score - mu_b) / sigma_b

    print(f"  Priya z = {z_priya:+.2f}   Rohan z = {z_rohan:+.2f}")
    print()


# ── Section 3: CDF ─────────────────────────────────────────────────────────────

def section_cdf():
    print("─" * 55)
    print("SECTION 3: The CDF")
    print("─" * 55)

    mu, sigma, x = 70, 10, 85
    p_numeric = cdf_numeric(x, mu, sigma)
    p_exact = cdf_exact(x, mu, sigma)
    print(f"  P(X<={x}) numeric={p_numeric:.4f}  exact={p_exact:.4f}")

    p_between = cdf_exact(80, mu, sigma) - cdf_exact(60, mu, sigma)
    print(f"  P(60<=X<=80) = {p_between:.4f}")
    print()


# ── Section 4: Empirical Rule ─────────────────────────────────────────────────

def section_empirical_rule():
    print("─" * 55)
    print("SECTION 4: 68-95-99.7 Rule (Exact)")
    print("─" * 55)

    mu, sigma = 70, 10
    for k in [1, 2, 3]:
        p_within = cdf_exact(mu + k * sigma, mu, sigma) - cdf_exact(mu - k * sigma, mu, sigma)
        print(f"  mu +/- {k}*sigma : {p_within:.4%}")
    print()


# ── Section 5: Stdlib Verification ───────────────────────────────────────────

def section_verification():
    print("─" * 55)
    print("SECTION 5: Verification vs statistics.NormalDist")
    print("─" * 55)

    mu, sigma, x = 70, 10, 85
    nd = NormalDist(mu, sigma)
    print(f"  pdf ours={normal_pdf(x, mu, sigma):.6f}  stdlib={nd.pdf(x):.6f}")
    print(f"  cdf ours={cdf_exact(x, mu, sigma):.6f}  stdlib={nd.cdf(x):.6f}")
    print()


# ── Section 6: Percentiles ────────────────────────────────────────────────────

def section_percentiles():
    print("─" * 55)
    print("SECTION 6: Percentiles via Inverse CDF")
    print("─" * 55)

    mu, sigma = 500, 100
    score_90th = inverse_cdf(0.90, mu, sigma)
    stdlib_90th = NormalDist(mu, sigma).inv_cdf(0.90)
    print(f"  90th percentile: ours={score_90th:.1f}  stdlib={stdlib_90th:.1f}")

    p_above_650 = 1 - cdf_exact(650, mu, sigma)
    print(f"  P(score > 650) = {p_above_650:.4f}")
    print()


# ── Section 7: Central Limit Theorem ─────────────────────────────────────────

def section_clt():
    print("─" * 55)
    print("SECTION 7: The Central Limit Theorem")
    print("─" * 55)

    random.seed(11)
    single_draws = [skewed_sample() for _ in range(5000)]
    ascii_histogram(single_draws, label="Original skewed_sample() — NOT normal")

    means_n2 = sample_means(2000, 2)
    means_n30 = sample_means(2000, 30)
    ascii_histogram(means_n2, label="Sample means (n=2)")
    ascii_histogram(means_n30, label="Sample means (n=30) — looks normal")

    pop_std = std_dev(single_draws)
    print(f"{'n':<6} {'Predicted std':>15} {'Observed std':>15}")
    for n, means in [(2, means_n2), (30, means_n30)]:
        predicted = pop_std / math.sqrt(n)
        observed = std_dev(means)
        print(f"{n:<6} {predicted:>15.4f} {observed:>15.4f}")
    print()


# ── Section 8: Common Mistakes ────────────────────────────────────────────────

def section_mistakes():
    print("─" * 55)
    print("SECTION 8: Common Mistakes")
    print("─" * 55)

    incomes = [25000, 28000, 30000, 32000, 33000, 35000, 36000, 38000,
               40000, 42000, 45000, 50000, 480000]
    print(f"  Mistake 1 — income mean={mean(incomes):,.0f} vs median={median(incomes):,.0f} (skewed!)")

    narrow_density = normal_pdf(70, mu=70, sigma=0.1)
    print(f"  Mistake 2 — normal_pdf can exceed 1: {narrow_density:.4f}")

    mu, sigma, x = 70, 10, 85
    print(f"  Mistake 3 — P(X>x) needs 1-cdf: cdf={cdf_exact(x, mu, sigma):.4f} "
          f"vs 1-cdf={1 - cdf_exact(x, mu, sigma):.4f}")

    a, b = 60, 80
    wrong = cdf_exact(a, mu, sigma) - cdf_exact(b, mu, sigma)
    correct = cdf_exact(b, mu, sigma) - cdf_exact(a, mu, sigma)
    print(f"  Mistake 4 — order matters: wrong={wrong:.4f} vs correct={correct:.4f}")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 03 LESSON 06 — The Normal Distribution")
    print("=" * 55)
    print()

    section_pdf()
    section_standardization()
    section_cdf()
    section_empirical_rule()
    section_verification()
    section_percentiles()
    section_clt()
    section_mistakes()

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
