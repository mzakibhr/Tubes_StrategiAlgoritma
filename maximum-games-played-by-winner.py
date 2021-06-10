import math
import timeit
def maxGameByWinnerDynamic(n):
    start = timeit.default_timer()
    dp = [0 for jumlahpermainan in range(n)]
     
    # jika hanya 1 pemain maka hanya terdapat 0 permainan
    # untuk 1 permainan maka dibutuhkan 2 pemain
    dp[0] = 1
    dp[1] = 2
     
    # loop sampai ke-jumlahpermainan Fibonacci
    # bilangan kurang dari atau sama dengan n
    jumlahpermainan = 1
    while dp[jumlahpermainan] <= n:
        jumlahpermainan = jumlahpermainan + 1
        dp[jumlahpermainan] = dp[jumlahpermainan - 1] + dp[jumlahpermainan - 2]

    # hasil (jumlahpermainan - 1) ditambahkan 1 pada pembulatan pada loop while   
    # dan hasil yang diinginkan adalah nilai terakhir, yaitu yang lebih kecil dari n
    stop = timeit.default_timer()
    execution_time = stop - start
    return (jumlahpermainan - 1), execution_time

def maxGameByWinnerBruteForce(n):
    start = timeit.default_timer()
    jumlahpermainan = 0 #jumlah permainan dimulai dari 0 permainan
    # akan dilakukan loop sampai pemain kurang dari 2 pemain
    i = 2
    while i <= n:
        n = n/2
        jumlahpermainan = jumlahpermainan + 1
        if n % 2 != 0: # jika ganjil maka pemain akan dibulatkan untuk permainan selanjutnya
            n = math.ceil(n)
    stop = timeit.default_timer()
    execution_time = stop - start
    return jumlahpermainan, execution_time
 
# Main Program
n = int(input("Masukkan Jumlah Pemain: "))
print("=======================================")
print("Berdasarkan Algoritma Brute Force\nJumlah Pemain :", n,"\nUntuk Menang Membutuhkan", maxGameByWinnerBruteForce(n)[0], "Permainan")
print("Waktu Eksekusi: ",maxGameByWinnerBruteForce(n)[1], "seconds")
print("=======================================")
print("=======================================")
print("Berdasarkan Algoritma Dynamic\nJumlah Pemain :", n, "\nUntuk Menang Membutuhkan", maxGameByWinnerDynamic(n)[0], "Permainan")
print("Waktu Eksekusi: ",maxGameByWinnerDynamic(n)[1], "seconds")
