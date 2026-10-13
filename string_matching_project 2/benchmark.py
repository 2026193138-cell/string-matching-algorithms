"""Reproducible timings. Run from project root: python benchmark.py"""
import csv
import random
import statistics
import time
from pathlib import Path
from src.algorithms import naive, kmp, rabin_karp

ALGORITHMS = {'Naive': naive, 'KMP': kmp, 'Rabin-Karp': rabin_karp}
SIZES = [1000, 5000, 10000, 50000]
REPEATS = 7

def inputs(n, case):
    if case == 'random':
        rng = random.Random(2026 + n)
        return ''.join(rng.choices('abcd', k=n)), 'abcaabca'
    if case == 'repetitive':
        return 'a' * n, 'a' * 15 + 'b'
    if case == 'frequent_matches':
        return 'ab' * (n // 2), 'abab'
    raise ValueError(case)

def main():
    rows = []
    for case in ('random', 'repetitive', 'frequent_matches'):
        for n in SIZES:
            text, pattern = inputs(n, case)
            expected = naive(text, pattern)
            for name, algorithm in ALGORITHMS.items():
                assert algorithm(text, pattern) == expected, (case, n, name)
                measurements = []
                for _ in range(REPEATS):
                    start = time.perf_counter_ns()
                    algorithm(text, pattern)
                    measurements.append((time.perf_counter_ns() - start) / 1_000_000)
                rows.append({'case': case, 'text_length': n, 'pattern_length': len(pattern), 'algorithm': name, 'median_ms': round(statistics.median(measurements), 5), 'matches': len(expected)})
    Path('results').mkdir(exist_ok=True)
    with open('results/benchmark.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print('Saved results/benchmark.csv (timings depend on your computer)')

if __name__ == '__main__':
    main()
