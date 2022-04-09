# 将微信的dat格式文件转换为图片文件

from ast import Str
import os
from re import I

g_output_path = "./"


def GetFiles(path):
    """得到所有待转换文件"""
    files = os.listdir(path)
    file_list = []
    for file in files:
        filename, extension = os.path.splitext(file)
        if os.path.isfile(os.path.join(path, file)) and extension == ".dat":
            file_list.append(os.path.join(path, file))
    return file_list


def imageDecode(f, fn):
    """转换单个文件到当前路径"""
    imageDecode(f, fn, g_output_path)


def imageDecode(f, fn, exportFolder):
    """转换单个文件到指定路径"""
    assert isinstance(exportFolder, str)
    dat = open(f, "rb")
    if not exportFolder.endswith("/"):
        exportFolder += "/"
    out = exportFolder + fn + ".png"
    png = open(out, "wb")
    for now in dat:
        for nowByte in now:
            # todo 自动计算该值
            newByte = nowByte ^ 0x5D  # 注意将这里的二进制数改成dat格式开头的4个16进制值和jpeg格式开头的FF D8的亦或结果的前两个
            png.write(bytes([newByte]))
    dat.close()
    png.close()


def DecodeDatInCurPath(onOneFileComplete):
    """转换当前路径下所有文件"""
    DecodeDatInPath(g_output_path, onOneFileComplete)


def DecodeDatInPath(folderPath, onEachFileComplete):
    """ 转换指定路径下所有文件"""
    # 遍历当前文件夹下的所有文件
    files = GetFiles(folderPath)
    # 对所有文件调用imageDecode
    for file in files:
        imageDecode(file, os.path.basename(file), folderPath)
        print("处理完毕："+file)
        onEachFileComplete()
