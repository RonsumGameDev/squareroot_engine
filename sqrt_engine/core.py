"""
The Ultimate Digit-by-Digit Square Root Engine. This uses the classic Long division method of calculating square roots.
Author : Saksham (Ronsum) Dwivedi

For contributors:
n : The input number
places : The Decimal precision (how many numbers after decimal)
debug : This is to check the details of the calculation

def extract_pairs(num: str) -> list[int]
def compute_sqrt(n: int, places: int = 10, debug: bool = False) -> str:
"""

def extract_pairs(num):
    """ Break number string into 2-digit chunks from left to right """
    if len(num) % 2 != 0:
        num = '0' + num

    output = []
    index = 0
    while index < len(num):
        chunk = num[index : index+2]
        output.append(int(chunk))
        index += 2
    return output

def sqroot(n, places=10, debug=False):
    if n < 0:
        raise ValueError("Cannot take square root of negative number.")

    n_str = str(n)
    digit_chunks = extract_pairs(n_str)

    remainder = 0
    answer = ''

    # Initial approximation
    chunk = digit_chunks.pop(0)
    for guess in range(1, 10):
        if guess * guess > chunk:
            guess -= 1
            break

    base = guess
    answer += str(base)
    remainder = chunk - (base * base)
    divisor = base * 2

    if debug:
        print(f"[INIT] First digit: {base}, Remainder: {remainder}, Divisor : {divisor}")

    # Decimal start
    answer += '.'
    digit_chunks += [0] * (places * 2)

    for chunk in digit_chunks:
        remainder = remainder * 100 + chunk

        digit = 0
        while True:
            trial = (divisor * 10 + digit) * digit
            if trial > remainder:
                digit -= 1
                break
            digit += 1

        step_value = (divisor * 10 + digit) * digit
        remainder -= step_value
        divisor = divisor * 10 + 2 * digit
        answer += str(digit)

        if debug:
            print(f"[STEP] Chunk: {chunk}, Digit: {digit}, Subtract: {step_value}, Remainder: {remainder}, New Divisor: {divisor}")

    return answer
