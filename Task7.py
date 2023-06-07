def JStoXML(a, b):
    print("Zrozumiano. [.json to .xml]")
    print("Próba utworzenia nowgo pliku")
    data = load_js(a)
    write_xml(b, data)
    print("Wykonano!")
    
 def YMLtoXML(a, b):
    print("Zrozumiano. [.yml to .xml]")
    print("Próba utworzenia nowgo pliku")
    data = load_yml(a)
    write_xml(b, data)
    print("Wykonano!")
    
    
 def write_xml(a, data):
    data = {"root": data}
    xml_data = xmltodict.unparse(data)
    with open(a, 'w') as f:
        f.write(xml_data)
        
 
def pick():
    if file_extension_old == ".json":
        if file_extension_new == ".xml":
            JStoXML(a, b)
        if file_extension_new == ".yml":
            JStoYML(a, b)

    if file_extension_old == ".xml":
        if file_extension_new == ".json":
            XMLtoJS(a, b)
        if file_extension_new == ".yml":
            XMLtoYML(a, b)

    if file_extension_old == ".yml":
        if file_extension_new == ".json":
            YMLtoJS(a, b)
        if file_extension_new == ".xml":
            YMLtoXML(a, b)


verify_file()
pick()
