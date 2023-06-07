def load_yml(a):
    with open(a) as f:
        return {"root": yaml.safe_load(f)}
