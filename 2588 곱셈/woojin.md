## 2588번 곱셈

### 곱셈 

문제 출처 : https://www.acmicpc.net/problem/2588

## 내가 푼 코드

```
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BJ_2588 {
    
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int firstNum = Integer.parseInt(br.readLine());
        int secondNum = Integer.parseInt(br.readLine());
        int total = 0;
        int count = 0;
        while(true){
            int result = firstNum * (secondNum % 10);
            System.out.println(result);
            count++;
            for (int i = 1; i < count; i++) {
                result *= 10;
            }
            total += result;
            secondNum /= 10;
            if(secondNum == 0)
                break;
        }
        System.out.println(total);
        
        br.close();
    }
}
```

## 생각한 방향

1. 두 번째로 주어진 숫자의 각 자리 수를 구해 첫 번째 수와 곱한 결과를 출력.
2. (3),(4),(5)는 곱셈된 숫자만 구하면 되지만, 총합은 거기에 각 인자 번호 만큼 10을 곱해주어야 재대로 나옴