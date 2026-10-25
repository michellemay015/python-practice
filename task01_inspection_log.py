"""
Task 1: Inspection log summary

Each line is part_id, result, measured_length_mm.

Print:
1. Total parts, OK count, NG count
2. Yield %, rounded to 1 decimal
3. Average length of OK parts only
4. List of NG part IDs

Expected output:
Total: 6  OK: 4  NG: 2
Yield: 66.7%
Avg OK length: 12.01 mm
NG parts: ['P002', 'P005']

Stretch expected output:
(nothing extra printed, all OK parts are within 12.00 +/- 0.05 mm)

Hint: use line.split(",") and float()
Stretch: flag OK parts outside 12.00 +/- 0.05 mm
"""

log = [
    "P001,OK,12.02",
    "P002,NG,12.31",
    "P003,OK,11.98",
    "P004,OK,12.05",
    "P005,NG,11.62",
    "P006,OK,12.9",
]


# write your code below
OK = 0
NG = 0
Okresult=[]
ng_parts=[]
avgok=0.0
deviation=0

for line in log:
    part_id, result, length = line.split(",")
    length = float(length)
    if result == "OK":
        OK +=1
        Okresult.append(length)

    elif result == "NG":
        NG +=1
        ng_parts.append(part_id)

total=OK+NG
Yield=OK/total*100
avgok= sum(Okresult)/len(Okresult)
print (f"total:{total} OK:{OK} NG{NG}")
print (f"Yield:{Yield:.1f}")
print (f"avgok:{avgok:.2f}mm")
print (f"ng_parts:{ng_parts}")

for line in log:
    part_id, result, length = line.split(",")
    length=float(length)
    if result == "OK" and (length<11.95 or length>12.05):
        print(f"outoftolerance:{part_id},{length}")
