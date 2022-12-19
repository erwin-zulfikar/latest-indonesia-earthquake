"""
Konsep Dasar OOP adalah setiap komponen program seolah-olah adalah sebuah objek.
Dan setiap objek selalu memiliki Identitas dan juga Perilaku / Kemampuan untuk melakukan tugas tertentu.
Analogi Objek Segitiga
1. Segitiga adalah sebuah objek.
2. Objek segitiga memiliki 2 identitas (variabel) berupa alas dan tinggi.
3. Objek segitiga memiliki “kemampuan” (fungsi) untuk menghitung luasnya sendiri.

Sebelumnya, kita perlu tahu dulu bahwa sesuatu tidaklah dikatakan objek,
kecuali jika memiliki atribut atau perilaku.
Identitas = berupa Variabel (Alas dan Tinggi dari Objek Segitiga)
Perilaku / Kemampuan = berupa Method / Fungsi (Hitung Luas / get_luas dari Objek Segitiga)
Konstruktor adalah sebuah fungsi yang akan dipanggil pertama kali saat sebuah objek di-instantiasi-kan.
Fungsi tersebut harus selalu bernama __init__()

Kesimpulan:
1. Objek pada python adalah kumpulan dari variabel-variabel (dinamakan atribut)
dan kumpulan dari fungsi-fungsi (dinamakan perilaku).
2. Atas definisi itu, maka semua hal di dalam python adalah sebuah Objek.
3. Objek dan Kelas dalam python bermakna sama. Akan tetapi, jika disebutkan dalam konteks terpisah,
maka kelas adalah blueprint dan objek adalah variabel nyata.
4. Konstruktor adalah fungsi yang pertama kali dipanggil ketika sebuah objek diinstantiasi.
5. Objek bisa memiliki atribut yang berupa instan dari kelas lainnya
"""


class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas                        # identitas (variabel)
        self.tinggi = tinggi                    # identitas (variabel)

    def get_luas(self):                         # perilaku/kemampuan (method/fungsi)
        return 0.5 * self.alas * self.tinggi


segitiga1 = Segitiga(5, 10)                     # buat objek segitiga1 dari class Segitiga
segitiga2 = Segitiga(10, 10)                    # buat objek segitiga2 dari class Segitiga

print('luas segitiga1:', segitiga1.get_luas())  # cetak objek segitiga1
print('luas segitiga2:', segitiga2.get_luas())  # cetak objek segitiga2
