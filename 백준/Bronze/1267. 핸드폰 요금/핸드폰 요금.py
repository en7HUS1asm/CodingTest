import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
ans = ""

def young(t):
    rate = 10
    charge = (t // 30) * rate + 10
    return charge

def min(t):
    rate = 15
    charge = (t // 60) * rate + 15
    return charge

ans_m, ans_y = 0, 0
for i in range(N):
	ans_m += min(lst[i])
	ans_y += young(lst[i])

if ans_m < ans_y:
	ans = "M " + str(ans_m)
elif ans_y < ans_m:
	ans = "Y " + str(ans_y)
else:
	ans = "Y " + "M " + str(ans_y)
print(ans)