#pengguna input
input_user = input("masukkan nama barang, harga satuan, jumlah (pisahkan pake koma :)")

#memisahkan nilai nilai variabel dan memasukkan nya sesuia urutan
nama_barang, harga_satuan, jumlah_barang = input_user.split(",")

#menghilangkan spasi berlebih dan memberikan format datanya
nama_barang = str(nama_barang.strip())
harga_satuan = int(harga_satuan.strip())
jumlah_barang = int(jumlah_barang.strip())

#proses penghitungan dengan rumus
sub_total = harga_satuan * jumlah_barang
pajak = sub_total * 0.11
total_belanja = sub_total + pajak

#Output
print (f"Subtotal = {sub_total} PPN= {pajak} Total= {total_belanja}")
