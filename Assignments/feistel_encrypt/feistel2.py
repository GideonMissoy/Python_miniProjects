import sys

def feistel_round(input_string, round_key):
    left = input_string[:4]
    right = input_string[4:]

    new_left = right
    new_right = int(left, 2) & int(round_key, 2)

    return new_left + bin(new_right)[2:].zfill(4)

def feistel_encrypt(input_string, num_rounds, round_keys):
    output = input_string

    for i in range(num_rounds):
        output = feistel_round(output, round_keys[i])

    return output

def feistel_decrypt(input_string, num_rounds, round_keys):
    output = input_string

    for i in reversed(range(num_rounds)):
        output = feistel_round(output, round_keys[i])

    return output

if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) < 3:
        print("Usage: python3 feistel.py [-d] input_string num_rounds round_key_1 round_key_2 ... round_key_n")
        sys.exit()

    decrypt_flag = False
    if args[0] == "-d":
        decrypt_flag = True
        args.pop(0)

    input_string = args[0]
    num_rounds = int(args[1])
    round_keys = args[2:]

    if len(round_keys) != num_rounds:
        print("Error: Number of round keys must match number of rounds.")
        sys.exit()

    if decrypt_flag:
        output = feistel_decrypt(input_string, num_rounds, round_keys)
    else:
        output = feistel_encrypt(input_string, num_rounds, round_keys)

    print(output[-8:])

