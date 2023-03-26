import argparse

def feistel(input, rounds, keys, decrypt=False):
    # Split the input into left and right halves
    left, right = input[:4], input[4:]

    # Perform the specified number of rounds
    for i in range(rounds):
        # Apply the round function, which is a bitwise AND operation
        if not decrypt:
            result = int(right) & int(keys[i])
        else:
            result = int(left) & int(keys[rounds - i - 1])
        
        # Swap the left and right halves and XOR the result with the left half
        left, right = right, str(int(left) ^ result).zfill(4)
    
    # Concatenate the left and right halves and return the result
    return left + right

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Feistel cipher program')
    parser.add_argument('input', type=str, help='an 8-bit input string')
    parser.add_argument('rounds', type=int, help='the number of rounds to perform')
    parser.add_argument('keys', type=str, nargs='+', help='the round keys')
    parser.add_argument('-d', '--decrypt', action='store_true', help='perform decryption')
    args = parser.parse_args()

    # Validate the input length
    if len(args.input) != 8:
        print('Input string must be 8 bits')
        exit()

    # Validate the number of keys
    if len(args.keys) != args.rounds:
        print('Number of keys must match number of rounds')
        exit()

    # Encrypt or decrypt the input
    result = feistel(args.input, args.rounds, args.keys, args.decrypt)

    # Print the result
    print(result)

