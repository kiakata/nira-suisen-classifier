# coding: utf-8
"""
このファイルは、なんのために存在しているか
"""
import os
import numpy as np
from PIL import Image

# local
from config import file_path


def resize(raw_path, interim_path):
    for file_name in os.listdir(raw_path):
        img = Image.open(os.path.join(raw_path,
                                      file_name))
        np_img = np.array(img)
        print('-' * 30)
        print('-' * 10 + 'resize前' + '-' * 10)
        print(np_img.dtype)
        print(np_img.ndim)
        print(np_img.shape)

        img_resize = img.resize((256, 256))
        np_img = np.array(img_resize)
        print('-' * 10 + 'resize後' + '-' * 10)
        print(np_img.dtype)
        print(np_img.ndim)
        print(np_img.shape)

        try:
            if img_resize.mode != 'RGB':
                img_resize = img_resize.convert('RGB')
            img_resize.save(os.path.join(interim_path,
                                         file_name))
        except IOError:
            print('cannot convert'.format(infile))


def main():
    """
    この関数はどんな処理をするのか

    Parameters
    --------
        sample : pandas DataFrame
            sampleのデータ

    Returns
    --------
        sample : pandas DataFrame
            結果を返す
    """
    resize(file_path.RAW_NIRA_DIR_PATH, file_path.RAW_SUISEN_DIR_PATH)
    resize(file_path.INTERIM_NIRA_DIR_PATH, file_path.INTERIM_SUISEN_DIR_PATH)


if __name__ == '__main__':
    main()
