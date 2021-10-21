## 2941번 크로아티아 알파벳

### 크로아티아 알파벳

문제 출처 : https://www.acmicpc.net/problem/2941

## 내가 푼 코드

```
# 1.첫번째 줄에 단어가 주어진다
c = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# 2.주어진 단어
w = input()
#  3.alphabet 이라는 변수 안에 차례대로 c를 넣어준다 print alphabet 을 하면 c= c- dz= ... 들이 나옴
for alphabet in c:
    # print(alphabet)
    # 4.주어진 단어에 alphabet 을 C에 속한 리스트 값으로 바꾼다 replace = 문자를 변경
    w = w.replace(alphabet, 'c')
    #  5. len 함수는 C 원소의 개수를 센다
print(len(w))

```




## 생각한 방향

1. 배열을 만들고 반복문을 통해 확인하고 replace 함수로 문자를 변경하고 len으로 개수를 적는다 라고 생각했다
