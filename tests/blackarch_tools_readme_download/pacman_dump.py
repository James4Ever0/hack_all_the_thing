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
        for s in sec:
            if s[0].isalnum(): # better analyze it. what is it?
                # check the format.
                if ":" in s:
                    # then it must be the line.
                    mprefix = s.split(":")[0]
                    mformat = 
        sec = []
