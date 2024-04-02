import socket, json

# this sucks and not up to date.

# use file "nmap-services" instead

# command:
# locate nmap-services
# less /usr/share/nmap-services

OUTPUT_FILE = "output/port_to_service.json"

def main():
    portmap = {}
    for port, service_name in generate_port_to_service_name():
        portmap[port] = service_name
    
    with open(OUTPUT_FILE, "w+") as f:
        f.write(json.dumps(portmap))
    print("[get_port_to_service_name]", "data write to:", OUTPUT_FILE)
        
def generate_port_to_service_name():
    for port in range(65535):
        port = port + 1
        try:
            service_name = socket.getservbyport(port)
            print('[get_port_to_service_name]',f"service '{service_name}' is for port {port}")
            yield port, service_name
        except OSError:
            print("[get_port_to_service_name]", f"port {port} not recognized as a service")

if __name__ == "__main__":
    main()