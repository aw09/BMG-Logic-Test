result = ''
for i in range(1,51):
    if i % 15 == 0:
        result += 'Frontend Backend'
    elif i % 3 == 0:
        result+= 'Frontend'
    elif i % 5 == 0:
        result += 'Backend'
    else:
        result += str(i)
    
    result += ','

print()
result = result[:-1]
print(result)
string = "1,2,Frontend,4,Backend,Frontend,7,8,Frontend,Backend,11,Frontend,13,14,Frontend Backend,16,17,Frontend,19,Backend,Frontend,22,23,Frontend,Backend,26,Frontend,28,29,Frontend Backend,31,32,Frontend,34,Backend,Frontend,37,38,Frontend,Backend,41,Frontend,43,44,Frontend Backend,46,47,Frontend,49,Backend"

assert result == string  # OK