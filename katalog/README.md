berikut link heroku saya : https://pbptugas2elang.herokuapp.com/

Bagan dan Penjelasan 

![image](https://user-images.githubusercontent.com/86994564/190307354-19e62ac2-8383-451e-8452-43184b60d8ef.png)



Pertama, permintaan klien diproses oleh middlewares dan kemudian meneruskan permintaan ke router URL.Urls.py digunakan agar pengguna bisa mengakses aplikasi kita. Saat pengguna membuat request untuk sebuah halaman pada aplikasi web, Django controller mengambil alih untuk mencari tampilan yang diminta melalui file url.py, kemudian mengembalikan respons HTML atau 404 not found error jika tidak menemukannya. Jika URL cocok atau ditentukan, fungsi di views.py dipanggil.Views.py adalah fungsi Python yang mengambil request pada web dan mengembalikan respons web. Respons bisa berupa kode HTML dari halaman web, gambar, 404 error, dokumen XML, atau yang lainnya.Kemudian tampilan akan melakukan kueri ke model dan model mengembalikan hasil query ke tampilan. Models.py digunakan untuk menampilkan tata letak suatu aplikasi. Models.py adalah subclass dari classdjango.db.models.Model. Semua field diwakili oleh instance dari subclassdjango.db.models.Field. Setelah itu tampilan akan mengembalikan respons ke pengguna dalam bentuk html

Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Anda dapat membangun dan menjalankan aplikasi Django tanpa lingkungan virtual yang diinisialisasi. Namun, ketika Anda mencoba menginstal paket Django apa pun, paket itu akan diinstal pada paket global Anda. Lingkungan virtual mencegah Anda menginstal paket Python secara global dengan membuat lingkungan python yang terisolasi untuk setiap proyek. Membuat virtual env sangat disarankan karena ketika virtualenv Anda diaktifkan dan mencoba membekukan pip < requirements.txt, ini memungkinkan Anda untuk menulis semua dependensi yang digunakan untuk proyek, tidak semua dependensi secara global.

Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
Pertama kita mengkonfigurasi views.py yang berada di katalog, kita memberi informasi yang di perlukan seperti nama dan npm. Kemudian kita mengkonfigurasi urls.py di project_django folder agar bisa menampilkan /katalog. Setelah itu kita juga konfigurasi urls.py yang berada di katalog dengan mengisi path dengan string kosong agar bisa menampilkan /katalog. Setelah itu, rubah isi katalog.html agar bisa mengiterasi looping untuk menampilkan konten. Dan yang terakhir melakukan deploy di herokuapp
