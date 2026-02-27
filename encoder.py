def encode(input_path, output_path):

    # 1. Reading and storing the file content
    try:
        with open(input_path, 'r') as f:
            raw_lines = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("Error: Input file not found.")
        return

    # 2. Reading and storing number of lines & words
    num_of_lines = len(raw_lines)

    # 3. Writing output to file

    with open(output_path, 'w') as f:
        f.write("3^" + raw_lines[0] + "\n")
        for i in range(1, num_of_lines):
            f.write("1<" + raw_lines[i] + "\n")

# Execute functions
encode('input.txt', 'output.box')
print("File Converted to Box Successfully")
