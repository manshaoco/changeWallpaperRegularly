# ChangeWallpaperRegularly
import os
import time
import ctypes
import schedule

def errorAndExit(title,tips):
    ctypes.windll.user32.MessageBoxA(0,tips.encode('gb2312'),title.encode('utf-8'),0)
    exit()

def readCSV(filePath):
    csvFile = open(filePath,encoding='utf-8')
    csvList = []
    for line in csvFile:
        line = line.replace("\n","")
        csvList.append(line.split(","))
    csvFile.close()
    return csvList

def changeWallpaperTo(wallpaperPath):
    ctypes.windll.user32.SystemParametersInfoW(20,0,nowFolderPath+wallpaperPath,0)
    return True

# 读取配置文件中的时间和壁纸文件名
if not os.path.exists('config.csv'):
    errorAndExit("Error","配置文件不存在！请按照要求重新创建配置文件！")
timeSet = []
wallpaperPath = []
configList = readCSV('config.csv')
for i in range(1,len(configList)):
    timeSet.append(configList[i][0])
    wallpaperPath.append(configList[i][1])

# 获取当前文件夹路径
nowFolderPath = os.getcwd() + "\\"

# 程序启动后，检查时间更换壁纸
nowTime = time.strftime("%H:%M",time.localtime())
for i in range(len(timeSet)+1):
    if nowTime < timeSet[0]:
        changeWallpaperTo(wallpaperPath[-1])
    elif nowTime > timeSet[-1]:
        changeWallpaperTo(wallpaperPath[-1])
    else:
        changeWallpaperTo(wallpaperPath[i-1])

# 设置定时任务更换壁纸
for i in range(len(timeSet)):
    schedule.every().day.at(timeSet[i]).do(changeWallpaperTo,wallpaperPath[i])

# 程序保持运行的代码
while True:
    schedule.run_pending()
    time.sleep(1)