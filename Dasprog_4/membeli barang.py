N, M = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

harga = 0
uang = 0
hutang = 0

total_harga = 0
for i in P:
    if i > 0:
        harga += 1
        total_harga += i

total_pecahan = 0
for j in C:
    if j < 0:
        uang += 1
        total_pecahan += j

if harga == len(P) and uang == 0:
    hutang = min(C) - sum(P)
elif harga == 0 and uang == len(C):
    hutang = sum(C) - max(P)
elif harga > 0 and uang > 0:
    hutang = total_pecahan - total_harga

print(hutang)