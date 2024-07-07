import xml.etree.ElementTree as ET

# Step 1: Parse XML Input
def parse_xml(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        return root
    except Exception as e:
        print(f"Error parsing XML: {e}")
        return None

# Step 2: Define Data Mapping Rules
mapping_rules = {
    'source_field_1': 'target_field_1',
    'source_field_2': 'target_field_2',
    # Add more rules as needed
}

# Step 3: Perform Data Mapping
def perform_mapping(xml_root, mapping_rules):
    mapped_data = []
    for record in xml_root.findall('.//record'):
        record_data = {}
        for source, target in mapping_rules.items():
            source_element = record.find(source)
            if source_element is not None and source_element.text:
                record_data[target] = source_element.text
            else:
                record_data[target] = None
        mapped_data.append(record_data)
    return mapped_data

# Step 4: Output Mapped Data
def main(xml_file):
    xml_root = parse_xml(xml_file)
    if xml_root is not None:
        mapped_data = perform_mapping(xml_root, mapping_rules)
        for data in mapped_data:
            print(data)

if __name__ == "__main__":
    input_xml_file = "C:\\Users\\Gaurav\\Desktop\\Internship proj\\Input_335300.xml"  # Replace with the path to your XML file
    main(input_xml_file)
