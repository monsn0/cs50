def main():
    time_input = input("What time is it? ").lower()
    try:
        time = convert(time_input)

        if time >= 7 and time <= 8:
            print("breakfast time")
        elif time >= 12 and time <= 13:
            print("lunch time")
        elif time >= 18 and time <= 19:
            print("dinner time")

    except ValueError:
        print("Please enter a valid time in the following format: ##:## or ##:## a/p.m.")

def convert(time):
    if not time.endswith(".m."):
        hour, minute = time.split(":")

    elif time.endswith("p.m."):
        time = time.removesuffix("p.m.").rstrip()
        hour, minute = time.split(":")
        if int(hour) < 12:
            hour = str(int(hour) + 12)

    elif time.endswith("a.m."):
        time = time.removesuffix("a.m.").rstrip()
        hour, minute = time.split(":")
        if hour == "12":
            hour = "0"

    return float(hour) + (float(minute) / 60)

main()
