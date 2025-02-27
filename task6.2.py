input_digit = int(input("Enter your number of sec (0 <= number < 8640000): "))

days, remainin_hours = divmod(input_digit, 24 * 60 * 60)
hours, remainin_minutes = divmod(remainin_hours, 60 * 60)
minutes, seconds = divmod(remainin_minutes, 60)

if 11 <= days % 100 <= 19:
    day_name = "днiв"
else:
    day = days % 10
    if day == 1:
        day_name = "день"
    elif 2 <= day <= 4:
        day_name = "днi"
    else:
        day_name = "днiв"

print(days, f"{day_name}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")