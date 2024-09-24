**Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.**

Fungsi registrasi, login, dan logout bisa dibuat dengan mengimport library yang dibutuhkan masing-masing fungsi, dan membuat fungsinya masing-masing pada views.py, lalu membuat file HTML masing-masing, lalu menambahkan path url ke dalam urlpattern nya pada urls.py

Lalu merestriksi halaman main, maka halaman main hanya bisa diakses ketika user sudah login.

**Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.**

Setelah berhasil membuat ketiga fungsi tadi, register akun baru, dan menambahkan tiga new item entry.

**Menghubungkan model Product dengan User.**
note: dalam kode saya, Product diganti dengan Item.

Dalam models.py, import user from django.contrib.auth.models, lalu pada model Item yang sudah dibuat, tambahkan 
``` 
user = models.ForeignKey(User, on_delete=models.CASCADE)
```

Lalu pada views.py, ubah potongan kode create_item_entry untuk mencegah Django tidak menyimpan objek yang dibuat pada form langsung ke database. Dan return request.user untuk menandakan objek tersebut dimiliki oleh user yang sedang login.
```
def create_item_entry(request):
    form  = ItemEntryForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
        item_entry = form.save(commit=False)
        item_entry.user = request.user
        item_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_item_entry.html", context)
```

Jika sudah selesai, pastikan sudah ada satu user pada database dengan meregistrasi user baru. Lalu bisa migrasi model.

**Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.**

Untuk menampilkan username pengguna yang sedang logged in, modifikasi kode show_main menjadi seperti berikut : 
```
def show_main(request):
    item_entries = Item.objects.filter(user=request.user)
    
    context = {
        ......

        'user_name': request.user.username,

        ........
```
Item entries yang diubah berfungsi untuk menampilkan objek Item yang terhubung dengan pengguna yang sedang logged in, dan untuk menampilkan user yang sedang logged in pada website, ubah 'user_name' menjadi seperti di kode.

Untuk menampilkan cookies last_login, tambahkan import berikut pada views.py: 
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
Lalu pada fungsi login_user, tambahkan cookie last_login pada kode: 
```
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```
Lalu untuk menampilkannya pada halaman, tambahkan kode :
```
....

'last_login': request.COOKIES['last_login'],

....
```
pada show_main variabel context.

Lalu ubah fungsi logout_user menjadi seperti berikut:
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
yang berfungsi untuk menghapus cookie last_login saat user logout.

Lalu pada file main.html, tambahkan
```
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```
untuk menampilkan kapan user terakir login.


**Apa perbedaan antara HttpResponseRedirect() dan redirect()**
Dalam hal fungsionalitas, kedua fungsi tersebut sama, yaitu mengalihkan user ke URL baru. 

Namun parameter HttpResonseRedirect() hanya menerima URL, redirect() bisa menerima model, view, ataupun URL. 

Jadi redirect() lebih fleksibel daripada HttpResponseRedirect().

**Jelaskan cara kerja penghubungan model Product dengan User!**

Cara Kerja Penghubungan Model Product dengan User
1. Model User dan Product:

    Model User: Menyimpan informasi pengguna seperti username dan password. 
    
    Model Product: Menyimpan entri item yang dibuat oleh pengguna. Setiap entri item akan memiliki field user yang mengaitkan dengan pengguna yang membuatnya.

2. Menambahkan ForeignKey:

    Menambahkan user = models.ForeignKey(User, on_delete=models.CASCADE) di model Product menghubungkan setiap entri item dengan satu pengguna. Jika pengguna dihapus, entri item yang terkait juga akan dihapus.

3. Membuat Entri :

    Dalam fungsi create_item_entry, kita memeriksa apakah form valid.
    Jika valid, kita siapkan objek Product tanpa menyimpannya terlebih dahulu (commit=False).
    Kita kemudian menetapkan item_entry.user = request.user, yang berarti entri item ini milik pengguna yang sedang login.
    Terakhir, kita simpan objek item entry ke dalam database.

4. Menampilkan Entri item:

    Dalam fungsi show_main, kita ambil semua entri item milik pengguna yang sedang login dengan Product.objects.filter(user=request.user).
    Hanya entri item milik pengguna tersebut yang akan ditampilkan di halaman utama.

5. Migrasi Database:

    Setelah mengubah model, kita jalankan perintah migrasi untuk memperbarui database agar mencerminkan perubahan yang kita buat.
    Jika ada data lama, kita harus menetapkan pengguna default untuk menghindari error.

**Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.**

Authentication adalah proses verifikasi identitas pengguna, sedangkan Authorization adalah proses menentukan hak akses pengguna setelah terautentikasi.

Saat pengguna login, terjadi proses verifikasi identitas pengguna (authentication), setelah itu terjadi proses menentukan akses pengguna (authorization) setelah pengguna terautentikasi.

Django menyediakan sistem authentication secara built-in yang menghandle login dan logout user. Fitur yang tersedia pada Django seperti: 

Model User: Django memiliki model User yang menyimpan informasi pengguna.

Form Login: Anda bisa menggunakan AuthenticationForm untuk menangani login pengguna dengan validasi otomatis.

Django menyediakan fitur authorization dengan menggunakan @login_required untuk melindungi view tertentu yang membutuhkan authentication. Contohnya pada views.py, fungsi show_main : 
```
@login_required(login_url='/login')
def show_main(request):
    item_entries = Item.objects.filter(user=request.user)
    
    context = {

.....
```

**Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?**

Django mengingat pengguna yang telah login dengan mneggunakan sistem session yang menggunakan cookies. 

- Ketika user login, Django menyimpan Session ID berupa ID unik yang disimpan di server. ID sesi ini dikirim ke browser user dalam bentuk cookie.

- Cookie sessionid ini digunakan untuk menyimpan ID sesi sisi user. Ketika user mengunjungi situs yang sama lagi, browser mengirimkan cookie ini kembali ke server.

- Saat server menerima cookie, Django akan mencocokan ID sesi yang diterima dengan server. Jika cocok, maka user akan masih terautentikasi.

Cookies memiliki kegunaan lain seperti:
- Pengaturan Iklan : Cookies juga digunakan untuk menampilkan iklan yang relevan berdasarkan minat user.
- Personalisasi : Cookies dapat digunakan untuk menyimpan preferensi user, seperti bahasa yang dipilih atau tema tampilan.

Tidak semua cookies aman digunakan. Contohnya: 
- Persistent Cookies: Cookies yang tetap ada meskipun browser ditutup. Jika tidak diatur dengan benar, ini dapat menimbulkan risiko keamanan.
- Tracking Cookies : Selain menimbulkan masalah privasi, cookies ini dapat diakses oleh penyerang jika tidak dilindungi dengan baik, memungkinkan mereka untuk melacak aktivitas user tanpa izin.
def show_xml_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
Lalu import kedua fungsi berikut ke urls.py pada main. Dan tambahkan path URL ke urlpatterns:
```
path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
```
Screenshot Postman
- XML
  <img width="1271" alt="xml" src="https://github.com/user-attachments/assets/58f306a6-4240-492c-98d4-04408488c549">
- JSON
  <img width="1275" alt="json" src="https://github.com/user-attachments/assets/f4dce31f-797b-4b45-b8e0-eb29c1b14fa5">
- XML by ID
  <img width="1275" alt="xml by id" src="https://github.com/user-attachments/assets/f83a518e-b528-4451-ad8a-89df0d0dc9a4">
- JSON by ID
  <img width="1271" alt="json by id" src="https://github.com/user-attachments/assets/e3b24420-1a60-47a7-931f-1248f6cb0500">
