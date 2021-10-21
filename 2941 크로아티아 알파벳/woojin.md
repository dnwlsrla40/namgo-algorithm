## 2941번 크로아티아 알파벳

### 크로아티아 알파벳

문제 출처 : https://www.acmicpc.net/problem/2941

## 내가 푼 코드

```
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BJ_2941 {
    
    public static void main (String[] args) throws IOException {
        String[] croatia = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();

        int count = 0;
        for (int i = 0; i < croatia.length; i++) {
            while(input.contains(croatia[i])){ // input에 c=이 포함되어 있다면 반복
                input = input.replaceFirst(croatia[i],"*"); // c= -> c= 바꿔라 input = c=c=
                count++;                                                      // count = 1
            }
        }
        input = input.replace("*", "");
        if(input != ""){
            for (int i = 0; i < input.length(); i++) {
                count++;
            }
        }
        System.out.println(count);
        br.close();
    }
}
```

```
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BJ_2941 {
    
    public static void main (String[] args) throws IOException {
        String[] croatia = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // python  -> input()
        String input = br.readLine();

        int count = 0;
        
        for (String s : croatia) {
            if(input.contains(s))
                input = input.replace(s, "*");
        }
        count = input.length();
        System.out.println(count);
        br.close();
    }
}
```

## 생각한 방향

1. String 배열을 만들어서 입력값에 해당 크로아티아 문자가 포함되어 있는 지 검사 포함되어 있다면 그 문자를 없애고 갯수 증가
2. 2번째 코드는 다시 생각해서 더 깔끔하게 짠 코드 방식은 같음