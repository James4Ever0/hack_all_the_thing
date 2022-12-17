import subprocess

cmd = ["pacman","-Si"]

output = subprocess.check_output(cmd)
import io
sio = io.StringIO(output.decode('utf-8')+"\n\n")

sec = []
for line in sio.readlines():
    mline =line.strip()
    if mline !="":
        sec.append(line)
    if mline == "" and sec !=[]:
        # process this sec.
        fmts = []
        for s in sec:
            if s[0].isalnum(): # better analyze it. what is it?
                # check the format.
                if ":" in s:
                    # then it must be the line.
                    mprefix = s.split(":")[0]
                    myName = mprefix.strip()
                    if len(myName)>0:
                        mformat = mprefix+":"+"{"+myName+"}"
                        fmts.append(mformat)
        if len(fmts)>0: 
            myFormatter = "\n".join(fmts)
            source_file = "".join(sec)
            source_file = source_file.strip().replace("\n"," \n")
            import parse
            # do we have parse in blackarch?
            # yes, by our dearly anaconda.
            # heck!
            result = parse.parse(myFormatter, source_file)
            if result is None:
                print("source?",source_file)
                print("_"*4)
                print("formatter?",myFormatter)
                print("_"*4)
                print("shit happened. nothing parsed.")
                breakpoint()
        sec = []
