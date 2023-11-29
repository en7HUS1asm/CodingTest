import sys
input = sys.stdin.readline

N=  int(input())
lst = [list(map(int, input().split())) for _ in range (N)]
for i in range(N):
	print("Case #"+str(i+1)+":",sum(lst[i]))