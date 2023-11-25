import sys
input = sys.stdin.readline

wrd = input()
ans = []
for i in range(26):
	ans.append(wrd.count(chr(97+i)))
print(*ans)