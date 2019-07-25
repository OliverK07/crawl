from oliverCrawl.class_craw import crawl
import time
import csv

tStart = time.time()
sourceFile = input("Enter Source csv name:")
targetFile = input("Enter Target csv name:")
s_Date = input("Enter Start date in format 'yyyy/mm/dd' :")
e_Date = input("Enter End date in format 'yyyy/mm/dd' :")
with open(targetFile, 'w', newline='') as tgt:
    writer = csv.writer(tgt)
    writer.writerow(['No', 'Start', 'End', 'percentage'])
    # writer.writerow(['No', 'Start', 'End'])
    with open(sourceFile, newline='') as csvFile:
        tmp = crawl("tmp")
        # with open('test.csv', newline='') as csvFile:
        rows = csv.reader(csvFile)
        for row in rows:
            if len(row[0]) < 3:
                print("Source file content invalid.")
                continue
            print("Dealing code: " +row[0])
            # tmp = getRow(row[0], start_day, end_day)
            tmp.setCode(row[0])
            tmp.setStartDate(s_Date)
            tmp.setEndDate(e_Date)
            tmp.createURL()
            writer.writerow(tmp.getRow())

tEnd = time.time()
print ("spend time:")
print (tEnd -tStart)
