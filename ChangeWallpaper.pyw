# ChangeWallpaperRegularly
import schedule
# 需手动使用 pip install schedule 安装该第三方库
import ctypes
import time
import os

# 参数区
t0 = "05:30"
t1 = "08:30"
t2 = "10:30"
t3 = "13:30"
t4 = "16:30"
t5 = "18:30"
# 结束参数区

nowFolderPath = os.getcwd() + "\\"

def changeWallpaperTo0():
    # 更换第0张壁纸
    selectPath = "0.png"
    ctypes.windll.user32.SystemParametersInfoW(20,0,nowFolderPath+selectPath,0)
    return 0
def changeWallpaperTo1():
    # 更换第1张壁纸
    selectPath = "1.png"
    ctypes.windll.user32.SystemParametersInfoW(20,0,nowFolderPath+selectPath,0)
    return 0
def changeWallpaperTo2():
    # 更换第2张壁纸
    selectPath = "2.png"
    ctypes.windll.user32.SystemParametersInfoW(20,0,nowFolderPath+selectPath,0)
    return 0
def changeWallpaperTo3():
    # 更换第3张壁纸
    selectPath = "3.png"
    ctypes.windll.user32.SystemParametersInfoW(20,0,nowFolderPath+selectPath,0)
    return 0
def changeWallpaperTo4():
    # 更换第4张壁纸
    selectPath = "4.png"
    ctypes.windll.user32.SystemParametersInfoW(20,0,nowFolderPath+selectPath,0)
    return 0
def changeWallpaperTo5():
    # 更换第5张壁纸
    selectPath = "5.png"
    ctypes.windll.user32.SystemParametersInfoW(20,0,nowFolderPath+selectPath,0)
    return 0

nowTime = time.strftime("%H:%M",time.localtime())
if nowTime < t0:  # 说明在第0个时间之前
    changeWallpaperTo5()
elif nowTime < t1:
    changeWallpaperTo0()
elif nowTime < t2:
    changeWallpaperTo1()
elif nowTime < t3:
    changeWallpaperTo2()
elif nowTime < t4:
    changeWallpaperTo3()
elif nowTime < t5:
    changeWallpaperTo4()
else:
    changeWallpaperTo5()

schedule.every().day.at(t0).do(changeWallpaperTo0)
schedule.every().day.at(t1).do(changeWallpaperTo1)
schedule.every().day.at(t2).do(changeWallpaperTo2)
schedule.every().day.at(t3).do(changeWallpaperTo3)
schedule.every().day.at(t4).do(changeWallpaperTo4)
schedule.every().day.at(t5).do(changeWallpaperTo5)

while True:
    schedule.run_pending()
    time.sleep(1)