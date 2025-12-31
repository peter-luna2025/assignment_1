def main():
    time = input("What time is it?  ")
    ctime = time.strip(" a.m.|p.m.")
    hr, min = ctime.split(":")

    actual_time = float(hr) + (float(min) / 100)

    if actual_time >= 7.0 and actual_time <= 8.0:
        print("Breakfast time")

    if actual_time >= 12.0 and actual_time <= 13.0:
        print("Lunch time")

    if actual_time >= 18.0 and actual_time <= 19.0:
        print("Dinner time")

    else:
        return


if __name__ == "__main__":
    main()