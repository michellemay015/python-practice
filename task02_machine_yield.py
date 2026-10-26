"""
Task 02: Yield per machine

Each record is "part_id,machine,length_mm".
Spec: 11.95 to 12.05 mm (inclusive) = OK, otherwise NG.

1. Write a function in_spec(length) that returns True or False.
2. Count OK and NG for each machine, using a dict of dicts.
3. Print the yield for each machine (1 decimal place).
4. Print all NG part IDs on one line.

Expected output:
M1: OK 3, NG 1, yield 75.0%
M2: OK 2, NG 2, yield 50.0%
NG parts: P002, P005, P008

Stretch goal:
Also write the same 3 lines into task02_summary.txt (use "w" mode).
"""

records = [
    "P001,M1,12.02",
    "P002,M2,12.31",
    "P003,M1,11.98",
    "P004,M2,12.04",
    "P005,M1,11.90",
    "P006,M2,12.00",
    "P007,M1,12.05",
    "P008,M2,11.94",
]

# write your code below
def in_spec(length):
    return 11.95<=length<=12.05
count={}
ngparts=[]

for line in records:
    part_id,machine,length=line.split(',')
    length=float(length)

    if machine not in count:
        count[machine]={"OK":0,"NG":0}

    if in_spec(length):
        count[machine]["OK"]+=1
    else:
        count[machine]["NG"]+=1
        ngparts.append(part_id)
with open("task02_summary.txt", "w") as f:
    for machine, c in count.items():
        total=c["OK"]+c["NG"]
        yields=c["OK"]/total*100
        print(f"{machine}: OK {c['OK']}, NG {c['NG']}, yield {yields:.1f}%")
        f.write(f"{machine}: OK {c['OK']}, NG {c['NG']}, yield {yields:.1f}%\n")
    
    print("NG parts:", ", " .join(ngparts))
    ngpartstext=", " .join(ngparts)
    text =(f"NG parts: {ngpartstext}")
    f.write(text)
    

    
