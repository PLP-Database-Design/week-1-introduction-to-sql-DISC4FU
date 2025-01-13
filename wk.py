
def modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content (for example, converting to uppercase)
        modified_content = content.upper()
        
        # Open the output file in write mode and write the modified content
        with open(output_filename, 'w') as new_file:
            new_file.write(modified_content)
        
        print(f"File successfully modified and saved as {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' cannot be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    input_filename = input("Please enter the filename to read: ")
    output_filename = input("Please enter the filename to save the modified content: ")
    
    modify_file(input_filename, output_filename)

if __name__ == "__main__":
    main()
