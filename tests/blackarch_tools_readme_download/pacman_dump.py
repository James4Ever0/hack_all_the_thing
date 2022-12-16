import subprocess

cmd = ["pacman","-Si"]

output = subprocess.check_output(cmd)
import io
sio = io.StringIO(output.decode('utf-8')+"\n\n")

sec = []
for line in sio.readlines():
    line =line.strip()
    if line !="":
        sec.append(line)
    if line == "" and sec !=[]:
        # process this sec.
        sec = []
