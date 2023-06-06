# Hangman-Game-Wth-Python

# Apa itu Game Hangman?
Hangman adalah permainan tebak kata sederhana di mana pemain harus menebak sebuah kata dengan menebak huruf-huruf yang membentuk kata tersebut. Pada awal permainan, kata yang harus ditebak disembunyikan dan pemain diberi jumlah kesempatan terbatas untuk menebak huruf-huruf yang benar. Jika pemain menebak huruf yang salah, maka kesempatan mereka berkurang.

Dalam permainan Hangman, ada beberapa komponen penting:

1. Kata Rahasia: Ini adalah kata yang harus ditebak oleh pemain. Pada awal permainan, kata rahasia ini disembunyikan dan hanya ditampilkan sebagai garis-garis pengganti untuk setiap huruf yang harus ditebak.
2. Jumlah Kesempatan: Pemain diberi jumlah kesempatan terbatas untuk menebak huruf-huruf yang benar sebelum mereka kalah. Setiap kali pemain menebak huruf yang salah, jumlah kesempatan akan berkurang.
3. Tebakan Huruf: Pemain harus menebak huruf-huruf yang membentuk kata rahasia. Mereka memasukkan huruf-huruf ini satu per satu dan program menentukan apakah huruf tersebut benar atau salah.
4. Tampilan Gantungan: Ada tampilan gantungan yang akan ditampilkan secara bertahap setiap kali pemain menebak huruf yang salah. Tampilan ini biasanya mencakup bagian-bagian tubuh manusia (seperti kepala, badan, tangan, dan kaki) yang digambar secara berturut-turut untuk menggambarkan jumlah kesalahan yang telah dilakukan.

Tujuan pemain dalam permainan Hangman adalah menebak kata rahasia sebelum jumlah kesempatan habis. Jika pemain berhasil menebak semua huruf-huruf yang benar sebelum jumlah kesempatan habis, mereka memenangkan permainan. Namun, jika jumlah kesempatan habis sebelum kata rahasia terungkap, pemain kalah.

# Konsep OOP Apa Saja yg di Gunakan pada Program tersebut?


Pada kode program tersebut, terdapat beberapa konsep OOP (Object-Oriented Programming) yang diterapkan:

1. Class: Terdapat kelas Hangman yang mewakili permainan Hangman. Ini adalah sebuah blueprint untuk objek permainan Hangman yang akan dibuat.
2. Encapsulation: Variabel-variabel dan metode-metode terkait Hangman dibungkus dalam kelas Hangman. Mereka memiliki tingkat aksesibilitas yang tepat (misalnya, variabel wordlist bersifat private) untuk menjaga integritas dan rincian implementasi kelas tersebut.
3. Constructor: Terdapat metode __init__ yang berfungsi sebagai konstruktor kelas Hangman. Ini dipanggil saat objek Hangman baru dibuat dan menginisialisasi variabel-variabel anggota.
4. Method: Terdapat berbagai metode dalam kelas Hangman seperti choose_word, play, reset_game, display_hangman, display_word, dan lain-lain. Metode-metode ini mengimplementasikan logika permainan Hangman dan berinteraksi dengan variabel-variabel anggota kelas.
5. Inheritance: Meskipun tidak terlihat dalam contoh kode yang diberikan, konsep pewarisan dapat diterapkan jika ada perluasan atau variasi dalam permainan Hangman. Misalnya, Anda dapat membuat kelas turunan dari Hangman yang mengimplementasikan peraturan permainan yang sedikit berbeda.
6. Polymorphism: Kode program ini menggunakan polimorfisme secara tidak langsung. Misalnya, metode display_hangman dapat menghasilkan tampilan gantungan dengan berbagai tingkat kegagalan, tergantung pada nilai self.current_attempt. Dengan memperluas kode, Anda dapat membuat berbagai tampilan yang berbeda tergantung pada situasi.
7. Data Abstraction: Dalam kelas Hangman, variabel-variabel anggota dan detail implementasinya disembunyikan dari pengguna lain yang menggunakan objek Hangman. Pengguna hanya perlu mengetahui metode-metode publik yang dapat mereka panggil untuk berinteraksi dengan objek Hangman.

Penerapan konsep-konsep OOP dalam kode program ini membantu dalam organisasi, pemeliharaan, dan perluasan kode dengan cara yang terstruktur dan modular.


# Nama Anggota kelompok:
1. M. Febri Ardiansyah (G1A022049)
2. Muhammad Kevin Rinaldi (G1A022059)
3. Revan Averuz Mufid (G1A022065)

