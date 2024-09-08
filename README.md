*Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)*

Cara saya mengimplementasikan checklist:
1. Membuat proyek Django baru dengan membuat repo baru di github terlebih dahulu, lalu membuat direktori lokal dan clone dan inisialisasi git dan add remote url, lalu memulai virtual environment dan install dependencies, lalu buat proyek Django baru bernama consign_pbp.
2. Membuat aplikasi dengan nama main dengan cara menjalankan command python manage.py startapp main, 
3. Lalu mendaftarkan 'main' pada INSTALLED_APPS pada file settings.py di direktori proyek.
4. Membuat model pada main dengan nama Product, yang berisikan atribut title, item_type, item_name, item_price, item_description dengan tipe data yang sesuai. Jangan lupa untuk make migrations.
5. Membuat fungsi pada views.py bernama show_main yang mengembalikan template HTML yang menampilkan title, item_type, item_name, item_price, item_description.
6. Mengonfigurasi routing pada urls.py pada main dan project. path('', include('main.urls')) untuk project dan 

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]

pada urls.py di direktori main.

7. Deployment ke PWS dengan membuat project baru pada PWS, lalu menambahkan URL project PWS ke ALLOWED_HOST pada settings.py, selanjutnya run command yang diperlukan untuk push code ke PWS.

*Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.*

- bagan request client 
Client (Browser)
    |
    |-- request (URL) --> [urls.py]
                         - nentuin URL yang sesuai dengan request
    |
    |-- request diteruskan ke [views.py]
                         - jalankan logika untuk menangani request
                         - kalo perlu, meminta data dari [models.py]
    |
    |-- [models.py] akses database
                         - ambil atau memanipulasi data yang diminta
                         - return data ke [views.py]
    |
    |-- [views.py] memproses data
                         - milih berkas template HTML untuk dirender
                         - mengirim data ke template HTML
    |
    |-- template HTML (Tampilan)
                         - berisi data yang disertakan dari [views.py]
                         - nyusun dan menampilkan halaman ke client
    |
    |-- respon (HTML) --> Client (Browser)
                         - halaman hasil request ditampilkan


*Jelaskan fungsi git dalam pengembangan perangkat lunak!*
git dalam pengembangan perangkat lunak berfungsi untuk merubah atau mengelola source code suatu program yang nantinya mempermudah programmer untuk mengelola kode yang akan ditambah atau diremove.

*Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?*
Dari semua framework yang ada, Django dijadikan permulaan karena mudah digunakan untuk orang yang baru belajar membuat web. Struktur dari Django mempunyai pola MVT yang memudahkan pengorganisasian kode secara rapih. Django juga menggunakan python yang kita sudah belajar pada DDP-1. 

*Mengapa model pada Django disebut sebagai ORM?*
Model pada Django disebut sebagai Object-Relational Mapping karena pola pemrograman Django menghubungkan anatara database dan objek dalam python. Contohnya yaitu pada tugas kali ini, kita mendefinisikan model, lalu mengambil data dari model, lalu mengupdate data ke view/tampilan