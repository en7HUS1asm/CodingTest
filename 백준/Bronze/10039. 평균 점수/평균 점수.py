import sys
input = sys.stdin.readline

lst = [int(input()) for _ in range(5)]
lst = [i if i > 40 else 40 for i in lst]
ans = sum(lst)//5
print(int(ans))