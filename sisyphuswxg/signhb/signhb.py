#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import datetime
import time


class Signhb:

    def get_pins(self):
        with open('./pins.txt', 'r', encoding='utf-8') as f:
            pins = f.readlines()
        # pins = ['jd_4551ecddf601a\n', 'jd_IOgAyBPGWIIo\n', 'jd_betyDLWUoBmc\n', 'jd_qlWSyHhTBqGK']
        print('[pins]\n  ' + '  '.join(pins) + '\n')
        # return '[pins]\n  ' + '  '.join(pins) + '\n'

    def del_sign(self, pin, pp_flag):
        if not pp_flag:
            text = f"🧧del\n" \
                   f"./redistool del510 {pin}; ./redistool del510_signhb_jimdb {pin};\n"
        else:
            text = f"💰del\n" \
                   f"./redistool del510_signhb_jimdb_jxpp {pin};\n\n"
        print(text)

    def query_sign(self, pin, pp_flag):
        if not pp_flag:
            text = f"🧧query\n" \
                   f"./redistool query_signhb {pin};./redistool query_signhb_jimdb {pin};\n"
        else:
            text = f"💰query\n" \
                   f"[TODO]\n\n"
        print(text)
        # return text

    def add_sign(self, pin, continue_days, pp_flag):
        now_timestamp = int(time.time())
        today_date = datetime.date.today()

        if not pp_flag:
            print(f"🧧add")
            for i in range(continue_days, 0, -1):
                target_timestamp = now_timestamp - 86400 * i
                target_date = (today_date + datetime.timedelta(days=-i)).strftime('%Y-%m-%d')
                text = f"./redistool add_signhb_jimdb {pin} {target_timestamp} 0 0 0; " \
                       f"./redistool add_signhb {pin} {target_timestamp} 0 0 0;" \
                       f"    # {target_date}"
                print(text)
        else:
            print(f"💰add")
            print(f"[TODO]")

    def sign_info_by_pin(self, pin, continue_days=7, pp_flag=0):
        print()
        self.del_sign(pin, pp_flag)
        self.query_sign(pin, pp_flag)
        self.add_sign(pin, continue_days, pp_flag)


if __name__ == "__main__":
    s = Signhb()
    s.get_pins()
    pin = "jd_4551ecddf601a"
    s.sign_info_by_pin(pin)
    # s.sign_info_by_pin(pin, pp_flag=1)
