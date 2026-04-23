ages = [11,12,13,14,15,16,17,18,19,20]
between = 0
above = 0
below = 0

for age in ages:
    if age < 18:
        below += 1
    elif 18 <= age <+ 20:
        between += 1
    else: # age > 20
        above += 1

# display results
print("Age list:", ages)
print("Total number of values:", len(ages))
print("NUmber of people below 18:", below)
print("Number of between 18 to 20:", between)
print("Number of people above 20:", above)
