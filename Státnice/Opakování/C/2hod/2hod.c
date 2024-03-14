//
// Created by marti on 14.03.2024.
//

#include "stdio.h"

float ukol1() {

    float small_frac = (float) 3 / 2;
    int twelve = 12;
    float big_frac = (float) ((5 * 5) - (2 * 2)) / 6;

    return small_frac + twelve + big_frac;
}

void help_ukol2(int *a, int *b, int *c, int *d, int *e) {
    *a = 2;
    *b = 2;
    *c = 0;
    *d = 1;
    *e = 4;
}

void ukol2() {
    int a, b, c, d, e;

    help_ukol2(&a, &b, &c, &d, &e);
    float first = (float) a++ / b-- * d++;
    help_ukol2(&a, &b, &c, &d, &e);
    float second = b-- * c++ + e;
    help_ukol2(&a, &b, &c, &d, &e);
    float third = -b + --c;
    help_ukol2(&a, &b, &c, &d, &e);
    float fourth = ++a + a--;
    help_ukol2(&a, &b, &c, &d, &e);
    float fifth = c / a * d++ / c--;
    help_ukol2(&a, &b, &c, &d, &e);
    float sixth = a %= b = d = 1 + e / 2;

    help_ukol2(&a, &b, &c, &d, &e);

    printf("%f\n", first);
    printf("%f\n", second);
    printf("%f\n", third);
    printf("%f\n", fourth);
    printf("%f\n", fifth);
    printf("%f\n", sixth);

}


void ukol3(float a) {
    float obvod = 4 * a;
    float obsah = a * a;
    printf("Obvod: %f\n", obvod);
    printf("Obsah: %f\n", obsah);
}

int ukol4(char small_char) {
    if (small_char < 64 || small_char > 91) return 1;

    char res = (small_char + (char) 32);
    printf("%c\n", res);
    return 0;
}


void ukol5(int num){

    int first_num = (num / 100) % 10;
    int third_num = num % 10;

    printf("%i\n", first_num);
    printf("%i\n", third_num);
}

int ukol6(float num){
    return num / 1;
}

void ukol7(){
    printf("%s\n", "Uspesnost predmetu \"Diskretni struktury\", ktery ma zkratku KMI/DISK1, je 50%.");
}
