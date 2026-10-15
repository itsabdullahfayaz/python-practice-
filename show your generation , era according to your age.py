
name = input("Enter your name: ")
age = int(input("Enter your age: "))

year = 2026 - age

print("Name:", name)
print("Birth Year:", year)

if year >= 1960 and year <= 1969:
    print("Era: 60s")
    print("Generation: Baby Boomers")

elif year >= 1970 and year <= 1979:
    print("Era: 70s")
    print("Generation: Generation X")

elif year >= 1980 and year <= 1989:
    print("Era: 80s")
    print("Generation: Millennials")

elif year >= 1990 and year <= 1999:
    print("Era: 90s")
    print("Generation: Millennials")

elif year >= 2000 and year <= 2009:
    print("Era: 2000s")
    print("Generation: Gen Z")

elif year >= 2010 and year <= 2026:
    print("Era: 2010s")
    print("Generation: Gen Alpha")

else:
    print("You are from an era before 1960 or the year is invalid.")
