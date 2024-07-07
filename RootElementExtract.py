import xml.etree.ElementTree as ET

def get_root_element_value(xml_file, root_element):
    try:
        tree = ET.parse(xml_file)
        ns = {'ns2': 'urn:schemas-qad-com:xml-services'}  
        root = tree.getroot()

        element = root.find(f".//{root_element}", namespaces=ns)
        if element is not None:
            return element.text.strip() if element.text else None
        else:
            print(f"No matching root element '{root_element}' found in the XML file.")
            return None
    except ET.ParseError as e:
        print(f"Error parsing the XML file: {e}")
        return None

xml_file_path = 'C:\\Users\\Gaurav\\Desktop\\Internship proj\\Input_335300.XML'

root_element_name = 'ns2:siteCode' #Sir here put whatever root element ou want

result = get_root_element_value(xml_file_path, root_element_name)
if result is not None:
    print(f"The value of the root element '{root_element_name}' is: {result}")
