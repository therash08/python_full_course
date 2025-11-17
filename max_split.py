
s = input()

balance = 0
count = 0
temp = ''
result = []

for ch in s:
    temp += ch
    if ch == 'L':
        balance += 1
    else:
        balance -= 1
    
    if balance == 0:
        result.append(temp)
        count += 1
        temp = ''

print(count)
for r in result:
    print(r)
