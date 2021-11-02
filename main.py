#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Author: Evil0ctal
# @Time: 2021/11/02
# @Update: 2021/11/02
# @Function: Another useless code

import requests
import json
import numpy as np
from matplotlib import pyplot as plt
import math


def get(url):
    try:
        i = lambda x: int(x ** 2)
        payload = json.dumps({'msg': i(22.80350850198276)})
        print(payload)
        r = requests.post(url, data=payload)
    except Exception:
        print("request failed")
    finally:
        pi = math.pi
        x = np.linspace(-3.3 ** 0.5, 3.3 ** 0.5, 6001).reshape(-1, 1)
        y = (x ** 2) ** (1 / 3) + 0.9 * np.sqrt(3.3 - x ** 2) * np.sin(40 * pi * x)
        plt.plot(x, y, color='r')
        plt.xlim(-3, 3)
        plt.show()


def main():
    target = [121, 111, 117, 114, 95, 104, 101, 97, 114, 116]
    temp = [chr(target[i]) for i in range(len(target))]
    url = ("".join(temp))
    get(url)


if __name__ == "__main__":
    main()
