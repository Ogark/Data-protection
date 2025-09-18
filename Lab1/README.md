# Enigma Machine Simulator

This is a simplified simulation of the Enigma machine used during World War II.

Supports:

* Encoding messages with Caesar shift + 3 rotors
* Decoding messages by reversing the process

---

## Example 1

Input:
ENCODE
4
BDFHJLCPRTXVZNYEIWGAKMUSQO
AJDKSIRUXBLHWTMCQGZNPYFVOE
EKMFLGDQVZNTOWYHXUSPAIBRCJ
AAA

### Steps (Encoding)

| Step | Operation    | Input | Output |
| ---- | ------------ | ----- | ------ |
| 1    | Caesar shift | AAA   | EFG    |
| 2    | Rotor I      | EFG   | JLC    |
| 3    | Rotor II     | JLC   | BHD    |
| 4    | Rotor III    | BHD   | KQF    |

**Encoded message:** KQF

### Steps (Decoding)

| Step | Operation            | Input | Output |
| ---- | -------------------- | ----- | ------ |
| 1    | Rotor III reverse    | KQF   | BHD    |
| 2    | Rotor II reverse     | BHD   | JLC    |
| 3    | Rotor I reverse      | JLC   | EFG    |
| 4    | Caesar shift reverse | EFG   | AAA    |

**Decoded message:** AAA

---

## Example 2

Input:
ENCODE
1
BDFHJLCPRTXVZNYEIWGAKMUSQO
AJDKSIRUXBLHWTMCQGZNPYFVOE
EKMFLGDQVZNTOWYHXUSPAIBRCJ
HELLO

### Steps (Encoding)

| Step | Operation    | Input | Output |
| ---- | ------------ | ----- | ------ |
| 1    | Caesar shift | HELLO | IFMPS  |
| 2    | Rotor I      | IFMPS | PJVUZ  |
| 3    | Rotor II     | PJVUZ | WCKYA  |
| 4    | Rotor III    | WCKYA | FIVRG  |

**Encoded message:** FIVRG

### Steps (Decoding)

| Step | Operation            | Input | Output |
| ---- | -------------------- | ----- | ------ |
| 1    | Rotor III reverse    | FIVRG | WCKYA  |
| 2    | Rotor II reverse     | WCKYA | PJVUZ  |
| 3    | Rotor I reverse      | PJVUZ | IFMPS  |
| 4    | Caesar shift reverse | IFMPS | HELLO  |

**Decoded message:** HELLO

---

## Usage

Run the program and follow the prompts:

```
ENCODE or DECODE
Starting shift (0-25)
Rotor I
Rotor II
Rotor III
Message
```

This implementation demonstrates basic encryption primitives:

* Substitution (rotors)
* Permutation (Caesar shift with increment)

Supports both encoding and decoding in a practical, step-by-step way.
