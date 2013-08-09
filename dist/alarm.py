# coding:utf-8

import time
import sys

# a '.wav' file u want to play
soundFilePath  = 'alarm.wav'   

# Sounds for 120 seconds
longOfAlarm = 120       



# THE FOLLOWING PARAMETERS SHOULD NOT MODIFY
VERSION  = 1.0
TIP      = True
PLAYHOUR = 0
PLAYMIN  = 0

# END


def __init__(self):
    # Initialization
    pass


def echoAlarm():
    print 'Your Alarm Time is', PLAYHOUR, ':', PLAYMIN


def playSound():
    # make sure support current OS
    pf = sys.platform
    if pf == 'win32':
        import winsound
        # use 'winsound' lib to play arlam music on windows
        winsound.PlaySound(soundFilePath, winsound.SND_ASYNC)
        time.sleep(longOfAlarm)
        sys.exit()

    elif pf == 'linux':
        import os
        os.popen2('aplay -q' + soundFile)
        # linux may used 'os' lib to play
        time.sleep(longOfAlarm)
        sys.exit()

    elif pf == 'drawin':
        print 'Mac OS X is not supported in current version', VERSION  #mpg123
    else:
        print 'What operating system are you used?'

    sys.exit()


def clacAndSetAlarmTime(tType, tTime):

    global PLAYHOUR, PLAYMIN
    curHour = list(time.localtime())[3]
    curMin  = list(time.localtime())[4]

    if tType == 'h':
        tTime = int(tTime)
        if not 1 <= tTime <= 23:
            print 'Your hours argument is too big.'
            sys.exit()
        else:
            PLAYHOUR = curHour + tTime
            PLAYMIN  = curMin
            if PLAYHOUR == 24: PLAYHOUR = 0
            if PLAYHOUR > 24: PLAYHOUR = PLAYHOUR - 24
        echoAlarm()

    elif tType == 'm':
        tTime   = int(tTime)
        if not 0 < tTime <=59:
            print 'Your mins argument should between 1 and 59.'
            sys.exit()
        else:
            PLAYHOUR = curHour
            PLAYMIN = curMin + tTime
            if PLAYMIN == 60:
                PLAYMIN == 0
                PLAYHOUR = PLAYHOUR + 1
            if PLAYMIN > 60:
                PLAYMIN = PLAYMIN - 60
                PLAYHOUR = PLAYHOUR + 1
        echoAlarm()

    else:
        PLAYHOUR, PLAYMIN = tTime.split(':')
        PLAYHOUR = int(PLAYHOUR)
        PLAYMIN  = int(PLAYMIN)

        if (not 0 <= PLAYHOUR <= 23) or (not 0 <= PLAYMIN <= 59):
            print 'Error Time Arguments.'
            sys.exit()

        echoAlarm()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'No action specified.'
        sys.exit()

    if sys.argv[1].startswith('-') or sys.argv[1].startswith('/'):
        option = sys.argv[1][1:]
        if option == 'version':
            print 'version', VERSION
        elif option == 'help' or option == '-help' or option == '?':
            print '''\
This program will play a '.wav' file within the specified time.
The following arguments can be used.
Options include:
  --version : Prints the version number
  --help    : Display this help

How To Use (One argument limited):
  alarm.py [h][m][d]
  -h        : How many hours later to be alaram
  -m        : How many minutes later to be alram
  -d        : Use a special time to alram
  Example:
  alarm.py -h 1	     Alarm in one hours later
  alarm.py -m 45     Alarm in 45 minutes later
  alarm.py -d 15:46  Timetables depend on 24H
  '''
            sys.exit()
        elif (option == 'h' or option == 'm' or option == 'd') and len(sys.argv[2]) != 0:
            clacAndSetAlarmTime(option, sys.argv[2])
    else:
        print 'Unknow option.'
        sys.exit()

    while(TIP):
        dt = list(time.localtime())
        if dt[3] == PLAYHOUR and dt[4] == PLAYMIN:
            print 'Hey buddy, Let\'s have a rest!'
            playSound()
  
    





