import sys
input = sys.stdin.readline

N = int(input())
lst = list(int(input()) for _ in range(N))
lst.sort()
for i in lst:
	print(i)