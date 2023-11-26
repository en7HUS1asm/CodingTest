import sys
input = sys.stdin.readline

N = input()
N_1 = int(N,2)
ans = oct(N_1)
print(ans[2:])