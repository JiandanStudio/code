#include <cstdio>

int stepNum(int a){
    if(a == 1){
        return 0;
    }

    int num = 0;
    while (a != 1)
    {
        if(a % 2 == 0){
            a /= 2;
        }else{
            a = (a * 3 + 1) / 2;
        }
        num++;
    }
    return num;
}

int main(){
    int a;
    scanf("%d", &a);
    int num = stepNum(a);
    printf("%d", num);
    return 0;
}