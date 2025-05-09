def grep(file, text):
    lines_matching = []
    with open(file, "r") as f:
        for line in f:
            if text in line:
                lines_matching.append(line)
    return lines_matching


if __name__ == "__main__":
    filename = input("Enter file name: ")
    search_term = input("Enter search term: ")

    try:
        lines = grep(filename, search_term)
        for line in lines:
            print(line, end="")
    except FileNotFoundError:
        print(f"File {filename} does not exist")
