import sys

def feistel_encrypt(input_string, num_rounds, round_keys):
    left = input_string[:4]
    right = input_string[4:]

    for i in range(num_rounds):
        new_left = right
        new_right = int(left, 2) & int(round_keys[i], 2)
        left = new_left
        right = bin(new_right)[2:].zfill(4)

    return left + right

def feistel_decrypt(input_string, num_rounds, round_keys):
    left = input_string[:4]
    right = input_string[4:]

    for i in range(num_rounds):
        new_right = left
        new_left = int(left, 2) & int(round_keys[num_rounds-i-1], 2)
        left = bin(new_left)[2:].zfill(4)
        right = new_right

    return left + right

if __name__ == '__main__':
    input_string = sys.argv[2]
    num_rounds = int(sys.argv[3])
    round_keys = sys.argv[4:]

    if len(round_keys) != num_rounds:
        print("Error: Invalid number of round keys.")
        sys.exit(1)

    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        output = feistel_decrypt(input_string, num_rounds, round_keys)
    else:
        output = feistel_encrypt(input_string, num_rounds, round_keys)

    print(output[-8:])

