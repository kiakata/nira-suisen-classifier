# coding: utf-8
import os

# local
from config import file_path


def rename(dir_path):
    for i, file_name in enumerate(os.listdir(dir_path)):
        os.rename(os.path.join(dir_path, file_name),
                  os.path.join(dir_path, "{0:04d}.jpg".format(i)))


def main():
    rename(file_path.RAW_NIRA_DIR_PATH)
    rename(file_path.RAW_SUISEN_DIR_PATH)


if __name__ == '__main__':
    main()
