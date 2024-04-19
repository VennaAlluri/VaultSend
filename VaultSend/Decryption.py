# Decoding Base64 data and saving as an image without using built-in functions


# Reverse mapping of Base64 characters
base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
base64_chars_rev = {char: i for i, char in enumerate(base64_chars)}

# Function to decode Base64 data to binary
def decode_base64(data):
    result = bytearray()
    padding = data.count('=')
    data = data.replace('=', '')  # Remove padding characters
    
    for i in range(0, len(data), 4):
        chunk = data[i:i+4]
        
        # Convert 4 Base64 characters to a 24-bit integer
        value = 0
        for j, char in enumerate(chunk):
            value += base64_chars_rev[char] << (18 - j * 6)
        
        # Split the 24-bit integer into three 8-bit values
        for j in range(2, -1, -1):
            byte = (value >> (j * 8)) & 0xFF
            result.append(byte)
    
    return bytes(result[:-padding])
