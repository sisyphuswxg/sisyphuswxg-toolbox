#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import subprocess


from date_and_time import stamp2time, time2stamp


WORK_MINUTES = 25
BREAK_MINUTES = 5


def main():
    try:
        if len(sys.argv) <= 2:
            help()
            # print(f'🍅 tomato {WORK_MINUTES} minutes. Ctrl+C to exit')
            # tomato(WORK_MINUTES, 'It is time to take a break')
            # print(f'🛀 break {BREAK_MINUTES} minutes. Ctrl+C to exit')
            # tomato(BREAK_MINUTES, 'It is time to work')

        elif sys.argv[1] == 'timestamp2':
            time_stamp = sys.argv[2]
            print("timestamp => time")
            stamp2time(time_stamp)

        elif sys.argv[1] == '2timestamp':
            time_str = sys.argv[2]
            print("time => timestamp")
            time2stamp(time_str)

        elif sys.argv[1] == '-h':
            help()

        else:
            help()

    except KeyboardInterrupt:
        print('\n👋 goodbye')
    except Exception as ex:
        print(ex)
        exit(1)


def tomato(minutes, notify_msg):
    start_time = time.perf_counter()
    while True:
        diff_seconds = int(round(time.perf_counter() - start_time))
        left_seconds = minutes * 60 - diff_seconds
        if left_seconds <= 0:
            print('')
            break

        countdown = '{}:{} ⏰'.format(int(left_seconds / 60), int(left_seconds % 60))
        duration = min(minutes, 25)
        progressbar(diff_seconds, minutes * 60, duration, countdown)
        time.sleep(1)

    notify_me(notify_msg)


def progressbar(curr, total, duration=10, extra=''):
    frac = curr / total
    filled = round(frac * duration)
    print('\r', '🍅' * filled + '--' * (duration - filled), '[{:.0%}]'.format(frac), extra, end='')


def notify_me(msg):
    '''
    # macos desktop notification
    terminal-notifier -> https://github.com/julienXX/terminal-notifier#download
    terminal-notifier -message <msg>

    # ubuntu desktop notification
    notify-send

    # voice notification
    say -v <lang> <msg>
    lang options:
    - Daniel:       British English
    - Ting-Ting:    Mandarin
    - Sin-ji:       Cantonese
    '''

    print(msg)
    try:
        if sys.platform == 'darwin':
            # macos desktop notification
            subprocess.run(['terminal-notifier', '-title', '🍅', '-message', msg])
            subprocess.run(['say', '-v', 'Daniel', msg])
        elif sys.platform.startswith('linux'):
            # ubuntu desktop notification
            subprocess.Popen(["notify-send", '🍅', msg])
        else:
            # windows?
            # TODO: windows notification
            pass

    except:
        # skip the notification error
        pass


def help():
    appname = sys.argv[0]
    appname = appname if appname.endswith('.py') else 'sisyphuswxg'  # sisyphuswxg is pypi package
    print(f"====== 🧰 SISYPHUSWXG's ToolBox =======\n")
    print(f"📍2timestamp")
    print(f'  {appname} timestamp2 1557502800             # timestamp -> time')
    print()
    print(f"📍time2stamp")
    print(f'  {appname} 2timestamp "2019-05-10 15:40:00"   # time-> timestamp')
    print()


if __name__ == "__main__":
    main()
