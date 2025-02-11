import cv2
from cv2 import cuda
import tensorflow as tf

gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print("GPU terdeteksi:", gpus)
else:
    print("GPU tidak terdeteksi. Periksa instalasi CUDA/cuDNN dan driver GPU.")

print("Jumlah device CUDA:", cv2.cuda.getCudaEnabledDeviceCount())

print(cv2.getBuildInformation())
# cuda.printCudaDeviceInfo(0)