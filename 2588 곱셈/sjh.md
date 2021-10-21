## 2588번 곱셈

### 곱셈 

문제 출처 : https://www.acmicpc.net/problem/2588

## 내가 푼 코드

```python
n1 = input()
n2 = input()

ans1 = int(n1)*int(n2[2])
ans2 = int(n1)*int(n2[1])
ans3 = int(n1)*int(n2[0])
ans4 = ans1+ans2*10+ans3*100

print(ans1)
print(ans2)
print(ans3)
print(ans4)
```

## 생각한 방향

1. 두번째 인자로 받은 숫자의 각 자리수에 접근해서 곱하는 방식으로 진행 하였다.
2. 그렇게 구한 수의 합을 구해야 할 때는 자리수가 서로 다르므로 각 숫자의 상황에 맞게 자리수를 곱해서 더해주었다.
