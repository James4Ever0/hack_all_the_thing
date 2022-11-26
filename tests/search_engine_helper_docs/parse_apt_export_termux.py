
banned=['Sorting...','Full Text Search...']

with open("apt_export_termux.log","r") as f:
    d=f.read()
    lines=d.split("\n")

    for l in lines:
        if any([(b in l) for b in banned]):
            continue
        else:
            if l.strip() == "":
                print("_"*4)
            else:
                print(l)
