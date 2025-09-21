import time

def time_method(method_func, *args):
    start = time.time()
    method_func(*args)
    end = time.time()
    return end - start

def method_read_all(file_in, file_out):
    with open(file_in, 'r') as infile, open(file_out, 'w') as outfile:
        for line in infile:
            num = int(line.strip())
            outfile.write(f"{num*2}\n")

def method_read_line_by_line(file_in, file_out):
    with open(file_in, 'r') as infile, open(file_out, 'w') as outfile:
        for line in infile:
            num = int(line.strip())
            outfile.write(f"{num * 2}\n")

def method_split_in_two(file_in, file_out):
    with open(file_in, 'r') as f:
        lines = f.readlines()
    split=len(lines) // 2

    first_half = [int(line.strip()) * 2 for line in lines[:split]]
    second_half = [int(line.strip()) * 2 for line in lines[split:]]

    with open(file_out, 'w') as f:
        f.writelines(f"{num}\n" for num in first_half + second_half)


if __name__ == "__main__":
    infile = "file1.txt"
    methods = [
        (method_read_all, "Read all into memory"),
        (method_read_line_by_line, "Line by line"),
        (method_split_in_two, "Split in two halves")
    ]

    for method, description in methods:
        outfile = f"output_{description.replace(' ', '_').lower()}.txt"
        elapsed_time = time_method(method, infile, outfile)
        print(f"{description}: {elapsed_time:.6f} seconds")