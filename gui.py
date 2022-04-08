import tkinter as tk
import converter

isConverted = False
top = tk.Tk()
convertBtn = tk.Button(text="开始转换")
curProcess = tk.Label()

totalFileNum = 0
curCompleteFileNum = 0

# 转换按键回调
def onConvertButtonClick(event):
    global isConverted

    print("按下了转换按钮 ", event)
    if(isConverted == False):
        isConverted = True
        converter.DecodeDatInCurPath(onOneFileComplete)
        convertBtn.config(text="关闭")
        curProcess.config(text="转换完毕")
    else:
        top.destroy()

# 当一个文件转换完成 - 用于更新进度条
def onOneFileComplete():
    global curProcess
    global curCompleteFileNum
    global totalFileNum

    curCompleteFileNum += 1
    curProcess.config(text=str(curCompleteFileNum)+"/" + str(totalFileNum))
    top.update_idletasks()

# 界面绘制
def onGUI():
    global curProcess
    global totalFileNum
    global top

    top.geometry("200x100")
    top.title("微信dat文件转图片工具")

    totalFileNum = len(converter.GetFiles(converter.output_path))
    curProcess = tk.Label(text="待转换文件总数: "+str(totalFileNum))
    curProcess.pack()

    convertBtn.bind("<Button-1>", onConvertButtonClick)
    convertBtn.pack()

    top.mainloop()


onGUI()
