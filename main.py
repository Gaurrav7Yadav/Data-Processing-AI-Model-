import xml.etree.ElementTree as ET

def get_root_element_values(xml_files, root_elements, output_file):
    try:
        ns = {'ns2': 'urn:schemas-qad-com:xml-services'}

        with open(output_file, 'w') as output:
            output.write('<root>\n')  # Start of the output XML file

            for xml_file in xml_files:
                output.write(f'  <file name="{xml_file}">\n')  # Start of file entry in the output XML

                tree = ET.parse(xml_file)
                root = tree.getroot()

                for root_element in root_elements:
                    element = root.find(f".//{root_element}", namespaces=ns)
                    if element is not None:
                        value = element.text.strip() if element.text else None
                        output.write(f'    <result root_element="{root_element}" value="{value}"/>\n')
                    else:
                        output.write(f'    <result root_element="{root_element}" not_found="true"/>\n')

                output.write('  </file>\n')  # End of file entry in the output XML

            output.write('</root>')  # End of the output XML file

        print(f"Output written to {output_file}")

    except ET.ParseError as e:
        print(f"Error parsing the XML file: {e}")

xml_files_list = ['C:\\Users\\Gaurav\\Desktop\\Internship proj\\Input_335300.XML', 'C:\\Users\\Gaurav\\Desktop\\Internship proj\\Output_335300.XML', 'C:\\Users\\Gaurav\\Desktop\\Internship proj\\Output_335301.XML']  # Replace with your file paths
root_elements_list = ['ns2:interfaceName', 'ns2:transID', 'ns2:Order_OID']
output_xml_file = 'output_results.xml'  # Replace with your desired output file name

get_root_element_values(xml_files_list, root_elements_list, output_xml_file)
