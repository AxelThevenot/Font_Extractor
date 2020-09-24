import os
import glob

import warnings
warnings.filterwarnings("ignore")

import re

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


FONT_IMAGES_FOLDER_PATH = 'font_images'
FONT_IMAGES_PATTERN = '{*}_{*}.png'
REGEX_METADATA = '/\{(?P<font_name>.*)\}_\{(?P<chars>.*)\}.png'

FONT_EXTRACTED_FOLDER_PATH = 'font_extracted'

CHAR_SIZE = (64, 128)


def extract_meta_from_path(path, regex_meta):
    r = re.compile(regex_meta)
    m = r.search(path)
    groups = m.groupdict() if m is not None else {}
    # sanity check
    if 'font_name' not in groups.keys() or 'chars' not in groups.keys():
        print('The name does not respect the format {font_name}_{chars}.png')
        raise RuntimeError
    return groups['font_name'], groups['chars']


def get_font_images(path, pattern, regex_meta):
    pattern_path = os.path.join(path, pattern)
    font_images_paths = glob.glob(pattern_path)
    images = []
    for font_path_img in font_images_paths:
        font_name, chars = extract_meta_from_path(font_path_img, regex_meta)
        img = plt.imread(font_path_img)
        images.append({
            'font_name':font_name,
            'chars':chars,
            'img':img
        })

    return images

def white_to_transparency(img):
    x = np.asarray(img.convert('RGBA')).copy()

    x[:, :, 3] = (255 * (x[:, :, :3] < 16).any(axis=2)).astype(np.uint8)

    return Image.fromarray(x)


def extract_char_images(path, images, char_size):

    for img in images:
        font_path = os.path.join(path, img['font_name'])
        # create folder if not exists
        if not os.path.exists(font_path):
            os.makedirs(font_path)

        # get last index where the char stop
        _, y, _ = np.where(img['img'] == 0)


        last_idx = np.max(y) + 1
        steps = np.linspace(0, last_idx, len(img['chars']) + 1).astype(np.int)

        for start, stop, c in zip(steps[:-1], steps[1:], img['chars']):
            char_path = os.path.join(font_path, f'[{c}].png')
            print(c)
            char_img = (img['img'][:, start:stop] * 255).astype(np.uint8)

            char_img = Image.fromarray(char_img)
            char_img = char_img.resize(char_size)
            char_img = white_to_transparency(char_img)
            char_img.save(char_path)




if __name__ == '__main__':
    images = get_font_images(FONT_IMAGES_FOLDER_PATH, FONT_IMAGES_PATTERN, REGEX_METADATA)
    extract_char_images(FONT_EXTRACTED_FOLDER_PATH, images, CHAR_SIZE)
