import sys
n = sys.stdin.readline()

today = n.split()
year = int(today[2])
month = today[0]
day = int(today[1].replace(',',''))
hour, minute = map(int, today[3].split(':'))

default_days = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}
total_day_count = 365

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    default_days['February'] += 1
    total_day_count += 1

total_second = total_day_count * 24 * 60 * 60
passed_day = day - 1

l = list(default_days)
for d in l[:l.index(month)]:
    passed_day += default_days[d]

passed_second = (passed_day * 86400) + (hour * 3600) + (minute * 60)
print((passed_second / total_second) * 100)
