import re
import xmltodict

# import lxml_utils
import rich


def get_xml_text():
    # Sample text containing IP addresses
    text = (
        open("dns_kali.xml", "r").read() + "</testdata></magictree>\n"
    )  # encluse the element
    # text = open("dns_kali.xml", "r").read()
    return text


def extract_ip_list(text):
    # Regular expression pattern to match IPv4 addresses
    ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

    # Find all IP addresses in the text using re.findall
    ip_addresses = re.findall(ip_pattern, text)

    ret = []
    # Print the extracted IP addresses
    print("Extracted IP addresses:")
    for ip in ip_addresses:
        ret.append(ip)
    return ret


def extract_ip_list_by_parsing(xml_text):
    data = xmltodict.parse(xml_text)
    # data = lxml_utils.xml_str_to_dict(xml_text)
    ret = []
    rich.print(data)
    hostlist = data["magictree"]["testdata"]["host"]
    for host in hostlist:
        ret.append(host["#text"])
    return ret


def main():
    # return extract_ip_list(get_xml_text())
    return extract_ip_list_by_parsing(get_xml_text())


if __name__ == "__main__":
    ip_list = main()
    rich.print("ip list:", ip_list)
