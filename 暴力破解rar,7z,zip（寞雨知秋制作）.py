import itertools  #排列组合
import zipfile
import os
import py7zr
from threading import Thread
from unrar import rarfile
#导入模块，它是做压缩和解压缩的
#made by 寞雨知秋~

def jiejue(n):
    mima = "0123456789abcdefghijklmnopqrstuvwxyz"#可能的字符
    result = itertools.product(mima, repeat=n)  
    if not os.path.isfile("暴力破解%s.txt"%str(n)):
        book = open("暴力破解%s.txt"%str(n), "w+")
        for i in result:
            book.write("".join(i) + "\n")

        book.close()
#print(os.path.join(os.getcwd(),'123.zip'))

def moyu(min,max,zip_name):#zip
    # 暴力破解
    m = 0
    zfile = zipfile.ZipFile(zip_name)
    for i in range(min, max):
        keneng = 36 ** i
        jiejue(i)
        passfile = open("暴力破解%s.txt" % str(i))
        for line in passfile.readlines():
            try:
                password = line.strip("\n")
                zfile.extractall(path=os.getcwd(),pwd=password.encode('utf-8'))
                print("密码是：" + password)
                break
            except:
                m += 1
                print("密码尝试错误,当前进度：%s/" % str(m) + str(keneng))
def mogou(min,max,zip_name):#7z
    m = 0
    for i in range(min, max):
        keneng = 36 ** i
        jiejue(i)
        passfile = open("暴力破解%s.txt" % str(i))
        for line in passfile.readlines():
            try:
                pwd = line.strip("\n")
                archive = py7zr.SevenZipFile(zip_name, mode='r', password=pwd)
                print("密码是：" + pwd)
                archive.extractall()
                archive.close()
                break
            except:
                m += 1
                print("密码尝试错误,当前进度：%s/" % str(m) + str(keneng))
def moniao(min,max,zip_name):#rar
    m = 0
    zfile = rarfile.RarFile(zip_name)
    for i in range(min, max):
        keneng = 36 ** i
        jiejue(i)
        passfile = open("暴力破解%s.txt" % str(i))
        for line in passfile.readlines():
            try:
                password = line.strip("\n")
                zfile.extractall(path=os.getcwd(),pwd=password)
                print("密码是：" + password)
                break
            except:
                m += 1
                print("密码尝试错误,当前进度：%s/" % str(m) + str(keneng))
if __name__ == "__main__":
    print("请输入文件名，包含后缀")
    zip_name = input()
    print('请输入密码长度（大致估计）例如：（1，5）为1到4（不包含右边）') #用户输入文件名称，和密码位数
    lenth = input()
    start = 0
    for i in range(0, len(lenth)):
        if lenth[i].isdigit():
            start = i
            break
    try:
        mid = lenth.index(",")
    except:
        mid = lenth.index("，")
    end = 0
    for j in range(len(lenth) - 1, 0, -1):
        if lenth[j].isdigit():
            end = j
            break
    min = int(lenth[start:mid])  # min为第一个数字)
    max = int(lenth[mid + 1:end + 1])  # maxw为第二个数字)
    f = 0
    dianhao = zip_name.index(".")
    leixin = zip_name[dianhao + 1:]
    print(start, min, max, leixin)
    if leixin == "zip":# 自动辨别文件类型
        t1 = Thread(target=moyu, args=(min, max, zip_name))
        t1.start()
    elif leixin == "7z":
        t2 = Thread(target=mogou, args=(min, max, zip_name))
        t2.start()  # 太鸡儿慢了
    elif leixin == "rar":
        t3 = Thread(target=moniao, args=(min, max, zip_name))
        t3.start()

    # file = zipfile.ZipFile("123.zip")
    # zfile.extractall(path=os.getcwd(),members=zfile.namelist(),pwd=password.encode('utf-8'))
    #下一步的优化方向 ： 多线程！！！加快破解速度
