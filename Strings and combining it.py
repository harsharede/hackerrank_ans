T = int(raw_input())
s_str = []
for i in range(0,T):
    a = str(raw_input())
    s_str.append(a)

for s in s_str:
    e = ""
    o = ""
    for i in range(len(s)):
        temp = ';'
        if (i % 2) == 0:
            temp = list(s)[i]
            e = e+str(temp)
        else:
            temp = list(s)[i]
            o = o+str(temp)
    print e," ",o



