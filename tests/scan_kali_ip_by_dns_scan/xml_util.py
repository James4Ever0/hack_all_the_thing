import xml.etree.ElementTree as ET

# equivalent to xmltodict

# remember to fix invalid xml elements manually.

# Convert XML data to a Python dictionary
def xml_elem_to_dict(xml_element):
    data = {}
    for child in xml_element:
        data[child.tag] = xml_elem_to_dict(child) if len(child) > 0 else child.text
    return data

def xml_str_to_dict(xml_data):

    # Parse the XML data
    root = ET.fromstring(xml_data)

    xml_dict = xml_elem_to_dict(root)
    return xml_dict

if __name__ == '__main__':
    # Sample XML data
    xml_data = """
<root>
    <person>
        <name>John Doe</name>
        <age>30</age>
    </person>
    <person>
        <name>Jane Smith</name>
        <age>25</age>
    </person>
</root>
"""
    print(xml_str_to_dict(xml_data))