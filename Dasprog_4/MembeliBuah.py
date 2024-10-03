N, K = map(int, input().split())
harga_buah = list(map(int, input().split()))

harga_buah.sort()  
jumlah_buah = 0

for harga in harga_buah:
    if K >= harga:
        jumlah_buah += 1

print(jumlah_buah)