from sys import argv
script_name, work_days, hourly_rate, bonus = argv
work_days = int(work_days)
hourly_rate = int(hourly_rate)
bonus = int(bonus)

print("зарплата:", (work_days*8*hourly_rate)+bonus)
