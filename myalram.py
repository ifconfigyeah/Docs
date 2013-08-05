# -*- coding:utf-8 -*-
import time
import sys

soundFile = 'sound.wav'
not_executed = 1
version = '0.2 beta'
playHour = 0
playMin  = 0
interval = 1              # 默认1小时后闹铃

def soundStart():
    if sys.platform[:5] == 'linux':
        import os
        os.popen2('aplay -q' + soundFile)
    else:
        import winsound
        winsound.PlaySound(soundFile, winsound.SND_ASYNC)
        not_executed = 0
        time.sleep(60)                     # 播放闹铃一分钟后自动停止
#        winsound.PlaySound(soundFile, winsound.SND_PURGE)
        winsound.PlaySound("SystemExit", SND_PURGE)

if __name__ == '__main__':
    if sys.platform == 'darwin':
        print 'Mac OS X is not supported in current version', version
        exit()
    else:
        ct = list(time.localtime())
        curHour  = ct[3]
        curMin   = ct[4]

        playHour = curHour + interval 
        if playHour == 24:
            playhour = 0

        playMin  = curMin
        if playMin == 60:
            playHour = playHour + 1
            playMin  = 0

        print 'Alarm time is', playHour, ':', playMin

while(not_executed):
    dt = list(time.localtime())
    if dt[3] == playHour and dt[4] == playMin:
        soundStart()
       
        

