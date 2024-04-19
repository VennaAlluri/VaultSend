# Encoding an image to Base64 without using built-in functions

# Define Base64 characters
base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# Function to encode binary data as Base64
def encode_base64(data):
    result = []
    padding = 0
    for i in range(0, len(data), 3):
        chunk = data[i:i+3]
        if len(chunk) < 3:
            padding = 3 - len(chunk)
            chunk += b'\x00' * padding
        
        # Convert 3 bytes to a 24-bit integer
        value = int.from_bytes(chunk, byteorder='big')
        
        # Split the 24-bit integer into four 6-bit values
        for j in range(4):
            index = (value >> (18 - j * 6)) & 0x3F
            result.append(base64_chars[index])
    
    # Add padding characters if necessary
    for _ in range(padding):
        result[-1] = '='
    
    return ''.join(result)