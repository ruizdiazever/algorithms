# EXERCISE 3.1

# A
def timeToSeconds():
    "This function return the time in seconds"
    hours = int(input("Hours: "))
    minutes = int(input("Minutes: "))
    seconds = int(input("Seconds: "))

    hours *= 3600
    minutes *= 60
    seconds = seconds + hours + minutes

    print("The result is: ", seconds)

# B
def secondsToTime():
    "This function return the time in hours, minutes and seconds"
    seconds = int(input("Please input time in seconds: "))
    minutes = 0
    hours = 0

    hours = seconds / 3600
    seconds = seconds % 3600

    minutes =   seconds / 60
    seconds = seconds % 60


    print(f"""
    Hours:   {int(hours)}
    Minutes: {int(minutes)}
    Seconds: {int(seconds)}
    """)
