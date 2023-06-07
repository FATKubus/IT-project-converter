def XMLtoJS(x, y): 
    print("Zrozumiano. [.xml to .json]")
    print("Próba utworzenia nowego pliku...")
    data = upload_xml(x)
    return_json(y, data)
    print("Sukces!")

def YMLtoJS(x, y): 
    print("Zrozumiano. [.yml to .json]")
    print("Próba utworzenia nowego pliku...")
    data = upload_yml(x)
    return_json(y, data)
    print("Sukces!")

def return_json(x, data):
    with open(x, "w") as f:
        f.write(json.dumps(data)) 
