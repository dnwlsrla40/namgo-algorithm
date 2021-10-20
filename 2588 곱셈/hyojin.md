## 2588번 곱셈
### 곱셈
문제 출처 : https://www.acmicpc.net/problem/2588

## 내가 푼 코드

```
A = 473
B = 385


def add(A, B):
    for i in range(int(len(str(B))), 0, -1):
        B_ = str(B)[i - 1]
        print(A * int(B_))
    print(A * B)


add(A, B)

```

## 생각한 방향
1. 두 번째로 주어진 숫자의 각 자리 수를 구해 첫 번째 수와 곱한 결과를 출력.
