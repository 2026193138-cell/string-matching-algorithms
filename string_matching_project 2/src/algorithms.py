"""Return every starting index of pattern in text."""

def naive(text: str, pattern: str) -> list[int]:
    if not pattern:
        return list(range(len(text) + 1))
    m = len(pattern)
    return [i for i in range(len(text) - m + 1) if text[i:i+m] == pattern]


def kmp(text: str, pattern: str) -> list[int]:
    if not pattern:
        return list(range(len(text) + 1))
    m = len(pattern)
    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j and pattern[i] != pattern[j]:
            j = lps[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    result = []
    j = 0
    for i, char in enumerate(text):
        while j and char != pattern[j]:
            j = lps[j-1]
        if char == pattern[j]:
            j += 1
        if j == m:
            result.append(i-m+1)
            j = lps[j-1]
    return result


def rabin_karp(text: str, pattern: str) -> list[int]:
    if not pattern:
        return list(range(len(text) + 1))
    n, m = len(text), len(pattern)
    if m > n:
        return []
    base, mod = 257, 1_000_000_007
    highest = pow(base, m-1, mod)
    ph = th = 0
    for i in range(m):
        ph = (ph*base + ord(pattern[i])) % mod
        th = (th*base + ord(text[i])) % mod
    result = []
    for i in range(n-m+1):
        if ph == th and text[i:i+m] == pattern:
            result.append(i)
        if i < n-m:
            th = ((th - ord(text[i])*highest)*base + ord(text[i+m])) % mod
    return result
