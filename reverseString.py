import time
import matplotlib.pyplot as plt
import numpy as np
import sys
from decimal import Decimal

sys.setrecursionlimit(150000)

def reverse_string_iteratif(string):
    """Membalikkan string menggunakan loop."""
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return reversed_string

def reverse_string_rekursif(string):
    """Membalikkan string menggunakan rekursi."""
    if len(string) == 0:
        return string
    else:
        return reverse_string_rekursif(string[1:]) + string[0]

def measure_time(func, string):
  start_time = time.perf_counter()
  func(string)
  end_time = time.perf_counter()
  return end_time - start_time  # No need to format here, perf_counter already returns in seconds

# Tentukan ukuran input
input_sizes = [10,20,50,100,200,500,1000,5000,10000,12500,15000]

# Inisialisasi dictionary untuk menyimpan waktu eksekusi
loop_times = {}
recursive_times = {}

for size in input_sizes:
    string = "a" * size  # Buat string dengan ukuran yang diinginkan

    # Mengukur waktu dan menyimpannya dalam dictionary
    loop_times[size] = measure_time(reverse_string_iteratif, string)
    recursive_times[size] = measure_time(reverse_string_rekursif, string)

# print(loop_times)
# print(recursive_times)


for size, time in loop_times.items():
    print(f"Size: {size}, Iterative Time: {Decimal(time):.10f} seconds")
print("")
for size, time in recursive_times.items():
    print(f"Size: {size}, Recursive Time: {Decimal(time):.10f} seconds")

plt.plot(list(loop_times.keys()), list(loop_times.values()), label="Iteratifm", marker = "o")
plt.plot(list(recursive_times.keys()), list(recursive_times.values()), label="Rekursif", marker = "o")
plt.xlabel("Ukuran Input")
plt.ylabel("Waktu Eksekusi (detik)")
plt.title("Perbandingan Waktu Eksekusi Fungsi Pembalik String")
plt.legend()
plt.show()