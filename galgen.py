#!/usr/bin/python3

import argparse
import os
import datetime

from PIL import Image
from PIL.ExifTags import TAGS

from lib import html_tmpl

def exif(info):
    if info is None:
        return {}

    myTags = ['ISOSpeedRatings', 'Model', 'LensModel', 'FocalLength',
            'DateTime', 'ExposureTime', 'Orientation']
    ret = {}

    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        if decoded in myTags:
            ret[decoded] = value

    return ret

def is_image(i):
    if not i.name.startswith('.') \
        and i.is_file() \
        and i.name.lower().endswith('jpg'):
            return True
    else:
        return False

def thumber(directory, gallery_dir):
    THUMB_SIZE = (1152, 864)

    d = os.scandir(directory)
    images = [(i.name, i.path) for i in d if is_image(i)]

    thumbed = []

    for image in images:
        file, ext = os.path.splitext(image[0])
        thumb = file + '_thumb.jpg'

        im = Image.open(image[1])

        im_cp = im.copy()
        im_cp.save(os.path.join(gallery_dir, file+'.jpg'), "JPEG")

        info = exif(im._getexif())
        path = os.path.join(gallery_dir, thumb)

        im.thumbnail(THUMB_SIZE, Image.ANTIALIAS)
        o = info.get('Orientation', -1)
        if o == 8:
            log('flip', 'Rotate 90 deg cw.')
            im = im.rotate(90)

        im.save(path, "JPEG")

        thumbed.append((image[0], thumb, info))
        log('thumb', 'Created thumbnail for "{}"..'.format(file))

        return thumbed
 
def log(label='LOG', msg=''):
    ts = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    print('['+ts+'] ['+label.upper()+'] ' + msg)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', 
            help='directory to turn into a site')

    args = parser.parse_args()
    
    if args.directory:
        directory = args.directory
    else:
        directory = os.getcwd()

    gallery_dir = os.path.join(directory, 'gal')
    os.makedirs(gallery_dir, exist_ok=True)

    thumbed = thumber(directory, gallery_dir)

    with open(os.path.join(gallery_dir, 'index.html'), 'w') as index:
        log('shit', 'Write the document')
        index.write(html_tmpl.build_doc(directory, thumbed))

    log('SUCCESS', '... Done!')
