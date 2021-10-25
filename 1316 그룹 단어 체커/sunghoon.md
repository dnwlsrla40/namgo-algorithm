N = int(input())
count = N
# find = 변수.find(찾을문자)
for _ in range(N):  #_바는 값을 무시 필요하지 않거나 사용되지 않는 값
    word = input()
    for i in range(len(word)-1):
        if word.find(word[i]) > word.find(word[i+1]):
            #  aba    a= index[0]   b= index[1]    a=index[2]
            # heh e = index 1 h= index 0  우 heh.find(heh[2]) 인 경  0이 나오고 .find(heh[1]) 은 1이 나와서 그룹단어 x
            count = count - 1
            break
print(count)
  #a find index 가 뒤에있는 b find index 보다 크면 이건 그룹단어 아니다


