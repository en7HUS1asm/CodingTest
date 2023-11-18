import sys
input = sys.stdin.readline

N = int(input())
lst = [list(input().strip()) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(2, len(lst[i])):
    	if lst[i][j] in lst[i][:j] and lst[i][j] != lst[i][j-1]:
    		lst[i][j] = '1'
    if lst[i].count('1')==0:
    	ans +=1
print(ans)