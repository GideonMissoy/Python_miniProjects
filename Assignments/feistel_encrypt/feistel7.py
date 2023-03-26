import argparse

def feistel_encrypt(input, rounds, keys):
    # Split the input into left and right halves
    left, right = input[:4], input[4:]

    # Perform the specified number of rounds
    for i in range(rounds):
        # Apply the round function, which is a bitwise AND operation
        result = int(right, 2) & int(keys[i], 2)
        
        # Swap the left and right halves and XOR the result with the left half
        left, right = right, "{0:b}".format(int(left, 2) ^ result).zfill(4)
    
    # Concatenate the left and right halves and return the result
    return left + right

def feistel_decrypt(input, rounds, keys):
    # Split the input into left and right halves
    left, right = input[:4], input[4:]

    # Perform the specified number of rounds
    for i in range(rounds):
        # Apply the round function, which is a bitwise AND operation
        result = int(left, 2) & int(keys[rounds - i - 1], 2)
        
        # Swap the left and right halves and XOR the result with the right half
        right, left = left, "{0:b}".format(int(right, 2) ^ result).zfill(4)
    
    # Concatenate the left and right halves and return the result
    return left + right

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Feistel cipher program')
    parser.add_argument('input', type=str, help='an 8-bit binary input string')
    parser.add_argument('rounds', type=int, help='the number of rounds to perform')
    parser.add_argument('keys', type=str, nargs='+', help='the round keys in binary')
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

    # Encrypt the input using the specified round keys
    encrypted = feistel_encrypt(args.input, args.rounds, args.keys)

    # Decrypt the encrypted input using the same round keys
    decrypted = feistel_decrypt(encrypted, args.rounds, list(reversed(args.keys)))

    # Print the decrypted string
    print(decrypted)

    # Check that encrypting and then decrypting the same string with the same keys gives the original string
    if decrypted == args.input:
        print('Encryption and decryption successful')
    else:
        print('Encryption and decryption failed')

