import sys
input = sys.stdin.readline

E,S,M= map(int, input().split())
En, Sn, Mn = 15, 28, 19
E = 0 if E==En else E
S = 0 if S==Sn else S
M = 0 if M==Mn else M

ans, tmp = 0, 0
while True:
	if (tmp*Sn+S) % En == E and (tmp*Sn+S) % Mn == M:
		ans = tmp*Sn+S
		if ans !=0:
			break;
	tmp +=1
print(ans)