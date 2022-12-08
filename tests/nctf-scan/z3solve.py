from z3 import *

data1 = 0x162AEB99F80DD8EF8C82AFADBA2E087A
data2 = 0x47C9F2ACA92F6476BE7F0A6DC89F4305
data3 = 0x33B57575
answer = []
flag1 = []
key = [0x7E, 0x1F, 0x19, 0x75]
solver = Solver()
flag = [Int("flag%d" % i) for i in range(36)]
for i in range(16):
    answer.append((data1 >> 8 * i) & 0xFF)
for i in range(16):
    answer.append((data2 >> 8 * i) & 0xFF)
for i in range(4):
    answer.append((data3 >> 8 * i) & 0xFF)
print(answer)
for i in range(0, 9):
    v3 = key[3]
    v4 = flag[4 * i + 3]
    v5 = key[0]
    v6 = flag[4 * i]
    v7 = flag[4 * i + 1]
    v8 = key[1]
    v9 = flag[4 * i + 2]
    v10 = (v6 + v4) * (key[0] + v3)
    v11 = key[2]
    v12 = v3 * (v6 + v7)
    v13 = (v3 + v11) * (v7 - v4)
    v14 = v4 * (v11 - v5)
    v15 = v5 * (v9 + v4)
    solver.add(v14 + v10 + v13 - v12 == answer[4 * i])
    solver.add(v6 * (v8 - v3) + v12 == answer[4 * i + 1])
    solver.add(v15 + v14 == answer[4 * i + 2])
    solver.add(v6 * (v8 - v3) + (v8 + v5) * (v9 - v6) + v10 - v15 == answer[4 * i + 3])

if solver.check() == sat:
    m = solver.model()
    rex = []
    for i in range(34):
        rex.append(m[flag[i]].as_long())
    print(rex)
else:
    print("n0")
