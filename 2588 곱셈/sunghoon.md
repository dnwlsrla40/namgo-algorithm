## 2588번 곱셈

### 곱셈 

문제 출처 : https://www.acmicpc.net/problem/2588

## 내가 푼 코드

```
num1 = int(())
num2 = int(())

print(num1 * (num2%10))
print(num1 * ((num2%100)//10))
print(num1 * (num2//100))
print(num1 * num2)


```

## 생각한 방향

1. 파이썬 연산자를 이용하여 %로 몫이 아닌 나머지를 구해서 곱하고 //로 소수점을 버리고 정수부분만 곱해서 하나하나 나타냄

## 염려되는 부분
1. 숫자가 커지거나 바뀔경우 문제가 생길것으로 예상됨
