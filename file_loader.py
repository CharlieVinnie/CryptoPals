def load_file_as_string_list(file_path: str):
    with open(file_path, "r") as file:
        return [line.rstrip("\r\n") for line in file]

def load_file_as_single_string(file_path: str):
    return "".join(load_file_as_string_list(file_path))

def load_file_as_it_is(file_path: str):
    with open(file_path, "r") as file:
        return "".join(file.readlines())