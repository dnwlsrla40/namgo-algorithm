package main;

import javax.script.ScriptContext;
import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        // 스캐너 부분에 N장의 카드를 cardNum , 숫자 M 을 max 로 선언
        Scanner sc = new Scanner(System.in);
        int cardNum = sc.nextInt();
        int max = sc.nextInt();
        // 3수의 합
        int plus = 0;
        // 근사치 (max 가장 가까운 수)
        int prac = 0;
        // 반복문으로 처음애 N에서 선언한 숫자만큼 숫자를 집어넣을 수 있게 만든다
        // new int [cardNum] = [] 안에 int 값을 cardNum 개 담을 수 있는 공간을 새롭게 만들어라
        int [] arr = new int[cardNum];
        for (int i = 0; i < cardNum; i++) {
            arr[i]=sc.nextInt();
        }
        //세 중첩 for 문을 통해 전체의 경우의 수 탐지
        //N만큼 반복(배열 arr 를 순회) 첫 번째 부터 cardNum 보다 i가 작을때까지
        for(int i = 0; i<cardNum; i++) {
            //i+1번째 위치한 arr 부터 순회 두 번째 부터 cardNum 보다 j가 작을때까지
        for(int j = i+1; j<cardNum; j++) {
            //j+1번째부터 arr 순회  끝까지 cardNum 보다 k가 작을때까지
        for(int k = j+1; k<cardNum; k++) {
            //세 수를 더한다.
            plus = arr[i] + arr[j] + arr[k];
            //근사치 보다 크고 세수의 합보다 작거나 같으면 새로운 근사치
            if(prac < plus && plus <= max)
                prac = plus;
                }
            }
        }
        //for 문을 다 돌고 가장 근접한 근사치는 prac 에 있다.
        System.out.println(prac);

    }
}






