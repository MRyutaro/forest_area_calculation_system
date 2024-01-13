import numpy as np
import pandas as pd
from tifffile import TiffFile

if __name__ == '__main__':
    tifffile_path = r'data\JAXA_HRLULC_Japan_v23.12\LC_N34E135.tif'

    with TiffFile(tifffile_path) as tif:
        image = tif.asarray()

        # tiffファイルの中身を確認する
        # print(image)  # [[13 13 13 ...  9  9  9] ... [ 1  1  1 ...  9  9  9]]
        # print(image.shape)  # (12000, 12000)
        # print(type(image))  # <class 'numpy.ndarray'>
        # print(type(image[0][0]))  # <class 'numpy.uint8'>

    all_pixels = image.shape[0] * image.shape[1]
    id_list = np.unique(image)

    pixels = pd.DataFrame(index=id_list, columns=['count', 'ratio'])
    for id in id_list:
        pixels.loc[id, 'count'] = np.count_nonzero(image == id)

    pixels['ratio'] = pixels['count'] / all_pixels

    print(f"pixels: {pixels}")
