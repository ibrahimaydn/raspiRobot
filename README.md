# Raspberry Pi Zero W Robot Kontrol Sistemi (GUI + Kamera)

Bu proje, Raspberry Pi Zero W kullanılarak geliştirilen 2 modlu bir robot kontrol sistemidir:

- 🕹️ Manuel Mod: Tkinter GUI ile ok tuşları veya butonlar üzerinden robot kontrolü.
- 🤖 Otomatik Mod: Kamera üzerinden engel algılayarak kendini yönlendirme.

## Özellikler
- Python 3 ile yazılmıştır
- OpenCV kullanımı ile temel görüntü işleme
- GPIO motor sürme
- Kullanıcı dostu grafik arayüz

## Gereksinimler
- Raspberry Pi OS
- Kamera (v1.3)
- L298N motor sürücü
- Python kütüphaneleri: `opencv-python`, `RPi.GPIO`, `tkinter`

## Çalıştırma

```bash
python3 main.py
