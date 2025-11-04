import tkinter as tk
import tkinter.messagebox as msg

top = tk.Tk()
top.title("prediksinilai")
top.geometry("400x300")
top.configure(bg="lightblue")

L1 = tk.Label(top, text="Aplikasi Prediksi Prodi Pilihan:")
L1.pack()
E1 = tk.Entry(top,)
E1.pack()
for i in range(10):
    L = tk.Label(top, text=f"Masukkan Nilai mata pelajaran-{i+1}:")
    L.pack()
    E = tk.Entry(top, bd=3 )
    E.pack()


def tampilkanprodi():
    nama = E1.get()
    msg.showinfo("Hasil prediksi adalah", f"prodi anda adalah : Teknologi Informasi")


tombolnama = tk.Button(top, text="Tampilkan Nama", command=tampilkanprodi)
tombolnama.pack(pady=11)

top.mainloop()
