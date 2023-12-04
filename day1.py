import re
with open(r'day1_input.txt', 'r') as f:
    l = []
    for line in f.readlines() + ['']:
        coordinate = ''
        match = re.findall(r'\d+', line)
        string = ''
        s = ''.join(match)
        if len(s) == 1:
            string = s + s
        if len(s) > 1:
            string = s[0] + s[-1]
        if len(s) == 0:
            string = '00'            
        number = int(string)
        l.append(number)
    print(sum(l))
