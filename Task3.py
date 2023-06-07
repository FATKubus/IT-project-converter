def XMLtoJS(a, b): 
    print("Zrozumiano. [.xml to .json]")
    print("Próba utworzenia nowego pliku")
    data = upload_xml(a)
    return_json(b, data)
    print("Wykonano!")

def YMLtoJS(a, b): 
    print("Zrozumiano. [.yml to .json]")
    print("Próba utworzenia nowego pliku")
    data = upload_yml(a)
    return_json(b, data)
    print("Wykonano!")

def write_json(a, data):
    with open(a, "w") as f:
        f.write(json.dumps(data)) 
