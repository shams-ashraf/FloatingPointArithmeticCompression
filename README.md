# FloatingPointArithmeticCompression 🔢📦

A Python implementation of **Arithmetic Coding** using floating-point precision for lossless text compression and decompression.

---

## 📌 Overview

This tool demonstrates arithmetic compression by encoding a string into a single floating-point number and storing it in a binary file. It also supports accurate decompression using stored frequency ranges.

- Uses the `decimal` module for high-precision calculations.
- Stores the encoded float using `struct.pack`.
- Supports saving/loading character ranges for decompression.
- Easy command-line interface for compression and decompression modes.

---

## 🧠 How It Works

1. **Compression**
   - Reads a text string from `input.txt`
   - Calculates character probabilities
   - Builds interval ranges for each character
   - Compresses string into a float in range [0, 1)
   - Saves:
     - Compressed float to `floating/compressed.bin`
     - Ranges to `floating/ranges.txt`

2. **Decompression**
   - Loads compressed float from binary file
   - Loads ranges from file
   - Asks user for original string length
   - Reconstructs original string using inverse arithmetic decoding

---

Choose an option:
1. Compress string
2. Decompress string
Enter your choice:

📦 Compression
Add your string to floating/input.txt
Run:
Choose 1 to compress
Output:
floating/compressed.bin
floating/ranges.txt

🧩 Decompression
Run:
Choose 2 to decompress
Enter original string length (e.g., 12)
Output:
floating/decompressed.txt
