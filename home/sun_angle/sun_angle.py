def sun_angle(time):
    time = int(time.split(':')[0]) * 60 + int(time.split(':')[1])
    if time < 360 or time > 1080:
        return "I don't see the sun!"
    return (time-360)*0.25
