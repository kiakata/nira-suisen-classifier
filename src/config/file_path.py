# GET BASE DIR PATH
import os
BASE_DIR_PATH = '/'.join(os.path.dirname(os.path.abspath(__file__)).split('/')[:-2])
del(os)

# data directory file path
# raw
RAW_DIR_PATH = BASE_DIR_PATH + '/data/raw'
RAW_NIRA_DIR_PATH = BASE_DIR_PATH + '/data/raw/nira'
RAW_SUISEN_DIR_PATH = BASE_DIR_PATH + '/data/raw/suisen'

# interim
INTERIM_DIR_PATH = BASE_DIR_PATH + '/data/interim'
INTERIM_NIRA_DIR_PATH = BASE_DIR_PATH + '/data/interim/nira'
INTERIM_SUISEN_DIR_PATH = BASE_DIR_PATH + '/data/interim/suisen'

# preprocessed
PREPROCESSED_DIR_PATH = BASE_DIR_PATH + '/data/preprocessed'
PREPROCESSED_TRAIN_DIR_PATH = BASE_DIR_PATH + '/data/preprocessed/train'
PREPROCESSED_TRAIN_NIRA_DIR_PATH = BASE_DIR_PATH + '/data/preprocessed/train/nira'
PREPROCESSED_TRAIN_SUISEN_DIR_PATH = BASE_DIR_PATH + '/data/preprocessed/train/suisen'
PREPROCESSED_VAL_DIR_PATH = BASE_DIR_PATH + '/data/preprocessed/val'
PREPROCESSED_VAL_NIRA_DIR_PATH = BASE_DIR_PATH + '/data/preprocessed/val/nira'
PREPROCESSED_VAL_SUISEN_DIR_PATH = BASE_DIR_PATH + '/data/preprocessed/val/suisen'
