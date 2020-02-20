#!/usr/bin/python3

# waktu start 6:52
# 7:12 - 8:32

class ATime():
    time_min = ""
    time_hour = ""
    time_sec = ""

    def __init__(self, time_str):
        self.time_str = time_str
        self.time_hour, self.time_min, self.time_sec = self.parse_time(self.time_str)

    def parse_time(self, time_now):
        time_min_tmp = ""
        time_hour_tmp = ""
        time_sec_tmp = ""
        total_dot = 0

        for time_len in range(len(time_now)):
            if time_now[time_len] != ":":
                if total_dot == 0:
                    time_hour_tmp += time_now[time_len]
                elif total_dot == 1:
                    time_min_tmp += time_now[time_len]
                elif total_dot == 2:
                    time_sec_tmp += time_now[time_len]
            else:
                total_dot+=1
        return time_hour_tmp, time_min_tmp, time_sec_tmp

    def add(self, time_now):
        hour_now, mnt_now, sec_now = self.parse_time(time_now)

        hour_tmp = "0"
        mnt_tmp = "0"
        sec_tmp = "0"

        if (int(self.time_hour) + int(hour_now)) > 23:
            hour_diff = (int(self.time_hour) + int(hour_now)) - 23
            hour_tmp = str(hour_diff)
        else:
            hour_tmp = int(self.time_hour) + int(hour_now)

        if (int(self.time_min) + int(mnt_now)) > 59:
            mnt_diff = (int(self.time_min) + int(mnt_now)) - 60
            mnt_tmp = str(mnt_diff)
            hour_tmp = str(int(self.time_hour) + int(hour_now) + 1)
        else:
            mnt_tmp = int(self.time_min) + int(mnt_now)

        if (int(self.time_sec) + int(sec_now)) > 59:
            sec_diff = (int(self.time_sec) + int(sec_now)) - 60
            sec_tmp = str(sec_diff)
            mnt_tmp = str(int(self.time_sec) + int(mnt_now)+ 1)
        else:
            sec_tmp = int(self.time_sec) + int(sec_now)

        self.time_hour = hour_tmp
        self.time_min = mnt_tmp
        self.time_sec = sec_tmp

    def now(self):
        self.time_hour = "0"+str(self.time_hour) if int(self.time_hour) < 10 else self.time_hour
        self.time_min = "0"+str(self.time_min) if int(self.time_min) < 10 else self.time_min
        self.time_sec = "0"+str(self.time_sec) if int(self.time_sec) < 10 else self.time_sec
        return str(self.time_hour) +":"+ str(self.time_min) +":"+ str(self.time_sec)

if __name__ == "__main__":
    print("Mulai berjalan jalan")
    waktu = ATime("6:52:0") # format jj:mm:dd

    print("1km perjalanan awal", waktu.now())
    waktu.add("0:8:15")
    print("3km perjalanan kedua", waktu.now())
    waktu.add("0:7:12")
    print("1km sebelum sampai rumah", waktu.now())
    waktu.add("0:8:15")
    print("Sampai dirumah jam", waktu.now())