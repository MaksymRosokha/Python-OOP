def gen_time(start, stop, step):
    result = start
    while ((result[0] < stop[0]) or
           (result[0] == stop[0] and result[1] <= stop[1]) or
           (result[0] == stop[0] and result[1] == stop[1] and result[2] <= stop[2])):
        yield result
        hours = result[0] + step[0]
        minutes = result[1] + step[1]
        seconds = result[2] + step[2]

        if seconds >= 60:
            minutes += int(seconds / 60)
            seconds %= 60
        if minutes >= 60:
            hours += int(minutes / 60)
            minutes %= 60
        if hours >= 24:
            hours %= 24

        result = (hours, minutes, seconds)


if __name__ == "__main__":
    for time in gen_time((8, 10, 00), (10, 50, 15), (0, 15, 12)):
        print(time)
