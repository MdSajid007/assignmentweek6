file_name = input("Enter a file name: ")

try:
    with open(file_name, 'r') as file:
        for line in file:
            print(line.upper(), end='')
            
except FileNotFoundError:
    print(f"Error! File '{file_name}' does not exist.")

