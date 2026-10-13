# 문자열 검색 알고리즘 3종의 성능 비교

- 이름: LIU TINGYANG
- 학번: 2026193138
- 과목: 고급알고리즘 개인 프로젝트

## 연구 목표
Naive Search, KMP, Rabin–Karp 알고리즘의 문자열 검색 정확성과 실행 시간을 비교한다.

## 프로젝트 구조
- `src/algorithms.py`: 세 가지 문자열 검색 알고리즘
- `tests/test_algorithms.py`: 예제 및 재현 가능한 무작위 테스트
- `benchmark.py`: 입력 유형 및 크기별 실행 시간 측정
- `results/benchmark.csv`: 실험 실행 후 생성되는 결과

## 실행 방법
Python 3.10 이상, 추가 패키지 불필요.

```bash
python -m unittest discover -s tests -v
python benchmark.py
```

실험은 무작위 문자열, 반복 문자열, 빈번한 일치 문자열을 대상으로 수행한다. 실행 시간은 `perf_counter_ns()`로 7회 측정한 중앙값(ms)이다. 결과는 실행 환경에 따라 달라진다.

## 이론적 시간 복잡도
| 알고리즘 | 일반적인 검색 시간 | 최악의 경우 |
|---|---|---|
| Naive | O(nm) | O(nm) |
| KMP | O(n+m) | O(n+m) |
| Rabin–Karp | 기대 O(n+m) | O(nm) |

여기서 n은 텍스트 길이, m은 패턴 길이이다. Rabin–Karp는 해시 충돌 시 실제 문자열 비교를 수행해 정확성을 보장한다.

## AI 활용 및 검증
AI를 활용하여 알고리즘의 동작 원리, KMP의 LPS 배열, 롤링 해시 및 실험 설계를 학습하고 초안 코드를 작성했다. 이후 예제와 무작위 테스트로 결과를 검증하도록 구성했다. 실제 실험 결과는 본인 환경에서 다시 실행하고 분석해야 한다.
