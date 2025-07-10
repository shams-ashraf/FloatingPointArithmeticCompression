from decimal import Decimal, getcontext
import struct

getcontext().prec = 200

def get_frequency(data):
    frequency_dict = {}
    for char in data:
        frequency_dict[char] = frequency_dict.get(char, 0) + 1
    for key in frequency_dict.keys():
        frequency_dict[key] = Decimal(frequency_dict[key]) / Decimal(len(data))
    return frequency_dict

def generate_ranges(data):
    freq = get_frequency(data)
    start = Decimal(0)
    dictionary = {}
    sorted_chars = sorted(freq.keys())
    for key in sorted_chars:
        value = freq[key]
        dictionary[key] = (start, start + value)
        start += value
    return dictionary

def compress(data, file_name):
    ranges = generate_ranges(data)
    low = Decimal(0)
    high = Decimal(1)

    for char in data:
        range_width = high - low
        high = low + range_width * ranges[char][1]
        low = low + range_width * ranges[char][0]

    compressed_value = (low + high) / 2
    write_decimal_to_binary(compressed_value, file_name)
    return ranges

def decompress(float_number, ranges, length):
    answer = ''
    cnt = length
    while cnt > 0:
        for key in ranges.keys():
            if ranges[key][0] <= float_number <= ranges[key][1]:
                answer += key
                float_number = (float_number - ranges[key][0]) / (ranges[key][1] - ranges[key][0])
                break
        cnt -= 1
    return answer

def write_decimal_to_binary(data, filename):
    float_data = float(data)  
    with open(filename, 'wb') as file:
        file.write(struct.pack('d', float_data))


def read_decimal_from_binary(filename):
    with open(filename, 'rb') as file:
        float_data = struct.unpack('d', file.read(8))[0] 
        return Decimal(float_data)

def compress_mode():
    output_file_name = "floating/compressed.bin"

    with open("floating/input.txt", 'r') as input_file:
        string_to_compress = input_file.read().strip()

    ranges = compress(string_to_compress, output_file_name)

    compressed_float = read_decimal_from_binary(output_file_name)
    print("Compressed value:", compressed_float)

    with open("floating/ranges.txt", "w") as ranges_file:
        for char, (low, high) in ranges.items():
            ranges_file.write(f"{char}: {low}, {high}\n")

def decompress_mode():
    compressed_file_name = "floating/compressed.bin"
    ranges_name = "floating/ranges.txt"
    decompressed_file_name = "floating/decompressed.txt"

    ranges = {}
    with open(ranges_name, "r") as ranges_file:
        for line in ranges_file:
            char, values = line.split(":")
            low, high = values.split(",")
            ranges[char] = (Decimal(low.strip()), Decimal(high.strip()))

    compressed_float = read_decimal_from_binary(compressed_file_name)

    length_of_string = int(input("Enter the length of the string to be decompressed: "))
    decompressed_string = decompress(compressed_float, ranges, length_of_string)

    with open(decompressed_file_name, "w") as decompressed_file:
        decompressed_file.write(decompressed_string)

def main():
    while True:
        print("\nChoose an option:")
        print("1. Compress string")
        print("2. Decompress string")
        choice = input("Enter your choice: ")

        if choice == '1':
            compress_mode()
        elif choice == '2':
            decompress_mode()
            break

if __name__ == "__main__":
    main()
