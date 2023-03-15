import xml.etree.ElementTree as tree


def write_xml_file(accounts, counter, output_path):
    root = tree.Element("root")
    for user in accounts:
        account = tree.SubElement(root, "account")
        tree.SubElement(account, "user name").text = user.name
        tree.SubElement(account, "account id").text = user.account_id
        tree.SubElement(account, "address").text = user.address
        tree.SubElement(account, "phone number").text = user.phone_number

    final_tree = tree.ElementTree(root)
    final_tree.write(output_path)


def read_file_contents(input_file):
    with open(input_file, 'r') as file:
        return file.readlines()
