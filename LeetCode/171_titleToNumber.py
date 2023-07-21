def titleToNumber(columnTitle: str) -> int:

    initial = ord('A') - 1
    alphabet = {chr(i): i - initial for i in range(ord('A'), ord('Z') + 1)}

    total = 0
    for index, letter in enumerate(columnTitle[::-1]):
        power = index
        number = alphabet[letter]
        total += number * (26 ** power)

    return total