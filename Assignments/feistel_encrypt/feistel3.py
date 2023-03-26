import sys

def feistel_round(input_string, round_key):
    left = input_string[:4]
    right = input_string[4:]

    new_left = right
    new_right = int(left, 2) & int(round_key, 2)

    return new_left + bin(new_right)[2:].zfill(4)

def feistel_encrypt(input_string, round_keys):
    num_rounds = len(round_keys)
    for i in range(num_rounds):
        input_string = feistel_round(input_string, round_keys[i])

    return input_string

def feistel_decrypt(input_string, round_keys):
    num_rounds = len(round_keys)
    for i in range(num_rounds):
        input_string = feistel_round(input_string, round_keys[num_rounds-i-1])

    return input_string

if __name__ == '__main__':
    decrypt_mode = False
    input_string = ''
    round_keys = []

    # Parse command line arguments
    for arg in sys.argv[1:]:
        if arg == '-d':
            decrypt_mode = True
        elif len(input_string) == 0:
            input_string = arg
        else:
            round_keys.append(arg)

    # Check input validity
    if len(input_string) != 8:
        print('Error: Input string must be 8 bits long')
        sys.exit(1)

    if len(round_keys) == 0:
        print('Error: No round keys provided')
        sys.exit(1)

    # Perform encryption or decryption
    if decrypt_mode:
        output = feistel_decrypt(input_string, round_keys)
    else:
        output = feistel_encrypt(input_string, round_keys)

    # Print the result
    print(output[-8:])

