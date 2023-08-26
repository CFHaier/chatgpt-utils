import yaml

def read_instructions(path):
    raw = read_yaml(path)
    assert len(raw) > 0
    delimiter, instructions = list(raw.items())[0]
    assert isinstance(instructions, list)
    return delimiter, instructions


def read_yaml(path):
    # file containing instructions must be yaml
    file_extension = path.split(".")[-1]
    assert file_extension == "yaml" or file_extension == "yml"
    with open(path, 'r') as file:
        return yaml.safe_load(file)