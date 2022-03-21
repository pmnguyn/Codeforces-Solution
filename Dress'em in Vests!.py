n, m, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
i = 0
j = 0
while i < n and j < m:
	if b[j] < a[i] - x:
		j = j + 1
	elif b[j] > a[i] + y:
		i = i + 1
	else:
		i = i + 1
		j = j + 1
		a[count] = i
		b[count] = j
		count = count + 1
print(count)

for k in range(count):
  print(a[k], b[k])
