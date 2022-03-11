yy1,yy2 = input().split()
yy1,yy2 = int(yy1),int(yy2)
day = ['일','월','화','수','목','금','토']
day1 = str(input())

while day.count(day1) == 0:
    day1 = str(input())
count = 0

for yy in range(yy1,yy2):
    if yy % 400 == 0:
        isLeap = True 
    elif yy % 100 == 0:
        isLeap = False
    elif yy % 4 == 0:
        isLeap = True
    else:
        isLeap = False
    if isLeap:
        count += 1

a = yy2 - yy1
a = (a * 365 + count) % 7
a = a + day.index(day1)
if a > 6:
    a = a - 6
print(day[a])