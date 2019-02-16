f = open('file.txt', 'r')
x = f.readlines()
f.close()

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
stat = []

for init in range(26):
    stat.append(0)

for ch in str(x):
    for letter in range(26):
        if ch.upper() == letters[letter].upper():
            stat[letter] = stat[letter] + 1

max = []
maxcount = 0
mincount = stat[0]
min = []
for index in range(26):
    if maxcount < stat[index]:
        max = []
        max.append(letters[index])
    elif maxcount == stat[index]: 
        max.append(letters[index])
        
    if mincount > stat[index]:
        min = []
        min.append(letters[index])
    elif mincount == stat[index]: 
        max.append(letters[index])

strr = str(x)

strr = strr.upper().replace(max[0].upper(), '±±§§-=')

strr = strr.upper().replace(min[0].upper(), max[0].upper())

strr = strr.upper().replace('±±§§-=', min[0].upper())

print(strr.lower())



