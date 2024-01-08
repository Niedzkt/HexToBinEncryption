def hex_to_bin(hex_file_path, bin_file_path):
    with open(hex_file_path, 'r') as file:
        hex_data = file.readlines()

    cleaned_hex = ''.join(line[9:49].strip() for line in hex_data)

    bin_data = bytes.fromhex(cleaned_hex)

    with open(bin_file_path, 'wb') as file:
        file.write(bin_data)

hex_to_bin('input file path', 'output file path')
