import argparse

def feistel_round(left, right, key):
    # Apply the round function, which is a bitwise AND operation
    result = int(right, 2) & int(key, 2)
    
    # Swap the left and right halves and XOR the result with the left half
    return right, "{0:b}".format(int(left, 2) ^ result).zfill(4)

def feistel_encrypt(input, rounds, keys):
    # Split the input into left and right halves
    left, right = input[:4], input[4:]

    # Perform the specified number of rounds
    for i in range(rounds):
        left, right = feistel_round(left, right, keys[i])
    
    # Concatenate the left and right halves and return the result
    return left + right

def feistel_decrypt(input, rounds, keys):
    # Split the input into left and right halves
    left, right = input[:4], input[4:]

    # Perform the specified number of rounds in reverse order
    for i in reversed(range(rounds)):
        left, right = feistel_round(left, right, keys[i])
    
    # Concatenate the left and right halves and return the result
    return left + right

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Feistel cipher program')
    parser.add_argument('input', type=str, help='an 8-bit binary input string')
    parser.add_argument('rounds', type=int, help='the number of rounds to perform')
    parser.add_argument('keys', type=str, nargs='+', help='the round keys in binary')
    parser.add_argument('-d', '--decrypt', action='store_true', help='decrypt the input using the specified keys')
    args = parser.parse_args()

    # Validate the input length
    if len(args.input) != 8:
        print('Input string must be 8 bits')
        exit()

    # Validate the input format
    if not all(c in '01' for c in args.input):
        print('Input string must consist only of 0s and 1s')
        exit()

    # Validate the number of keys
    if len(args.keys) != args.rounds:
        print('Number of keys must match number of rounds')
        exit()

    # Encrypt or decrypt the input using the specified round keys
    if args.decrypt:
        decrypted = feistel_decrypt(args.input, args.rounds, args.keys)
        print('Decrypted:', decrypted)

        # Encrypt the decrypted output using the same keys and verify that it matches the original input
        encrypted = feistel_encrypt(decrypted, args.rounds, args.keys)
        if encrypted == args.input:
            print('Original input:', args.input)
        else:
            print('Error: Decrypted output does not match original input')
    else:
        encrypted = feistel_encrypt(args.input, args.rounds, args.keys)
        print('Encrypted:', encrypted)

        # Decrypt the encrypted output using the same keys and verify that it matches the original input
        decrypted = feistel_decrypt(encrypted, args.rounds, args.keys)
        if decrypted == args.input:
            print('Original input:', args.input)
        else:
            print('Error: Decrypted output does not match original input')

