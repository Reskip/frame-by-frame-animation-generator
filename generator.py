# -*- coding: utf-8 -*-
# @Time    : 2020/10/13 16:26
# @Author  : reskip

import cv2
import os
import sys

import config

def getImageNameList():
    imageNames = os.listdir(config.INPUT_FOLDER)
    imageNames = filter(lambda name:
                        name.split(".")[-1] in config.ACCEPTABLE_TYPE,
                        imageNames)

    return sorted(imageNames, key=lambda name:
        int("".join(filter(lambda ch: ch.isdecimal(), name))))

def generate():
    videoWriter = cv2.VideoWriter(
        config.OUTPUT_FILE_NAME + ".mp4",
        cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
        config.FPS,
        config.SIZE)
    
    for name in getImageNameList():
        name = os.path.join(sys.path[0], config.INPUT_FOLDER, name)
        print("insert %s" % (name))
        img = cv2.imread(name)
        img = cv2.resize(img, config.SIZE)

        videoWriter.write(img)

    videoWriter.release()
