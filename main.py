import tkinter as tk
from motor_control import setup, ileri, geri, sola, saga, dur
import subprocess

setup()

def baslat_otomatik():
    subprocess.Popen(['python3', 'kamera.py'])

def tus_basilinca(event):
    if event.keysym == 'Up':
        ileri()
    elif event.keysym == 'Down':
        geri()
    elif event.keysym == 'Left':
        sola()
    elif event.keysym == 'Right':
        saga()

def tus_birakinca(event):
    dur()

def cikis():
    dur()
    pencere.destroy()

pencere = tk.Tk()
pencere.title("Raspberry Pi Robot Kontrol")
pencere.geometry("400x300")
pencere.bind("<KeyPress>", tus_basilinca)
pencere.bind("<KeyRelease>", tus_birakinca)

tk.Label(pencere, text="Manuel Kontrol için yön tuşlarını kullan").pack(pady=10)
tk.Button(pencere, text="Otomatik Modu Başlat", command=baslat_otomatik, height=2, width=25).pack(pady=20)
tk.Button(pencere, text="Çıkış", command=cikis, height=2, width=10).pack()

pencere.mainloop()
