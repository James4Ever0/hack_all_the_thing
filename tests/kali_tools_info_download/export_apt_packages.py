import subprocess

output = subprocess.check_output(["apt","list"])
#breakpoint()
# skip first "Listing..." line.
from io import StringIO 

mio = StringIO(output.decode("utf-8"))
for line in mio.readline():
    print("LINE?",line)
