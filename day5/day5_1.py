import re
with open('day5_input', 'r') as f:
    total_lines = f.readlines()
    total_seeds = total_lines[0].rstrip('\n').split(' ')[1::]
    total_seeds = list(map(int, total_seeds))
    done = True
    end_locs = set()
    for seed in total_seeds:
        for each in total_lines[2::]:
            each = each.rstrip('\n')
            if bool(re.search('[a-z]', each.split('-')[0])):
                cur_map = each.split('-')[0]
                done = True
            elif bool(re.search(r'\d+', each)) and (seed >= int(each.split(' ')[1]) and (seed < int(each.split(' ')[1])+int(each.split(' ')[2]))) and done:
                diff = int(each.split(' ')[1]) - int(each.split(' ')[0])
                dest = seed - diff
                seed = dest
                done = False
            elif bool(re.search(r'\d+', each)) and not(seed >= int(each.split(' ')[1]) and (seed < int(each.split(' ')[1])+int(each.split(' ')[2]))):
                dest = seed
        end_locs.add(dest)
    print(min(end_locs))
