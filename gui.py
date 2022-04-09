from importlib.resources import path
import tkinter as tk
import converter
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

isConverted = False
top = tk.Tk()
convertBtn = tk.Button(text="开始转换")
pathBtn = tk.Button(text="打开...")
curProcess = tk.Label()
folder2Convert = "./"

totalFileNum = 0
curCompleteFileNum = 0


def onConvertButtonClick(event):
    """转换按钮回调"""
    global isConverted

    print("按下了转换按钮 ", event)
    if(isConverted == False):
        isConverted = True
        converter.DecodeDatInPath(folder2Convert, onOneFileComplete)
        convertBtn.config(text="关闭")
        curProcess.config(text="转换完毕")
    else:
        top.quit()


def onOneFileComplete():
    """当每一个文件转换完成"""
    global curProcess
    global curCompleteFileNum
    global totalFileNum

    curCompleteFileNum += 1
    curProcess.config(text=str(curCompleteFileNum)+"/" + str(totalFileNum))
    top.update_idletasks()


def onPathBtnClick(event):
    """当指定路径按钮被点击"""
    global folder2Convert

    folder2Convert = fd.askdirectory(
        title='Open a file',
        initialdir='/',
    )
    totalFileNum = len(converter.GetFiles(folder2Convert))
    curProcess.config(text="待转换文件总数: "+str(totalFileNum))


def onGUI():
    """界面绘制"""
    global curProcess
    global totalFileNum
    global top

    top.geometry("200x100")
    top.title("微信dat文件转图片工具")

    pathBtn.bind("<Button-1>", onPathBtnClick)
    pathBtn.pack()

    curProcess = tk.Label(text="请指定一个路径")
    curProcess.pack()

    convertBtn.bind("<Button-1>", onConvertButtonClick)
    convertBtn.pack()

    top.mainloop()


onGUI()
