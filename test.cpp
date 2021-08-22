#include <stdio.h>
int main() {
    int arr[10] = {0};
    int count = 0;
    for(int i = 0; i < 10; i++) {
        scanf("%d", &arr[i]);
        if(arr[i] % 2 != 0) {
            count++;
        }
    }
    printf("%d", count);
    return 0;
}