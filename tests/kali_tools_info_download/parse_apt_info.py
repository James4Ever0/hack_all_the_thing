import parse

def parse_apt_info(packageName):
    cmd = ["apt","show",packageName]
    import subprocess
    output = subprocess.check_output(cmd)
    so = output.decode('utf-8')
    print(so)

if __name__ == "__main__":
    pname = "python3"
