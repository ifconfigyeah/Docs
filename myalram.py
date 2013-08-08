# -*- coding:utf-8 -*-
import time
import sys

soundFile = 'sound.wav'
not_executed = 1
version = '0.3 beta'
playHour = 0
playMin  = 0
interval = 1              # 默认当前时间1小时后闹铃

def soundStart():
    if sys.platform[:5] == 'linux':
        import os
        os.popen2('aplay -q' + soundFile)
    elif sys.platform == 'win32':
        import winsound
        winsound.PlaySound(soundFile, winsound.SND_ASYNC)
        not_executed = 0
        time.sleep(60*2)               
        # 播放2分钟自动退出
        sys.exit()
#        winsound.PlaySound(soundFile, winsound.SND_PURGE)
#        winsound.PlaySound("SystemExit", SND_PURGE)
    else:
        print '\nWhat\'s operating system you used?'
        sys.exit()


def __init__(self):
    if sys.platform == 'darwin':
        print 'Mac OS X is not supported in current version', version
        sys.exit()


if __name__ == '__main__':
    
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
            print 'Hey buddy, Let\'s have a rest now!'
            soundStart()
       
        

