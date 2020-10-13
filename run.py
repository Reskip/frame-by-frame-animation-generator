# -*- coding: utf-8 -*-
# @Time    : 2020/10/13 16:26
# @Author  : reskip

import os
import sys

def checkDeps():
    try:
        from generator import generate
    except:
        print("Start Install OpenCV")
        os.system("python -m pip install opencv-python")

if __name__ == "__main__":
    checkDeps()
    from generator import generate
    generate()
