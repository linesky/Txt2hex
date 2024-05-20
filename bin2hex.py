import sys

def convert_to_hex_and_save(input_file, output_file):
    try:
        # Open the input file in binary mode
        with open(input_file, 'rb') as infile:
            # Read the entire file content as bytes
            byte_data = infile.read()
        
        # Initialize an empty list to store the output lines
        output_lines = []
        
        # Iterate over the byte data in chunks of 32 bytes
        for i in range(0, len(byte_data), 32):
            chunk = byte_data[i:i + 32]
            # Convert each byte to hexadecimal and then to decimal
            hex_values = [f'{byte:02X}' for byte in chunk]
            #decimal_values = [str(int(hv, 16)) for hv in hex_values]
            # Join the decimal values with commas
            output_lines.append(','.join(hex_values))
        
        # Write the output lines to the output file
        with open(output_file, 'w') as outfile:
            outfile.write('\n'.join(output_lines))
        
        print(f'Successfully converted and saved to {output_file}')
    except Exception as e:
        print(f'Error: {e}')

print("\x1bc\x1b[43;37m")
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python script.py <input_file> <output_file>')
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convert_to_hex_and_save(input_file, output_file)

