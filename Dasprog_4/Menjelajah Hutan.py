r, c, n = map(int, input().split())
hutanEmas = []

for i in range(r):
    baris = list(map(int, input().split()))
    hutanEmas.append(baris)

gerakan = list(input())

x = 0 
y = 0
emas = hutanEmas[x][y]  

dalamHutan = True
for g in gerakan:
    if(g == 'R' and y + 1 < c):
        y += 1
        emas = emas + 3 + hutanEmas[x][y]
    elif(g == 'L' and y - 1 >= 0):
        y -= 1
        emas = emas - 2 + hutanEmas[x][y]
    elif(g == 'D' and x + 1 < r):
        x += 1
        emas = emas - 2 + hutanEmas[x][y]
    elif (g == 'U' and x -1 >= 0):  
        x -= 1
        emas = emas + 3 + hutanEmas[x][y]

    else:
        dalamHutan = False
        break

if  not dalamHutan:
    print(emas)
    print("gerakanmu salah bung!")
else: 
    (dalamHutan)
    print(emas)