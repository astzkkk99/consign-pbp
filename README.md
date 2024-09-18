**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

Dalam pengimplementasian suatu platform, data delivery diperlukan karena memungkinkan komunikasi antar komponen, dalam bentuk pertukana informasi antara server
dan client. Data delivery memastikan bahwa informasi yang dibutuhkan oleh aplikasi dapat dikirimkan, diproses, dan diambil sesuai kebutuhan.

**Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**

Baik XML maupun JSON, memiliki kelebihan dan kekurangannya masing-masing:

XML lebih baik dalam kasus di mana struktur data yang kompleks diperlukan, dan metadata yang lebih detail dibutuhkan.
JSON lebih sederhana, lebih ringan dalam sintaksnya, JSON lebih baik digunakan untuk komunikasi berbasis web.

JSON lebih populer karena lebih ringkas, lebih mudah dibaca oleh manusia, memiliki kecepatan yang lebih baik dalam memproses data dibandingkan XML.

**Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**
Dalam Django, method is_valid() digunakan untuk memvalidasi form yang dikirim oleh pengguna. Ketika method ini dipanggil, Django akan memeriksa apakah data yang dimasukkan sesuai dengan aturan yang telah ditentukan di form (misalnya, tipe data, panjang maksimal, input yang dibutuhkan, dll.). Jika form valid, method ini mengembalikan nilai True. Jika tidak valid, method ini mengembalikan False, dan Django menyimpan pesan kesalahan yang dapat ditampilkan kepada pengguna.

Kita membutuhkan is_valid() untuk memastikan bahwa data yang diinputkan oleh pengguna sesuai dengan aturan yang berlaku sebelum diproses lebih lanjut (misalnya disimpan ke database). Hal ini mencegah terjadinya error atau kesalahan logika dalam aplikasi yang disebabkan oleh input yang tidak valid.

**Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**
csrf_token (Cross-Site Request Forgery token) adalah token keamanan yang digunakan oleh Django untuk melindungi aplikasi web dari serangan CSRF. CSRF adalah serangan di mana penyerang mencoba untuk mengelabui pengguna agar mengirimkan permintaan yang tidak diinginkan ke server atas nama mereka tanpa sepengetahuan pengguna.

Ketika kita membuat form di Django, csrf_token ditambahkan untuk memastikan bahwa setiap permintaan yang dikirimkan oleh pengguna (seperti mengirimkan form) berasal dari sumber yang sah, yaitu aplikasi itu sendiri. Django memverifikasi bahwa token yang dikirimkan dengan form cocok dengan yang disimpan di sesi pengguna.

Jika kita tidak menambahkan csrf_token pada form, aplikasi kita menjadi rentan terhadap serangan CSRF. Dalam serangan ini, penyerang dapat memanfaatkan kredensial sesi pengguna untuk melakukan aksi yang tidak diinginkan, seperti mengubah data atau melakukan transaksi tanpa sepengetahuan pengguna. Misalnya, penyerang bisa membuat form di situs web yang mereka kontrol yang secara otomatis mengirim permintaan ke aplikasi Django dengan kredensial sesi pengguna yang sedang aktif. Tanpa csrf_token, server tidak dapat membedakan apakah permintaan tersebut berasal dari pengguna yang sah atau dari penyerang.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
- Membuat input form untuk menambahkan objek model pada app sebelumnya.

untuk menerima data item yang akan dijual, buat file forms.py pada direktori main, lalu tambahkan kode berikut : 

```

from django.forms import ModelForm
from main.models import Item

class ItemEntryForm(ModelForm):
    class Meta:
        model = Item
        fields = ["item_type", "item_name", "item_price", "item_description"]

```

sesuaikan fields dengan model yang sudah dibuat.

Lalu pada views.py pada direkotori main, tambahkan import berikut:

```
from django.shortcuts import render, redirect 
```
Lalu buat fungsi baru untuk membuat form entry usernya yang menerima parameter request. 
```
def create_item_entry(request):
    form  = ItemEntryForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_item_entry.html", context)
```
Lalu ubah fungsi show_main pada views.py dengan menambahkan item_entries sebagai berikut:

```
def show_main(request):
    item_entries = Item.objects.all()
    
    context = {
        'title' : "CONSIGN!",
        'item_type' : "Console",
        'item_name' : "PS4",
        'item_price': '2000000',
        'item_description': "PS4 bekas, udah dipake 4 tahun, minus lecet aja",
        'item_entries' : item_entries,
    }

    return render(request, "main.html", context)
```
Lalu buka urls.py pada main, import fungsi create_item_entry, dan tambahkan path ke urlpatterns:
```
from main.views import show_main, create_item_entry
```
```
path('create-item-entry', create_item_entry, name='create_item_entry'),
```
Lalu buat file html dengan pada direktori main/templates.
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```
Kode ini untuk menambahkan csrf token untuk security, mengeluarkan input sebagai tabel, dan untuk user mengsubmit barang yang ingin dijual.

Lalu pada main.html, tambahkan kode berikut untuk menampilkan data item pada bentuk tabel, dan membuat button yang dapat digunakan user.
```
{% extends 'base.html' %}
{% block content %}
<h1>{{ title }}</h1>

<h5>Item Type: </h5>
<p>{{ item_type }}<p>
<h5>Name: </h5>
<p>{{ item_name }}<p>
<h5>Price (Rp): </h5>
<p>{{ item_price }}<p>
<h5>Description: </h5>
<p>{{ item_description }}<p>

{% if not item_entries %}
<p>Belum ada item pada direktori!</p>
{% else %}
<table>
    <tr>
    <th>Type</th>
    <th>Name</th>
    <th>Price</th>
    <th>Description</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data mood di bawah baris ini 
    {% endcomment %} 
    {% for item_entry in item_entries %}
    <tr>
    <td>{{item_entry.item_type}}</td>
    <td>{{item_entry.item_name}}</td>
    <td>{{item_entry.item_price}}</td>
    <td>{{item_entry.item_description}}</td>
    </tr>
    {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_item_entry' %}">
    <button>Add Item</button>
</a>
{% endblock content %}
```

- Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.

untuk mengembalikan data dalam bentuk XML, import
```
from django.http import HttpResponse
from django.core import serializers
```
pada file views.py di main.

buatlah fungsi baru yang dapat mereturn data dalam XML:
```
def show_xml(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
Lalu pada urls.py pada main, import fungsi show_xml, lalu tambahkan path url ke urlpatterns.
```
path('xml/', show_xml, name='show_xml'),
```

Selanjutnya untuk JSON, buat fungsi yang mereturn data dalam bentuk JSON:
```
def show_json(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
Lalu pada urls.py pada main, import fungsi show_json, lalu tambahkan path url ke urlpatterns.
```
path('json/', show_json, name='show_json'),
```

Selanjutnya untuk mengembalikan data dalam XML by ID, dan JSON by ID, buatlah fungsi baru pada views.py: 
```
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

