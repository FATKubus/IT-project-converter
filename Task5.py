 def JStoYML(a, b):
    print("Zrozumiano. [.json to .yml]")
    print("Próba utworzenia nowgo pliku")
    data = load_js(a)
    write_yaml(b, data)
    print("Wykonano!")

 
def XMLtoYML(a, b):   
    print("Zrozumiano. [.xml to .yml]")
    print("Próba utworzenia nowgo pliku")
    data = load_xml(a)
    write_yaml(b, data)
    print("Wykonano!")
    
def write_yaml(a, data):
    with open(a, 'w') as f:
        yaml.dump(data, f)
