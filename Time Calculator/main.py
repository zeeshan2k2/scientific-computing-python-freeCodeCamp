
def add_time(time, added_hours, day=None):
    updated_time = []
    week_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    split_time = time.split()
    for_am_and_pm = split_time[1]
    splitting_numbers = split_time[0].split(":")
    hours = int(splitting_numbers[0])
    minutes = int(splitting_numbers[1])
    split_added_hours = added_hours.split(":")
    hours_added_hours = int(split_added_hours[0])
    minutes_added_hours = int(split_added_hours[1])
    sum_hours = hours + hours_added_hours
    sum_minutes = minutes + minutes_added_hours

    # checking first condition

    if sum_hours <= 12 and sum_minutes < 60:
        updated_time.append(sum_hours)
        updated_time.append(sum_minutes)
        updated_time.append(for_am_and_pm)
        print(str(updated_time[0]) + ":" + str(updated_time[1]), str(updated_time[2]))

    # checking second condition

    elif sum_hours <= 12 and sum_minutes > 60:
        updated_minutes = sum_minutes % 60
        if updated_minutes < 10:
            updated_minutes = "0" + str(updated_minutes)
        added_hours = sum_minutes // 60
        sum_hours = sum_hours + added_hours
        updated_hours = sum_hours - 12
        if updated_hours == 0:
            updated_hours = 12
        if sum_hours >= 12 and for_am_and_pm.lower() == "am":
            for_am_and_pm = "PM"
        elif sum_hours >= 12 and for_am_and_pm.lower() == "pm":
            for_am_and_pm = "AM"

        updated_time.append(updated_hours)
        updated_time.append(updated_minutes)
        updated_time.append(for_am_and_pm)
        print(str(updated_time[0]) + ":" + str(updated_time[1]), str(updated_time[2]))

    # checking third condition

    if sum_hours > 12 and day is not None and sum_minutes > 60 or sum_minutes < 60:
        updated_minutes = sum_minutes % 60
        extra_hours = sum_minutes // 60
        hours_updated = sum_hours % 12 + extra_hours
        sum_hours = sum_hours + extra_hours
        added_days = sum_hours // 24
        num_of_days = added_days % 7
        num = 0

        for days in week_days:
            if day == days:
                return num

            num += 1
        updated_day = (num_of_days + num) % 7

        # function to print new date and time
        def new_data_time(for_am_pm, updated_minutes, num_days):
            if updated_day == 0:
                days_later = ""
            elif updated_day == 1:
                days_later = "(Next Day)"
            elif updated_day >= 2:
                days_later = (sum_hours // 24) + 1, "Days Later"
                days_later = str(days_later).replace("'", "").replace(",", "")

            if updated_minutes < 10:
                updated_minutes = "0" + str(updated_minutes)

            updated_time.append(hours_updated)
            updated_time.append(updated_minutes)
            updated_time.append(for_am_and_pm)

            if day is None:
                updated_time.append("")

            if day is not None:
                number = 0
                for n in week_days:
                    if n == day.lower():
                        break
                    number += 1

                num = 0

                total_days = num_days + number

                if total_days <= 6:
                    for new_day in week_days[number:]:
                        if num == num_days:
                            updated_time.append(new_day)
                            break
                        num += 1

                if total_days >= 7:
                    new = total_days % 7
                    updated_date = week_days[new]
                    updated_time.append(updated_date)

                else:
                    updated_time.append(day)

            if updated_time[0] == 0:
                updated_time[0] = 12

            if days_later == " ":
                print(str(updated_time[0]) + ":" + str(updated_time[1]), str(updated_time[2]),
                      updated_time[3].capitalize(), days_later)
            elif day == None:
                print(str(updated_time[0]) + ":" + str(updated_time[1]), str(updated_time[2]),
                      updated_time[3].capitalize(), days_later)
            elif day != None:
                print(str(updated_time[0]) + ":" + str(updated_time[1]), str(updated_time[2]), ",",
                      updated_time[3].capitalize(), days_later)

        if 12 <= sum_hours and for_am_and_pm.lower() == "pm":
            for_am_and_pm = "AM"
            updated_day = (num_of_days + 1) % 7
            num_days = num_of_days + 1
            new_data_time(for_am_and_pm, updated_minutes, num_days)

        elif sum_hours >= 12 and for_am_and_pm.lower() == "am":
            num = sum_hours % 12
            if num % 2 == 0 and num > 0:
                for_am_and_pm = "PM"
            elif num % 2 != 0 or num == 0:
                for_am_and_pm = "AM"

            # for_am_and_pm = "PM"
            num_days = num_of_days
            new_data_time(for_am_and_pm, updated_minutes, num_days)


add_time("11:30 AM", "2:32", "Monday")
add_time("11:43 PM", "24:20", "tueSday")
add_time("3:00 PM", "3:10")
add_time("11:43 AM", "00:20")
add_time("10:10 PM", "3:30")
add_time("6:30 PM", "205:12")
add_time("12:23 AM", "48:00")
