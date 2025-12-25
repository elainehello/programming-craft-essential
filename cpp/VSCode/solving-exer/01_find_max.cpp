#include <iostream>
#include <cstdio>
using namespace std;

int max_of_four(int a, int b, int c, int d)
{
    int arr[4] = {a, b, c, d};
    int arrLength = sizeof(arr)/sizeof(arr[0]);
    int max = arr[0];
    
    for (int i = 1; i < arrLength; i++) {
        if (max < arr[i]) {
            max = arr[i];
        }
    }
    return max;
}

int main()
{
    int a, b, c, d;
    printf("Enter numbers:\n");
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("The max value is: %d\n", ans);

    return 0;
}