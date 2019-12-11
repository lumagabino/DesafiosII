t = int(input())
a2 = [2,4,8,6] 
a3 = [3,9,7,1]
a4 = [4,6]
a7 = [7,9,3,1]
a8 = [8,4,2,6]
a9 = [9,1]
for i in range(t): 
    a, b = [int(x) for x in input().split()]
    a = a%10
    if a==0:
        o = 1
    elif a==1:
        o = 1
    elif a==2:
        i = b%4-1
        o = a2[i]
    elif a==3:
        i = b%4-1
        o = a3[i]
    elif a==4:
        i = b%2-1
        o = a4[i]
    elif a==5:
        o = 5
    elif a==6:
        o = 6
    elif a==7:
        i = b%4-1
        o = a7[i]
    elif a==8:
        i = b%4-1
        o = a8[i]
    elif a==9:
        i = b%2-1
        o = a9[i]
    print(o)   


#include <iostream>
#include <cmath>
# using namespace std;

# typedef long long ll;

# int main()
# {
#     int a, t;
#     ll b;
#     cin>>t;
#     while (t--)
#     {
#         cin>>a>>b;
#         int r;

#         if (b==0) r = 1;
#         else if (a%10 == 0 || a%10 == 1 || a%10 == 5 || a%10 == 6 || b%4 == 1) r = a%10;
#         else if (b%4 == 0 && (a%10)%2 == 0) r = 6;
#         else if (b%4 == 0 && (a%10)%2 == 1) r = 1;
#         else if (b%4 == 2 || b%4 == 3) r = int(pow(a%10, b%4)) % 10;

#         cout<<r<<endl;
#     }
#     return 0;
# }