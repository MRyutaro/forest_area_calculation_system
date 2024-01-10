import matplotlib.pyplot as plt
from tifffile import TiffFile

tifffile_path = r'data\JAXA_HRLULC_Japan_v23.12\LC_N34E135.tif'

with TiffFile(tifffile_path) as tif:
    image = tif.asarray()

print(image)  # [[13 13 13 ...  9  9  9] ... [ 1  1  1 ...  9  9  9]]
print(image.shape)  # (12000, 12000)
print(type(image))  # <class 'numpy.ndarray'>

plt.imshow(image)
plt.show()
