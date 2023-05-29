import sys
import json, xmltodict, yaml

file = sys.argv[1]
file_object = open(file, "r")
format_in = str(sys.argv[2])

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

def convert_json(file, new_type): #convert json file into chosen type

    with open(file) as input:
        jsonStr = input.read()
        obj = json.loads(jsonStr)

    match new_type:
        case "xml":
            print("json to xml")
            try:
                new_file = open("converted_file.xml", "w")
                new_file.write(xmltodict.unparse(obj,))
                new_file.close()
            except ValueError as error:
                print("Cant convert that file to xml: ", error)
        case "yml" | "yaml":
            print("json to yaml")
            try:
                new_file = open("converted_file.yml", "w")
                new_file.write(yaml.dump(obj))
                new_file.close()
            except ValueError as error:
                print("Cant convert that file to yaml: ", error)
        case "json":
            print("file is already in json")

def convert_xml(file, new_type): #convert xml file into chosen type

    with open(file) as input:
        xmlStr = input.read()
        obj = xmltodict.parse(xmlStr)

    match new_type:
        case "xml":
            print("file is already in xml")
        case "yml" | "yaml":
            print("xml to yaml")
            try:
                new_file = open("converted_file.yml", "w")
                new_file.write(yaml.dump(obj))
                new_file.close()
            except ValueError as error:
                print("Cant convert that file to yaml: ", error)
        case "json":
            print("xml to json")
            try:
                new_file = open("converted_file.json", "w")
                new_file.write(json.dumps(obj))
                new_file.close()
            except ValueError as error:
                print("Cant convert that file to json: ", error)

def convert_yaml(file, new_type):
    with open(file) as input:
        yamlStr = input.read()
        obj = yaml.dump(yamlStr)

    match new_type:
        case "xml":
            print("yaml to xml")
            try:
                new_file = open("converted_file.xml", "w")
                new_file.write(xmltodict.unparse(obj))
                new_file.close()
            except ValueError as error:
                print("Cant convert that file to xml: ", error)
        case "yml" | "yaml":
            print("file is already in yaml")
        case "json":
            print("yaml to json")
            try:
                new_file = open("converted_file.json", "w")
                new_file.write(json.dumps(obj))
                new_file.close()
            except ValueError as error:
                print("Cant convert that file to json: ", error)

if (format_in == "json" or format_in == "xml" or format_in =="yml" or format_in =="yaml"):
    if is_valid(file_object, file_format(file)):
        print("your file data is valid ", file_format(file))
        match file_format(file):
            case "json":
                convert_json(file, format_in)
            case "xml":
                convert_xml(file, format_in)
            case "yaml"|"yml":
                convert_yaml(file, format_in)
    else:
        print("your file data is invalid")

else:
    print(format, " is not correct format")




