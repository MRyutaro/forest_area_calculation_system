import glob
import os
import re

if __name__ == "__main__":
    dir_path = r"data\JAXA_HRLULC_Japan_v23.12"

    # ファイルの一覧を取得する
    tiff_files_path = glob.glob(os.path.join(dir_path, "*.tif"))
    # print(f"tiff_files_path: {tiff_files_path}")

    # ファイル名の一覧を取得する
    tiff_files_name = [os.path.basename(tiff_file_path) for tiff_file_path in tiff_files_path]
    # print(f"tiff_files_name: {tiff_files_name}")

    north_latitudes = []
    east_longitudes = []

    # LC_N34E135.tifについて、正規表現を使って34と135を取得する
    pattern = r"LC_N(\d+)E(\d+).tif"
    for tiff_file_name in tiff_files_name:
        m = re.match(pattern, tiff_file_name)
        if m:
            north_latitude = m.group(1)
            east_longitude = m.group(2)
            # print(f"tiff_file_name: {tiff_file_name}, 北緯{north_latitude}度, 東経{east_longitude}度")

            north_latitudes.append(north_latitude)
            east_longitudes.append(east_longitude)

    # ソート
    min_north_latitude = min(north_latitudes)
    max_north_latitude = max(north_latitudes)
    min_east_longitude = min(east_longitudes)
    max_east_longitude = max(east_longitudes)

    print(f"min_north_latitude: {min_north_latitude}")
    print(f"max_north_latitude: {max_north_latitude}")
    print(f"min_east_longitude: {min_east_longitude}")
    print(f"max_east_longitude: {max_east_longitude}")
