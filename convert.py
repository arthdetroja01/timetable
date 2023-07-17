import csv
from collections import defaultdict
import xlsxwriter
import random

def get_random_color():
    color = '%06x' % random.randint(0, 0xFFFFFF)
    return '#' + color

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

col_map = {}

def make_timetable(courses):
    workbook = xlsxwriter.Workbook('timetable.xlsx')
    worksheet = workbook.add_worksheet()
    merge_format = workbook.add_format(
        {
            "border": 1,
            "align": "center",
            "valign": "vcenter",
            # "fg_color": "white",
        }
    )
    header_format = workbook.add_format({'bold': True, 'align': 'center'})
    color = '#FFC7CE'
    

    worksheet.write(0, 0, 'Hour', header_format)
    worksheet.write(0, 1, 'Batch', header_format)

    col_start = 2
    for day_num, day in enumerate(days):
        worksheet.write(0, col_start + 4 * day_num, day, header_format)
        worksheet.write(0, col_start + 4 * day_num + 1, '', header_format)
        worksheet.write(0, col_start + 4 * day_num + 2, '', header_format)
        worksheet.write(0, col_start + 4 * day_num + 3, '', header_format)
    
    row_start = 1
    cnt = 1
    for h in hrs:
        max_hours = 0
        
        # color += 1
        for b in batch:
            color = ''
            if b in col_map.keys():
                color = col_map[b]
            else:
                color = get_random_color()
                col_map[b] = color
            data_format = workbook.add_format({
                'align': 'center',
                'bg_color': color,
            })
            merge_format1 = workbook.add_format(
            {
                "border": 1,
                "align": "center",
                "valign": "vcenter",
                "bg_color": color,
            }
        )
            # for i in range(1, ans[hrs[h]][batch_no[b]] + 1):
                # row = f"{h} {b} "
            worksheet.write(row_start, 0, h, data_format)
            worksheet.write(row_start, 1, b, data_format)
            max_courses = 0
            for d in days:
                filtered_data = courses[hrs[h]][days[d]][b]
                # print(filtered_data)
                if not len(filtered_data) == 0:
                    title = []
                    cnos = filtered_data
                    facs = []
                    credits = []
                    for j in filtered_data:
                        title.append(cno[j][0])
                        credits.append(cno[j][1])
                        facs.append(cno[j][2])
                    # print(title)
                    # print(cnos)
                    # print(facs)
                    # print(credits)
                    num_courses = len(facs)
                    max_courses = max(max_courses, num_courses)
                    if(num_courses > 0):                        
                        for i in range(0, num_courses):
                            worksheet.write(row_start + i, col_start + 4 * (days[d]-1), cnos[i], data_format)
                            worksheet.write(row_start + i, col_start + 4 * (days[d]-1) + 1, title[i], data_format)
                            worksheet.write(row_start + i, col_start + 4 * (days[d]-1) + 2, facs[i], data_format)
                            worksheet.write(row_start + i, col_start + 4 * (days[d]-1) + 3, credits[i], data_format)
            for d in days:
                filtered_data = courses[hrs[h]][days[d]][b]
                if len(filtered_data) < max_courses:
                    # print(row_start+len( filtered_data), col_start + 4 * (days[d]-1), row_start+max_courses-1, col_start + 4 * (days[d]-1)+3)
                    worksheet.merge_range(row_start+len( filtered_data), col_start + 4 * (days[d]-1), row_start+max_courses-1, col_start + 4 * (days[d]-1)+3, ' ', merge_format)
            if(max_courses > 1):
                worksheet.merge_range(row_start, 1, row_start+max_courses-1, 1, b, merge_format1)
            max_hours += max_courses
            row_start += max_courses

        # print(cnt, max_hours+cnt)
        worksheet.merge_range(cnt, 0, max_hours+cnt, 0, h, merge_format)
        cnt += max_hours+1
        row_start += 1
    worksheet.autofit()
    workbook.close()

    print("Timetable created successfully!")

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
    # print(cno)
    # print_map_st_st(hrs)
    # print_map_st_st(batch_no)
    # print_map_st_ll(ans)
    # print_map_st_vector(courses)
    # print_timetable(courses)
    make_timetable(courses)
