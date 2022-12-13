import os
import glob


def clean_folders(*args):

    folders = list(args)

    for folder in folders:
        files = glob.glob(f'{folder}/*')
        for file in files:
            os.remove(file)

