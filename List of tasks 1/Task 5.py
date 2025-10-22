class Time:
    def __init__(self, hour=0, minute=0, second=0):
        if not(0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59):
            raise ValueError("Incorrect input")
        self.hour = hour
        self.minute = minute
        self.second = second

    def set_time(self, hour=0, minute=0, second=0):
        if not(0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59):
            raise ValueError("Incorrect input")
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        return f"Time({self.hour}, {self.minute}, {self.second})"

    def __str__(self):
        suffix = "AM"
        hour = self.hour
        if hour >= 12:
            suffix = "PM"
            if hour > 12:
                hour -= 12
        if hour == 0:
            hour = 12
        return f"{hour:02}:{self.minute:02}:{self.second:02} {suffix}"

if __name__ == "__main__":
    t1 = Time(14, 30, 45)
    print(repr(t1))
    print(str(t1))
    print(t1)

    t2 = Time(0, 5, 7)
    print(t2)

    t3 = Time()
    t3.set_time(23, 59, 59)
    print(t3)