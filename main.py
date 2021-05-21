import itertools
import re
from datetime import datetime

text_file = open("C:/Users/User/Downloads/" + "access_log_Jul95", "r")
lines = text_file.readlines()
text_file.close()

datePattern = r'.*?\[(.*)].*'
filteredLines = []

for line in lines:
    match = re.search(datePattern, line)
    dateString = match.group(1)
    date = datetime.strptime(dateString, "%d/%b/%Y:%H:%M:%S %z")
    fromDate = datetime.strptime("01/Jul/1995:02:35:00 -0400", "%d/%b/%Y:%H:%M:%S %z")
    toDate = datetime.strptime("01/Jul/1995:17:49:00 -0400", "%d/%b/%Y:%H:%M:%S %z")
    statusFilter = " 200 "
    if fromDate < date < toDate and re.search(statusFilter, line):
        filteredLines.append(line)

rankedLines = {}

siteNamePattern = "(.+?) - - "

for i, j in itertools.groupby(filteredLines, key=lambda x: re.search(siteNamePattern, x).group(1)):
    rankedLines[i] = len(list(j))

sort_orders = sorted(rankedLines.items(), key=lambda x: x[1], reverse=True)[:10]

for i in sort_orders:
    print(i[0], i[1])
