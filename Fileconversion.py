import xml.etree.ElementTree as ET
import pyodbc

def convert_database_to_xml(connection_string, query, output_file):
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute(query)

        root_element = ET.Element("data")

        for row in cursor.fetchall():
            entry = ET.SubElement(root_element, "entry")
            for field in cursor.description:
                key = field[0]
                value = row[field[0]]
                ET.SubElement(entry, key).text = str(value)

        tree = ET.ElementTree(root_element)
        tree.write(output_file, encoding='utf-8', xml_declaration=True)

        print("Database data converted to XML and saved to", output_file)

    except pyodbc.Error as e:
        print("Database error:", e)

if __name__ == '__main__':
    connection_string = "Driver={SQL Server};Server=ServerName;Database=DatabaseName;Trusted_Connection=yes;"
    query = "SELECT * FROM TableName"
    output_file = "output.xml"

    convert_database_to_xml(connection_string, query, output_file)
