def read_file(filename=""):

    """Reads a file and returns its content."""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
