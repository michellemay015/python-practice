"""
Task 3: Machine length report

Each line in `lines` is: part_id, machine, length (mm).
Spec is 11.95 to 12.05 mm (both ends are OK).

For each machine, report:
  - how many parts were measured
  - the average length (3 decimals)
  - how many parts were NG (outside spec)

Some rows have a length that is not a number. Skip them,
don't crash, and count how many rows were skipped.

Print the machines in order M1, M2, M3.

Expected output:
M1: 4 parts, avg 11.980 mm, NG 1
M2: 3 parts, avg 12.030 mm, NG 1
M3: 3 parts, avg 12.033 mm, NG 1
Skipped rows: 1

Stretch goal:
After the report, print the machine with the highest NG rate
(NG / parts) as a percentage with 1 decimal, e.g.
Worst machine: M2 (33.3% NG)
If two machines tie, printing either one is fine.
"""

lines = [
    "P001,M1,12.02",
    "P002,M2,12.08",
    "P003,M1,11.97",
    "P004,M3,12.00",
    "P005,M2,err",
    "P006,M1,11.92",
    "P007,M3,12.04",
    "P008,M2,11.98",
    "P009,M3,12.06",
    "P010,M1,12.01",
    "P011,M2,12.03",
]

# write your code below
low,high = 11.95,12.05
def in_spec(length):
    return low<=length<=high
count={}
skipped=0
for l in lines:
    part_id, machine, length=l.split(",")
    try:
        length=float(length)
    except ValueError:
        skipped+=1
        continue
        
    if machine not in count:
        count[machine]={"OK":0,"NG":0,"SUM":0}
        
    cm=count[machine]  
    if in_spec(length):
        cm["OK"]+=1
    else:
        cm["NG"]+=1
    cm["SUM"]=cm["SUM"]+length
worst=None
worstrate=-1
for machine in sorted(count): #(count,reverse=True) for reverse
    cm=count[machine] 
    total=cm["OK"]+cm["NG"]
    average=cm["SUM"]/total
    print(f"{machine}: {total} parts, avg {average:.3f} mm, NG {cm['NG']}")

    rate=cm["NG"]/total*100
    if rate>worstrate:
        worst,worstrate=machine,rate
print(f"Skipped rows: {skipped}")
print(f"Worst machine: {worst} ({worstrate:.1f}% NG)")

    
