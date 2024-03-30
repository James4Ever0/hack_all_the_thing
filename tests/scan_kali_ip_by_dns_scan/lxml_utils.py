from lxml import etree

def element_to_dict(element):
    """
    Recursively converts an XML ElementTree element to a dictionary.
    """
    data = {}
    for child in element:
        if child.tag in data:
            if not isinstance(data[child.tag], list):
                data[child.tag] = [data[child.tag]]
            data[child.tag].append(element_to_dict(child))
        else:
            data[child.tag] = element_to_dict(child) if len(child) > 0 else child.text
    return data

def xml_str_to_dict(xml_data):
    # Parse the XML data with lxml
    root = etree.fromstring(xml_data.encode('utf-8'))

    # Convert XML data to a dictionary using the custom function
    xml_dict = element_to_dict(root)
    return xml_dict
if __name__ == "__main__":
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
    xml_dict = xml_str_to_dict(xml_data)
    print(xml_dict)
