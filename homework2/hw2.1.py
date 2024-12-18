year=int(input("Enter the number of years:  "))
month=12
day=365
hour=24
print()

def days():
    return year*day
print(f"number of Days in {year} year(s):  ", days())
print()

def months():
    return year*month
print(f"number of Mounths in {year} year(s):  ", months())
print()

def hours():
    return year*day*hour
print(f"number of Hours in {year} year(s):  ", hours())
print()