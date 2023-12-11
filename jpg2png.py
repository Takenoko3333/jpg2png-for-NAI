# Copyright © 2023 Takenoko
# Released under the MIT license
# https://opensource.org/licenses/mit-license.php

import glob
import os
from PIL import Image, ExifTags
from PIL.PngImagePlugin import PngInfo
from datetime import datetime
from pywintypes import Time

# Windowsの場合
on_windows = os.name == 'nt'
if on_windows:
    import win32file
    import win32con

# 画像形式
IMG_INPUT_FORMAT = 'JPEG'
IMG_OUTPUT_FORMAT = 'PNG'
# 画像拡張子
IMG_INPUT_FILENAME_EXT = 'jpg'
IMG_OUTPUT_FILENAME_EXT = 'png'
# ディレクトリ
INPUT_DIR = 'inputs/'
OUTPUT_DIR = 'outputs/'

# 画像を配列に格納
files = glob.glob(INPUT_DIR + '*.' + IMG_INPUT_FILENAME_EXT)

# 全画像の変換・保存
for file in files:
    file_name = os.path.splitext(os.path.basename(file))[0]
    output_file_name = file_name + '.' + IMG_OUTPUT_FILENAME_EXT
    output_file_path = OUTPUT_DIR + output_file_name
    output_file_abspath = os.path.abspath(OUTPUT_DIR + output_file_name)

    def get_user_comment(exif_data):
        user_comment_tag = None
        for tag, value in exif_data.items():
            if ExifTags.TAGS.get(tag) == 'UserComment':
                user_comment_tag = tag
                break

        if user_comment_tag:
            user_comment = exif_data[user_comment_tag]
            return user_comment

        return None

    def convert_jpg_to_png_with_pnginfo(file, output_file_path):
        # 画像を開く
        image = Image.open(file)

        # Exif情報を取得
        exif_data = image._getexif()

        # UserCommentを取得
        user_comment = get_user_comment(exif_data)

        # JPEGからPNGに変換
        image.save(output_file_path, format="PNG")

        # 画像を閉じる
        image.close()

        # PNGにメタデータを追加して保存
        png_info = PngInfo()
        if user_comment is not None:
            # UserCommentのデコードと不要文字削除
            decoded_text = user_comment.decode('utf-8').replace('\x00', '').replace("UNICODE", "")

            # PNG格納用メタデータの作成
            if 'Software: NovelAI' in decoded_text:
                # png2jpg改で変換したNovelAI生成画像の場合
                # コメントを改行(\n)で分割し項目毎にpnginfoに格納
                comment_lines = decoded_text.split('\n')
                for line in comment_lines:
                    key, value = line.split(': ', 1)
                    png_info.add_text(key, value)
            else:
                # NovelAI生成画像以外の場合（Automatic1111生成画像の場合)
                # コメントをpnginfoに格納
                png_info.add_text('parameters', decoded_text)

            # PNGを保存
            with Image.open(output_file_path) as png_image:
                png_image.save(output_file_path, pnginfo=png_info)

    # JPEGからPNGへ変換し、pnginfoを追加
    convert_jpg_to_png_with_pnginfo(file, output_file_path)

    # 日時情報を取得
    with Image.open(file):
        access_time   = os.path.getatime(file) # アクセス日時
        modify_time   = os.path.getmtime(file) # 更新日時

        if on_windows:
            creation_time = os.path.getctime(file) # 作成日時

    # 日付情報の設定
    # PNGファイルのハンドルを取得（Windowsのみ）
    if on_windows:
        handle = win32file.CreateFile(
            output_file_path,
            win32con.GENERIC_WRITE,
            win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
            None,
            win32con.OPEN_EXISTING,
            0,
            None
        )

        # JPEGファイルに元画像の作成日時、アクセス日時、更新日時を設定
        win32file.SetFileTime(handle, Time(creation_time), Time(access_time), Time(modify_time))

        # ハンドルを閉じる
        handle.Close()

    # 他のプラットフォームではアクセス日時と更新日時を設定
    os.utime(output_file_path, (access_time, modify_time))










