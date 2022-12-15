import subprocess

output = subprocess.check_output(["apt","list"])
#breakpoint()
# skip first "Listing..." line.
from io import StringIO 
