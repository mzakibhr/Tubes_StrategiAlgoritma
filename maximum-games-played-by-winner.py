import math
import timeit
def maxGameByWinnerDynamic(N):
    start = timeit.default_timer()
    dp = [0 for jumlahpermainan in range(N)]
     
    # jika hanya 1 pemain maka hanya terdapat 0 permainan
    # untuk 1 permainan maka dibutuhkan 2 pemain
    dp[0] = 1
    dp[1] = 2
     
    # loop sampai ke-jumlahpermainan Fibonacci
    # bilangan kurang dari atau sama dengan N
    jumlahpermainan = 1
    while dp[jumlahpermainan] <= N:
        jumlahpermainan = jumlahpermainan + 1
        dp[jumlahpermainan] = dp[jumlahpermainan - 1] + dp[jumlahpermainan - 2]

    # hasil (jumlahpermainan - 1) ditambahkan 1 pada pembulatan pada loop while   
    # dan hasil yang diinginkan adalah nilai terakhir, yaitu yang lebih kecil dari N
    stop = timeit.default_timer()
    execution_time = stop - start
    return (jumlahpermainan - 1), execution_time

def maxGameByWinnerBruteForce(N):
    start = timeit.default_timer()
    jumlahpermainan = 0 #jumlah permainan dimulai dari 0 permainan
    # akan dilakukan loop sampai pemain kurang dari 2 pemain
    while N >= 2: 
        N = N/2
        jumlahpermainan = jumlahpermainan + 1
        if N % 2 != 0: # jika ganjil maka pemain akan dibulatkan untuk permainan selanjutnya
            N = math.ceil(N)
    stop = timeit.default_timer()
    execution_time = stop - start
    return jumlahpermainan, execution_time
 
# Main Program
N = int(input("Masukkan Jumlah Pemain: "))
print("=======================================")
print("Berdasarkan Algoritma Brute Force\nJumlah Pemain :", N,"\nUntuk Menang Membutuhkan", maxGameByWinnerBruteForce(N)[0], "Permainan")
print("Waktu Eksekusi: ",maxGameByWinnerBruteForce(N)[1], "seconds")
print("=======================================")
print("=======================================")
print("Berdasarkan Algoritma Dynamic\nJumlah Pemain :", N, "\nUntuk Menang Membutuhkan", maxGameByWinnerDynamic(N)[0], "Permainan")
print("Waktu Eksekusi: ",maxGameByWinnerDynamic(N)[1], "seconds")