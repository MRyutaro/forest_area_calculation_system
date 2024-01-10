import matplotlib.pyplot as plt
from tifffile import TiffFile

tifffile_path = r'data\JAXA_HRLULC_Japan_v23.12\LC_N34E135.tif'

with TiffFile(tifffile_path) as tif:
    image = tif.asarray()

plt.imshow(image)
plt.show()
