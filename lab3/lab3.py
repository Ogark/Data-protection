# Read the three intercepted hexadecimal messages
message1 = input().strip()
message2 = input().strip()
message3 = input().strip()

# Convert hexadecimal strings to byte arrays
m1 = bytes.fromhex(message1)
m2 = bytes.fromhex(message2)
m3 = bytes.fromhex(message3)

# Each message has the same length
n = len(m1)

# From the XOR process:
# m1 = M XOR A
# m2 = M XOR A XOR B
# m3 = M XOR B
# So: M = m1 XOR m2 XOR m3
clear_bytes = bytes([m1[i] ^ m2[i] ^ m3[i] for i in range(n)])

# Convert from bytes to ASCII text
print(clear_bytes.decode('ascii'))
