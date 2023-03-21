import xml.etree.ElementTree as tree
import xml.dom.minidom

def write_xml_file(accounts, counter, output_path):
    root = tree.Element("account")
    for user in accounts:
        tree.SubElement(root, "user name").text = user.name
        tree.SubElement(root, "account id").text = user.account_id
        tree.SubElement(root, "address").text = user.address
        tree.SubElement(root, "phone number").text = user.phone_number
    final_tree = tree.ElementTree(root)

    final_tree.write(output_path)


def read_file_contents(input_file):
    with open(input_file, 'r') as file:
        return file.readlines()
