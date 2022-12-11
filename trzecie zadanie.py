path = 'C://users//vdi-student//desktop//rozliczenie.csv'
mode = 'r'

with open (path, mode) as plik2:
    content = plik2.readlines()
    print(content[3])
for i in range (len(content)):
    print(content[i])
    content[i] = content[i].split('.')
   # print(content[i])
   # print(content[2][2])

   #obliczenie średniej wyplaty

total = 0
for i in range(1, len(content)):
    total = total + int(content[i][1])
print(total)
average = total / (len(content)-1)
print(round(average, 2))
# 3. obliczanie liczby kobiet na macierzynskim


