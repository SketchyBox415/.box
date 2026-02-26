def read_file_data(input_path, output_path):

    # 1. Reading and storing the file content
    try:
        with open(input_path, 'r') as f:
            raw_lines = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("Error: Input file not found.")
        return

def num_of_lines():

    # 2. Reading and storing number of lines & words
    global raw_lines
    num_of_lines = len(raw_lines)

def write_output_to_file():

    # 3. Writing output to file

    global output_path, num_of_lines
    with open(output_path, 'w') as f:
        f.write("3^" + raw_lines[0] + "\n")
        for i in range(1, num_of_lines):
            f.write("1<" + raw_lines[i] + "\n")

# Execute functions
read_file_data('input.txt', 'output.box')
num_of_lines()
write_output_to_file()
print("File Converted to Box Successfully")
