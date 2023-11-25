import json
import argparse
import xml.etree.ElementTree as ET


class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self, filename):
        with open(filename, 'w') as json_file:
            json.dump(self.get_dict(), json_file, indent=4)
        print(f"Data converted to Json and saved to {filename}")

    def get_dict(self):
        return self.__dict__

    def convert_to_xml(self, filename):
        root = ET.Element('Human')
        for key, value in self.get_dict().items():
            ET.SubElement(root, key).text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filename)
        print(f"Data converted to XML and saved to {filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert class instance to JSON or XML")
    parser.add_argument("--command", choices=["json", "xml"], required=True, help="Choose 'json or 'xml'")
    parser.add_argument("--filename", required=True, help="Specify the output filename")
    args = parser.parse_args()

    data = {"name": "Mike", "age": "37", "gender": "Male", "birth_year": "1986"}
    human_instance = Human(**data)

    if args.command == "json":
        human_instance.convert_to_json(args.filename)
    elif args.command == "xml":
        human_instance.convert_to_xml(args.filename)
