s = input()
t = input()
location = 0
a = ''

for i in range(len(s)):
  if s[i] != 'z':
    location = i
for i in range(len(s) - location - 1):
  a += 'a' 
s = s[0:location] + chr(ord(s[location]) + 1) + a

if (s == t):
  print("No such string")
else:
  print(s)
