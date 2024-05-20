import sys

def hex_to_byte(hex_str):
    try:
        # Try to convert the hex string to an integer (byte)
        return int(hex_str, 10)
    except ValueError:
        # If conversion fails, return 0
        return 0

def process_file(input_file, output_file):
    try:
        # Open and read the input file
        with open(input_file, 'r') as infile:
            lines = infile.readlines()
        
        # Initialize a list to hold the converted bytes
        output_bytes = []
        
        # Process each line
        for line in lines:
            # Remove any surrounding whitespace (like newlines)
            line = line.strip()
            if not line:
                continue
            # Split the line by commas
            hex_values = line.split(',')
            # Convert each hex value to a byte and store it in the list
            for hex_value in hex_values:
                byte = hex_to_byte(hex_value)
                output_bytes.append(byte)
        
        # Write the bytes to the output file
        with open(output_file, 'wb') as outfile:
            outfile.write(bytearray(output_bytes))
        
        print(f'Successfully processed and saved to {output_file}')
    except Exception as e:
        print(f'Error: {e}')
print("\x1bc\x1b[43;37m")
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python script.py <input_file> <output_file>')
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        process_file(input_file, output_file)

