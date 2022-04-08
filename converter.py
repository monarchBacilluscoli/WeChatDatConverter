# 将微信的dat格式文件转换为图片文件

import os

output_path = "./"

# 得到路径下所有的dat文件
def GetFiles(path):
    files = os.listdir(path)
    file_list = []
    for file in files:
        filename, extension = os.path.splitext(file)
        if os.path.isfile(os.path.join(path, file)) and extension == ".dat":
            file_list.append(os.path.join(path, file))
    return file_list

# 单个文件转换
def imageDecode(f, fn):
    dat = open(f, "rb")
    out = output_path + fn + ".png"
    png = open(out, "wb")
    for now in dat:
        for nowByte in now:
            #todo 自动计算该值
            newByte = nowByte ^ 0x5D  # 注意将这里的二进制数改成dat格式开头的4个16进制值和jpeg格式开头的FF D8的亦或结果的前两个
            png.write(bytes([newByte]))
    dat.close()
    png.close()

# 转换全部文件
def DecodeDatInCurPath(onOneFileComplete):
    # 遍历当前文件夹下的所有文件
    files = GetFiles(output_path)
    # 对所有文件调用imageDecode
    for file in files:
        print("处理中："+file)
        imageDecode(file, os.path.basename(file))
        onOneFileComplete()
