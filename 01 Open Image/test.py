import cv2

img = cv2.imread("01 Open Image\\botol.jpg")
# type(img) #-> cek tipe data
#img.shape -> cek ukuran data
#{[tinggi ukuran gambar], {panjang ukuran gambar}, {channel atau berapa banyak warna} -> layer cv BGR(Blue,Green,Red)}

#height, width, channel = img.shape #-> untuk mengambil panjang masing masing data gambar

cv2.imshow("sampah",img)
cv2.waitKey(0)