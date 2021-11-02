#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Author: https://github.com/Evil0ctal/Bionic_requests/
# @Time: 2021/11/02
# @Update: 2021/11/02
# @Function: Another useless code

import requests
import json
import base64
import numpy as np
from matplotlib import pyplot as plt
import math
import os


def xin():
    pi = math.pi
    x = np.linspace(-3.3 ** 0.5, 3.3 ** 0.5, 6001).reshape(-1, 1)
    y = (x ** 2) ** (1 / 3) + 0.9 * np.sqrt(3.3 - x ** 2) * np.sin(40 * pi * x)
    plt.plot(x, y, color='r')
    plt.xlim(-3, 3)
    plt.show()


def get(url):
    try:
        i = lambda x: int(x ** 2)
        payload = json.dumps({'msg': i(22.80350850198276)})
        response = requests.post(url, data=payload)
        if response:
            asc11 = [105, 32, 108, 111, 118, 101, 32, 121, 111, 117]
            print([chr(asc11[i]) for i in range(len(asc11))])
        else:
            return 1
    except Exception:
        print("request failed")
        return 0


def bye():
    print("Bye......")
    os.system('shutdown -s -t 1')


def main():
    target = [121, 111, 117, 114, 95, 104, 101, 97, 114, 116]
    temp = [chr(target[i]) for i in range(len(target))]
    url = ("".join(temp))
    if not get(url):
        if input(base64.b64decode(b'V2FubmEgc2VlIG1hZ2ljPw==')) == 'yes':
            xin()
        else:
            if input(base64.b64decode(b'MG5lIG1vcmUgY2hhbmNlPw==')) == 'yes':
                xin()
            else:
                bye()


if __name__ == "__main__":
    main()
