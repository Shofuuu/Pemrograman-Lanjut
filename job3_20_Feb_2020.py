#!/usr/bin/python3

class ATime():
    time_hour = 0
    time_min = 0
    time_sec = 0

    def __init__(self, time_init):
        self.time_hour, self.time_min, self.time_sec = self.time_parse(time_init)

    def time_parse(self, time_str):
        time_str_hour = ""
        time_str_min = ""
        time_str_sec = ""
        counter = 0

        for str_len in range(len(time_str)):
            if time_str[str_len] != ":":
                if counter == 0:
                    time_str_hour += time_str[str_len]
                elif counter == 1:
                    time_str_min += time_str[str_len]
                elif counter == 2:
                    time_str_sec += time_str[str_len]
            else:
                counter += 1

        return time_str_hour, time_str_min, time_str_sec

    def add(self, time_now):
        time_hour_now, time_min_now, time_sec_now = self.time_parse(time_now)
        time_diff = 0

        if (int(self.time_hour) + int(time_hour_now)) >= 23:
            time_diff = (int(self.time_hour) + int(time_hour_now)) - 24
            self.time_hour = str(time_diff)
        else:
            self.time_hour = str(int(self.time_hour) + int(time_hour_now))

        if (int(self.time_min) + int(time_min_now)) >= 59:
            time_diff = (int(self.time_min) + int(time_min_now)) - 60
            self.time_min = str(time_diff)
            self.time_hour = str(int(self.time_hour) + 1)
        else:
            self.time_min = str(int(self.time_min) + int(time_min_now))

        if (int(self.time_sec) + int(time_sec_now)) >= 59:
            time_diff = (int(self.time_sec) + int(time_sec_now)) - 60
            self.time_sec = str(self.time_sec)
            self.time_min = str(int(self.time_min) + 1)
        else:
            self.time_sec = str(int(self.time_sec) + int(time_sec_now))

    def num2time_format(self, num):
        if len(str(num)) < 2:
            return "0"+num
        else:
            return num

    def now(self):

        return self.num2time_format(self.time_hour) + ":" + self.num2time_format(self.time_min) + ":" + self.num2time_format(self.time_sec)

if __name__ == "__main__":
    waktu = ATime("06:52:00")

    waktu.add("00:08:15")
    waktu.add("00:07:12")
    waktu.add("00:07:12")
    waktu.add("00:07:12")
    waktu.add("00:08:15")

    print(waktu.now())