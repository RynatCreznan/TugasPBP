link = "https://pbptugas2elang.herokuapp.com/todolist"

Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
untuk menghindari serangan csrf, jika tidak ada potongan kode tersebut maka akan terjadi error.
  
Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
bisa, dengan menggunakan tag
  
Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
user melakukan input dengan melakukan submit, dan akan dilakukan pengecekan apakah input valid atau tidak, jika tidak maka akan disuruh input ulang, jika valid maka akan terdata di database. Setelah itu akan ditampilkan dalam html
  
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Pertama kita melakukan startapp todolist. Kemudian di project_django kita menambahkan todolist di settings.py dan pathnya di urls.py. Setelah itu kita bikin templates di todolist yang berjumlah 4 untuk register, login, todolist, dan tambah task. tidak lupa membuat fungsinya di views.py dan mendaftarkan pathnya di urls.py di todolist. makemigrations dan migrate. Terakhir lakukan deployment
  
