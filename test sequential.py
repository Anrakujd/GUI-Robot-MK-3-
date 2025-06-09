import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("from dinamis lengkap")
root.geometry("800x600")

entries = []
baris_ke = 0

frame = tk.Frame(root)
frame.pack(pady = 10)

#fungsi menambah textbox
def hapus_textbox(index):
    for widget in entries[index]["widgets"]:
        widget.destroy()
    entries.index=None
        

def tambah_textbox():
    global baris_ke
    satu_baris =[]
    widgets = []

    for kolom_ke in range(4):
        entry = tk.Entry(frame, width = 15)
        entry.grid(row = baris_ke, column = kolom_ke, padx=5, pady=5)
        satu_baris.append(entry)
        widgets.append(entry)
        
    btn_hapus = tk.Button(frame, text="Hapus", command = lambda idx=baris_ke: hapus_textbox(idx))
    btn_hapus.grid(row=baris_ke, column = 4, padx = 5)

    widgets.append(btn_hapus)

    entries.append({"entries": satu_baris, "widgets": widgets})
    baris_ke += 1

def tampilkan_isi():
    #print("isi semua texbox:")
    for i, baris in enumerate(entries, start=1):
        if baris is not None:
            isi = [e.get() for e in baris["entries"]]
        print("Baris {}: {}".format(i, isi))

#def simpan_ke_file():
    #if not entries:
       # messagebox.showinfo("info", "tidak ada data untuk disimpan")
        #return

    #with open("isi_textbox.txt", "w", encoding="utf-8") as f:
       # for i, (entry,_) in enumerate(entries, start = 1):
           # f.write("Textbox {}: {}\n".format(i, entry.get()))
   # messagebox.showinfo("Berhasil", "isi textbox disimpan ke file")

tk.Button(root, text="Tambah Baris", command=tambah_textbox).pack(pady = 10)
tk.Button(root, text="Tampilkan isi", command=tampilkan_isi).pack(pady = 5)
#tk.Button(root, text="simpan ke file", command=simpan_ke_file).pack(pady = 5)

root.mainloop()
        
