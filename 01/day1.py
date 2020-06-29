import math

input_file = "./day1.input"
with open(input_file, 'r') as f:
    input_lines = f.readlines()

part2 = False
##########################
## using basic functions
##########################
f = lambda x: math.floor(x/3)-2

def rf(mass):
    fuel_required = f(mass)
    fuel_for_fuel = 0
    while (fuel_required>0):
        fuel_for_fuel += fuel_required
        fuel_required = f(fuel_required)
    return fuel_for_fuel

fuel_sum = 0
for line in input_lines:
    mass = int(line.strip('\n'))
    fuel_sum += rf(mass) if part2 else f(mass)

print("Total fuel: {}".format(fuel_sum))

##############
## using map
##############
input_p1 = map(lambda x: int(x.strip('\n')), input_lines)
f = lambda x: 0 if x < 9 else math.floor(x/3)-2
rf = lambda x, y, func: 0 if y <= 0 else f(y) + func(x + f(y), f(y), func)
solve_func = (lambda x: rf(0, x, rf)) if part2 else (lambda x: f(x))
print("Total fuel: {}".format(sum(map(solve_func, input_p1))))

## Solution:
## Part1: 3394689
## Part2: 5089160