import re
def parser(line):
    bag = {'r':0,'g':0,'b':0}
    for num, colour in re.findall(r'(\d+) (\w)',line):
        bag[colour] = max(bag[colour], int(num))
    line = re.findall(r'(\w+)', line)[1]
    return bag, line

with open('day2_input', 'r') as f:
    total = 0
    for line in f.readlines():
        par_output = parser(line)
        total += (par_output[0]['r'] * par_output[0]['g'] * par_output[0]['b'])
    print(total)
