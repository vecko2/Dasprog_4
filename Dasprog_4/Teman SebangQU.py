N, r, c = map(int, input().split())
posisi_siswa = []
x_siswa = []
y_siswa = []

for _ in range (1, N+1):
    absen, x_absen, y_absen = map(int, input().split())
    posisi_siswa.append(absen)
    x_siswa.append(x_absen)
    y_siswa.append(y_absen)

for i in range (0, N):
    sebelahIsi = False
    for j in range(0,N):
       if(y_siswa[i] - 1 == y_siswa[j] and x_siswa[i] == x_siswa[j]) or (y_siswa[i] + 1 == y_siswa[j] and x_siswa[i] == x_siswa[j]):
        print (posisi_siswa[j])
        sebelahIsi = True
        break
    
    if not (sebelahIsi):
       print(0)