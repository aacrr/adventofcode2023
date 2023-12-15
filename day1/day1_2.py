import re
def rm(x):
    total = 0
    match = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for item in x:
        new = re.sub("[\n]","",item)
        new = re.sub("oneight", "oneeight", new)
        new = re.sub("threeight", "threeeight", new)
        new = re.sub("fiveight", "fiveeight", new)
        new = re.sub("nineight", "nineeight", new)
        new = re.sub("twone", "twoone", new)
        new = re.sub("sevenine", "sevennine", new)
        new = re.sub("eightwo", "eighttwo", new)

        for stri in match:
            if stri in new:
                new = re.sub(stri, str(match.index(stri)+1), new)

        new = re.sub("[a-z]","",new)
        new = new[0] + new[-1]
        total += int(new)
    return total

with open('day1_input','r') as file:
    print(rm(file.readlines()))
