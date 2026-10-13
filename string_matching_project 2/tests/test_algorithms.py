import random
import unittest
from src.algorithms import naive, kmp, rabin_karp

class AlgorithmTests(unittest.TestCase):
    def test_examples(self):
        cases = [('banana', 'ana', [1,3]), ('aaaa', 'aa', [0,1,2]), ('abc', 'd', []), ('', '', [0]), ('abc', '', [0,1,2,3]), ('abc', 'abcd', []), ('가나다가나', '가나', [0,3])]
        for text, pattern, expected in cases:
            for algorithm in (naive, kmp, rabin_karp):
                with self.subTest(algorithm=algorithm.__name__, text=text, pattern=pattern):
                    self.assertEqual(algorithm(text, pattern), expected)

    def test_random(self):
        rng = random.Random(2026)
        for _ in range(500):
            text = ''.join(rng.choices('abc', k=rng.randrange(60)))
            pattern = ''.join(rng.choices('abc', k=rng.randrange(12)))
            expected = naive(text, pattern)
            self.assertEqual(kmp(text, pattern), expected)
            self.assertEqual(rabin_karp(text, pattern), expected)

if __name__ == '__main__':
    unittest.main()
