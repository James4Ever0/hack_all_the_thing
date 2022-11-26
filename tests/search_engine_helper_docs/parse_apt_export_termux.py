
banned=['Sorting...','Full Text Search...']

with open("apt_export_termux.log","r") as f:
    d=f.read()
    lines=d.split("\n")

    mprog=[]
    import parse
    mbuf=[]

    for l in lines:
        if any([(b in l) for b in banned]):
            continue
        else:
            if l.strip() == "":
                if mbuf == []:
                    continue
                else:
                    mhead=mbuf[0]
                    mtail=mbuf[1]
                    #print("_"*4)
            else:
                #print(l)
                mbuf.append(l)
