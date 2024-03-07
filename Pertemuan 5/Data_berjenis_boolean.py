# Case 1
print("Case 1")
# Data bertipe Boolean yang kita deklarasikan (Cara standar)
f = bool(True)
g = bool(False)
print(f)
print(g)
print("=====================================================")

# Case 2
print("Case 2")
# Data bertipe Boolean dalam berbagai konteks
# Tercatat dengan sendirinya oleh komputer tanpa deklarasi.
print(3>2)
print(3+2 == 5)
print(3<2)
print("=====================================================")

# Case 3
print("Case 3")
# Data bertipe Boolean dalam berbagai konteks
# Tercatat dengan sendirinya oleh komputer tanpa deklarasi.
Penghasilan = 20000000
PenghasilanTanpaPajak = 4000000
if Penghasilan <= PenghasilanTanpaPajak:
    PajakYangHarusDibayar = 0
if Penghasilan > PenghasilanTanpaPajak:
    PajakYangHarusDibayar = 0.1 * Penghasilan
print("Pajak yang harus Anda bayar: Rp ", PajakYangHarusDibayar)

# Case 4
print("Case 4")
# Semua data yang tidak nol (kosong) memiliki nilai Boolean True
a = 3
b = "Ini data string."
c = ("Laptop", "buku", "ballpen")
d = ["laptop", "buku", "ballpen"]
e = {"laptop": "asus", "buku": "buku_teks", "ballpen": "arrow"}
f = {1, 2, 3, 4, 5}
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print("=====================================================")

# Case 5
print("Case 5")
# Variabel yang kosong memiliki nilai Boolean False
a = 0
b = ""
c = ()
d = []
e = {}
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print("=====================================================")
# Case 6
print("Case 6")
# Variabel yang panjangnya nol memiliki nilai Boolean False
class myclass():
    def __len__(self):
        return 0
print(bool(myclass()))
print("=====================================================")