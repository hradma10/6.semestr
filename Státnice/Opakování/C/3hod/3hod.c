//
// Created by marti on 14.03.2024.
//

#include <stdio.h>

void ukol1(int num) {
    int res = num < 0 ? -num : num;
    printf("%i\n", res);
}

int ukol2(int year) {

    if ((year % 4) == 0) {
        if ((year % 100) == 0) {
            return (year % 400) == 0 ? 1 : 0;
        }
        return 1;
    }
    return 0;
}

int ukol3(char c) {
    if (c >= 65 && c <= 90) printf("Velke\n");
    else if (c >= 97 && c <= 122) printf("Male\n");
    else printf("Chyba\n");

    return 0;
}


void ukol4_switch(int num) {
    switch (num) {
        case 10:
            printf("%i\n", 10);
        case 9:
            printf("%i\n", 9);
        case 8:
            printf("%i\n", 8);
        case 7:
            printf("%i\n", 7);
        case 6:
            printf("%i\n", 6);
        case 5:
            printf("%i\n", 5);
        case 4:
            printf("%i\n", 4);
        case 3:
            printf("%i\n", 3);
        case 2:
            printf("%i\n", 2);
        case 1:
            printf("%i\n", 1);
    }
}

void ukol4_normal(int num) {
    for (int i = num; i > 0; i--) {
        printf("%i\n", i);
    }

}

void ukol5(int a, int b) {
    long long int temp_a;
    printf("Prvnich %i nasobku: ", a);
    for (int i = 1; i <= a; i++) {
        printf("%i, ", i * b);
    }
    printf("\n");

    int vysledek = 1;
    temp_a = a;
    if (a == 0) {
        printf("%i\n", 0);
    } else {
        while (temp_a > 0) {
            vysledek *= b;
            temp_a--;
        }
    }
    printf("%i-ta mocnina: %i\n", a, vysledek);
    printf("\n");

    temp_a = a;
    int pocet_cislic = 0;
    while (1) {
        pocet_cislic++;
        temp_a /= 10;
        if (temp_a == 0) break;
    }
    printf("Pocet cislic: %i\n", pocet_cislic);
    printf("\n");

    temp_a = a;
    int first = 0;
    int second = 1;
    int res = 0;
    if (temp_a == 0) {
        vysledek = first;
    } else if (temp_a == 1) {
        vysledek = second;
    } else {
        while (temp_a > 1) {
            res = first + second;
            first = second;
            second = res;
            temp_a--;
        }
        vysledek = res;
    }
    printf("Fibonacciho cislo: %i\n", vysledek);
    printf("\n");

    vysledek = 0;
    for (int num = a + 1; num < b; num++) {
        vysledek += num;
    }
    printf("Cisla: %i\n", vysledek);
}

void ukol6_1(int n);

void ukol6_2(int n);

void ukol6_3(int n);

int ukol7(int num) {
    int reversedNum = 0;
    while (num > 0) {
        int digit = num % 10;
        reversedNum = reversedNum * 10 + digit;
        num /= 10;
    }
    return reversedNum;
}


