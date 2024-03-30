# import os
import subprocess
import xmltodict

# TODO: get open ports from nmap scan report.

NMAP_TIMEOUT = 60
import rich


def scan_ip(ip):
    # scanreport = "scanreport.xml"
    content = subprocess.check_output(f"nmap -oX - {ip}".split(' '), timeout=NMAP_TIMEOUT)
    # os.system(f"nmap -oX - {ip} > {scanreport}")
    # with open(scanreport, "r") as f:
    #     content = f.read()
    return content.strip()


def check_if_is_up_and_open_ports(ip):
    xml = scan_ip(ip)
    data = xmltodict.parse(xml)
    rich.print(data)

    up_count = data["nmaprun"]["runstats"]["hosts"]["@up"]  # str '1'
    # filtered_ports = data['nmaprun']['host']['ports']['filtered'] # these ports are filtered, not scanned.
    scanned_ports = data["nmaprun"]["host"]["ports"]["port"]
    scanned_port_stats = [
        dict(
            port=elem["@portid"],
            protocol=elem["@protocol"],
            state=elem["state"]["@state"],
        )
        for elem in scanned_ports
    ]
    # breakpoint()
    open_ports = [
        elem["port"] for elem in scanned_port_stats if elem["state"] == "open"
    ]
    return {"ports": {"open": open_ports}, "up": up_count}


def main():
    import get_ip_from_xml

    ip_list = get_ip_from_xml.main()
    report = {}
    for ip in ip_list:
        rich.print("Scanning IP:", ip)
        ret = check_if_is_up_and_open_ports(ip)
        report[ip] = ret
        rich.print("IP status:", ret)
    return report

if __name__ == "__main__":
    import json
    report = main()
    rich.print("report:", report)
    output_name = "nmap_scan_report.json"
    with open(output_name, 'w+') as f:
        json.dump(report, f)
    print("report write to:", output_name)