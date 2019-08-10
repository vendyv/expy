#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 02:13:48 2019

@author: vendy
"""
import pyqrcode

def qrcode():
    q = pyqrcode.create('https://github.com/vendyv')
    q.png('gthb.png', scale=10)#, module_color=[0, 0, 0, 255], background=[0xff, 0xff, 0xcc])
    print("QR code generated")
    q.show()

if __name__ == "__main__":
    qrcode()
