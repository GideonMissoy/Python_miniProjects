def feistel(input_str, num_rounds, round_keys, decrypt=False):
    # Convert the input string to an integer
    input_int = int(input_str, 2)

    # Split the input integer into two 4-bit halves
    left_half = (input_int >> 4) & 0b1111
    right_half = input_int & 0b1111

    # Perform the specified number of rounds
    for i in range(num_rounds):
        # Use the appropriate round key
        if decrypt:
            key = round_keys[num_rounds - i - 1]
        else:
            key = round_keys[i]

        # Compute the new right half using the round function
        new_right_half = right_half & key

        # Compute the new left half as the XOR of the old right half and the new right half
        new_left_half = left_half ^ new_right_half

        # Update the left and right halves for the next round
        left_half = right_half
        right_half = new_left_half

    # Combine the final left and right halves into an 8-bit output integer
    output_int = (right_half << 4) | left_half

    # Convert the output integer to an 8-bit binary string
    output_str = format(output_int, '08b')

    # Return the output string
    return output_str
