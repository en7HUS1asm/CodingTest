import sys
input = sys.stdin.readline

S = int(input())
ans = 1
while S >= (ans*(ans+1))//2:
	ans +=1
ans-=1
print(ans)