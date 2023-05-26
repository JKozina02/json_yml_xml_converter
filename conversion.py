import sys
import json, xmltodict, yaml

file_name = sys.argv[1]
file_object = open(file_name, "r")
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

format = file_format(file_name)
print(is_valid(file_object, format))
print(format)


