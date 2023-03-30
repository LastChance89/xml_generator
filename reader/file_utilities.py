from xml.dom import minidom


def write_xml_file(accounts, output_path):
    doc = minidom.Document()
    root = doc.createElement('accounts')
    doc.appendChild(root)

    for user in accounts:
        try:
            account = doc.createElement('account')
            username = doc.createElement('user name')

            username.appendChild(doc.createTextNode(user.name))
            account.appendChild(username)

            account_id = doc.createElement('account id')
            account_id.appendChild(doc.createTextNode(user.account_id))
            account.appendChild(account_id)

            address = doc.createElement('address')
            address.appendChild(doc.createTextNode(user.address))
            account.appendChild(address)

            phone_number = doc.createElement('phone number')
            phone_number.appendChild(doc.createTextNode(user.phone_number))
            account.appendChild(phone_number)

            root.appendChild(account)
        except Exception as e:
            print(e)

    doc.writexml(open(output_path, 'w'),
                 indent=" ",
                 addindent=" ",
                 newl="\n")


def read_file_contents(input_file):
    with open(input_file, 'r') as file:
        return file.readlines()
