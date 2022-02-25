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


class MkdirFiles(object):
    def __init__(self, year_path):
        self.year_path = year_path   # 存放年份文件夹路径

    def create_year(self):
        try:
            os.mkdir(self.year_path + year)
        except OSError:
            print("该文件已存在！")

    @staticmethod
    def create_files(path):
        big_month = [1, 3, 5, 7, 8, 10, 12]
        small_month = [4, 6, 9, 11]
        for i in range(1, 5):
            if i == 1:
                os.mkdir(path + "第{}季度".format(i))
                for j in range(1, 4):
                    os.mkdir(path + "第{}季度".format(i) + r'\\' + "{}月".format(j))
                    if j in big_month:
                        for k in range(1, 32):
                            os.mkdir(path + "第{}季度".format(i) + r'\\' + "{}月".format(j) + r'\\' + '{}日'.format(k))
                    elif j in small_month:
                        for k in range(1, 31):
                            os.mkdir(path + "第{}季度".format(i) + r'\\' + "{}月".format(j) + r'\\' + '{}日'.format(k))
                    else:
                        if int(year) % 4 == 0:
                            for k in range(1, 29):
                                os.mkdir(path + "第{}季度".format(i) + r'\\' + "{}月".format(j) + r'\\' + '{}日'.format(k))
                        elif int(year) % 4 != 0:
                            for k in range(1, 30):
                                os.mkdir(path + "第{}季度".format(i) + r'\\' + "{}月".format(j) + r'\\' + '{}日'.format(k))
            elif i == 2:
                os.mkdir(path + "第{}季度".format(i))
                for j in range(4, 7):
                    os.mkdir(path + "第{}季度".format(i) + r'\\' + "{}月".format(j))
                    if j in big_month:
                        for k in range(1, 32):
                            os.mkdir(path + "第{}季度".format(i) + r'\\' + "{}月".format(j) + r'\\' + '{}日'.format(k))
                    elif j in small_month:
                        for k in range(1, 31):
                            os.mkdir(path + "第{}季度".format(i) + r'\\' + "{}月".format(j) + r'\\' + '{}日'.format(k))
            elif i == 3:
                os.mkdir(path + "第{}季度".format(i))
                for j in range(7, 10):
                    os.mkdir(path + "第{}季度".format(i) + r'\\' + "{}月".format(j))
                    if j in big_month:
                        for k in range(1, 32):
                            os.mkdir(path + "第{}季度".format(i) + r'\\' + "{}月".format(j) + r'\\' + '{}日'.format(k))
                    elif j in small_month:
                        for k in range(1, 31):
                            os.mkdir(path + "第{}季度".format(i) + r'\\' + "{}月".format(j) + r'\\' + '{}日'.format(k))
            elif i == 4:
                os.mkdir(path + "第{}季度".format(i))
                for j in range(10, 13):
                    os.mkdir(path + "第{}季度".format(i) + r'\\' + "{}月".format(j))
                    if j in big_month:
                        for k in range(1, 32):
                            os.mkdir(path + "第{}季度".format(i) + r'\\' + "{}月".format(j) + r'\\' + '{}日'.format(k))
                    elif j in small_month:
                        for k in range(1, 31):
                            os.mkdir(path + "第{}季度".format(i) + r'\\' + "{}月".format(j) + r'\\' + '{}日'.format(k))


if __name__ == '__main__':
    xjz = MkdirFiles(r'D:\\')
    xjz.create_year()
    xjz.create_files(r'D:\\' + year + r'\\')

