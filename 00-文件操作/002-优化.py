"""
encoding : utf-8
author : xjz
date : 2021-12-14
purpose :
1、判读文件夹名是否存在
2、存在则返回“该文件夹已存在”，否则开始创建文件夹
"""
import os
import time


year = time.strftime('%Y', time.localtime(time.time()))  # 获取当前年份作为文件名

big_month = [1, 3, 5, 7, 8, 10, 12]    # 大月
small_month = [4, 6, 9, 11]   # 小月


try:
    os.mkdir(r'D:\\' + year)
except OSError:
    print("该文件已存在！")






