n = int(input())
L = list(map(int, input().split()))
count = 1
s = n - 1

for i in range(n): 
	L[i] = i - L[i]

for i in range(n-1, -1, -1):
	if i < s:
		count += 1
	s = min(s, L[i])

print(count)
