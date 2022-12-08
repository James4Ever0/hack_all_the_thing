import nmap3
nm=nmap3.NmapHostDiscovery()
#nm=nmap3.Nmap()
#import nmap
#nm=nmap.PortScanner()
mline=['121.199.46.85:443']
with open("my_targets.log",'r') as f:
#    for line in f.readlines():
    for line in mline:
        l=line.strip()
        if ":" in l:
            l=line.split(':')
            ipaddr=l[0]
            print("ip?",ipaddr)
            #nm.scan(ipaddr)
            #r=nm[ipaddr]['tcp'].keys()
            r=nm.nmap_portscan_only(ipaddr)
            #r=nm.scan_top_ports(ipaddr)
            # i want all common ports.
            #print('result?',r)
            ports=r[ipaddr]["ports"]
            for p in ports:
                pn=p["portid"]
                ps=p["state"]
                sn=p["service"]['name']
                print(pn, ps, sn)
