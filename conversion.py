import sys
import json, xmltodict, yaml

file = sys.argv[1]
file_object = open(file, "r")
#new_file = str(sys.argv[2])

def file_format(file): #returns format of a file

    format = file.split(".")[-1]

    if (format == "json" or format == "xml" or format =="yml" or format =="yaml"):
        return format
    else:
        return("wrong")


def is_valid(file, type): #checks if format is correct
    match type:
        case "json":
            try:
                json.load(file)
            except ValueError as error:
                print("Wrong json format: ", error)
                return False
            else:
                return True
            finally:
                file.close()
        case "xml":
            try:
                xmltodict.parse(file.read())
            except Exception as error:
                print("Wrong xml format: ", error)
                return False
            else:
                return True
            finally:
                file.close()
        case "yml" | "yaml":
            try:
                yaml.safe_load(file)
            except yaml.YAMLError as error:
                print("Wrong yaml format: ", error)
                return False
            else:
                return True
        case "wrong":
            return False

def convert_json(file,new_type):

    with open(file) as input:
        jsonStr = input.read()
        obj = json.loads(jsonStr)

    match new_type:
        case "xml":
            print("konwersja json na xml")
            try:
                new_file = open("xml_converted_file.xml", "w")
                new_file.write(xmltodict.unparse(obj,))
                new_file.close()
            except ValueError as error:
                print("Cant convert that file to xml: ", error)
        case "yml" | "yaml":
            try:
                new_file = open("yaml_converted_file.yml", "w")
                new_file.write(yaml.dump(obj))
                new_file.close()
            except ValueError as error:
                print("Cant convert that file to yaml: ", error)
        case "json":
            print("Plik już jest w formacie json")
            return file

my_format = file_format(file)
print(my_format)
print(is_valid(file_object, my_format))
convert_json(file, "xml")



