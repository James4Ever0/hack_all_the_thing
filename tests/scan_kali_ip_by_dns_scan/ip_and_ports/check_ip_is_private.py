import ipaddress

def is_private_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        if ip_obj.is_private:
            return True
        else:
            return False
    except ValueError:
        return False

# Test the function with an IP address
ip_to_check = '172.16.194.172'

if is_private_ip(ip_to_check):
    print(f"{ip_to_check} is a private IP address.")
else:
    print(f"{ip_to_check} is not a private IP address.")
