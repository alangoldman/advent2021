file = open("day3_input.txt", "r")
lines = file.readlines()
file.close()

report = [l.strip() for l in lines]

gamma = ""
epsilon = ""
for i in range(0, len(report[0])):
    zeros = 0
    ones = 0
    for r in report:
        if r[i] == "0":
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
power_consumption = gamma*epsilon

print(gamma, epsilon, power_consumption)

#part 2
def get_rating(readings, i, most):
    if len(readings) == 1:
        return readings[0]
    if i >= len(readings[0]):
        raise "Index out of bounds"
    if len(readings) == 0:
        raise "No more readings available"
    zeros = 0
    ones = 0
    for r in readings:
        if r[i] == "0":
            zeros += 1
        else:
            ones += 1
    if most and zeros > ones or (not most and zeros <= ones):
        filtered = [r for r in readings if r[i]=="0"]
    else:
        filtered = [r for r in readings if r[i]=="1"]
    return get_rating(filtered, i+1, most)

oxygen = int(get_rating(report, 0, True),2)
co2 = int(get_rating(report, 0, False),2)

print(oxygen, co2, oxygen*co2)