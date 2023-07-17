import csv
from collections import defaultdict

batch = {}
batch_no = {}
cno = defaultdict(list)
courses = [[defaultdict(list) for _ in range(10)] for _ in range(10)]

days = {
    '1MON': 1,
    '2TUE': 2,
    '3WED': 3,
    '4THU': 4,
    '5FRI': 5,
}

hrs = {
    'H1': 1,
    'H2': 2,
    'H3': 3,
}

hn = 0
bn = 0
ans = []

def print_map_st_st(m):
    with open('timetable.txt', 'a') as file:
        for m1 in m.items():
            file.write(f"{m1[0]:<5}{m1[1]:<5}\n")
        file.write("--------------------------------------------------------------------\n")

def print_map_st_ll(m):
    with open('timetable.txt', 'a') as file:
        for i, sublist in enumerate(m):
            for value in sublist:
                file.write(f"{i:<5}{value:<5}\n")
        file.write("--------------------------------------------------------------------\n")

def print_map_st_vector(m):
    with open('timetable.txt', 'a') as file:
        for h in hrs:
            for b in batch:
                for i in range(1, ans[hrs[h]][batch_no[b]]):
                    file.write(f"{h:<5}{b:<30}")
                    for d in days:
                        if len(courses[hrs[h]][days[d]][b]) >= i:
                            temp = courses[hrs[h]][days[d]][b][i-1]
                            vec = cno[temp]
                            file.write(f"{temp:<20}{vec[0]:<60}{vec[1]:<10}{vec[2]:<10}")
                        else:
                            file.write(f"{' ':<20}{' ':<60}{' ':<10}{' ':<10}")
                    file.write("\n")
        file.write("--------------------------------------------------------------------\n")

def print_timetable(courses):
    with open('timetable.txt', 'a') as file:
        for h in hrs:
            for b in batch:
                for i in range(1, ans[hrs[h]][batch_no[b]] + 1):
                    row = f"{h} {b} "
                    for d in days:
                        if len(courses[hrs[h]][days[d]][b]) >= i:
                            temp = courses[hrs[h]][days[d]][b][i-1]
                            row += f"{temp:<20}{cno[temp][0]:<60}{cno[temp][1]:<10}{cno[temp][2]:<10}"
                        else:
                            row += f"{'' : <20}{'' : <60}{'' : <10}{'' : <10}"
                    file.write(row + '\n')
        file.write("--------------------------------------------------------------------\n")

with open('query_result.csv', mode='r') as file:
    csvFile = csv.DictReader(file)
    cnt = 1
    for lines in csvFile:
        if lines['batch-code'] not in batch_no.keys():
            batch_no[lines['batch-code']] = cnt
            cnt += 1
        batch[lines['batch-code']] = lines['batch']
        cno[lines['cno']] = [lines['title'], lines['credits'], lines['fac']]
        courses[hrs[lines['hours']]][days[lines['day']]][lines['batch-code']].append(lines['cno'])

    hn = len(hrs)
    bn = len(batch)
    ans.append([0]*15)
    for h in hrs:
        temp = []
        temp.append(0)
        for b in batch_no:
            ele = 0
            for d in days:
                ele = max(ele, len(courses[hrs[h]][days[d]][b]))
            temp.append(ele)

        ans.append(temp)

    with open('timetable.txt', 'w') as file:
        for sublist in ans:
            file.write(" ".join(str(item) for item in sublist) + '\n')

    print_map_st_st(hrs)
    print_map_st_st(batch_no)
    print_map_st_ll(ans)
    print_map_st_vector(courses)
    print_timetable(courses)
