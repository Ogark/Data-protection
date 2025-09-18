# Enigma Machine Simulator

This is a simplified simulation of the **Enigma machine**, the famous encryption device used by Germans during World War II.

The program supports:

- **Encoding** messages using a Caesar shift with incrementing numbers and 3 rotors.
- **Decoding** messages by reversing the process.

## How It Works

1. **Caesar Shift with Increment**  
   Each letter is shifted by a starting number, incrementing by 1 for each subsequent letter.  
   Example: `AAA` with shift `4` → `EFG`

2. **Rotor Substitution**  
   The message passes through 3 rotors (substitution tables). Each rotor replaces letters according to its mapping.  
   Example rotors:

3. **Final Encoded Message**  
After passing all rotors, the encoded message is ready for transmission.

## Usage

Run the program and follow the prompts:

# Enigma Machine Simulator

This repository contains a **simplified simulation of the Enigma machine**, the famous encryption device used by Germans during World War II.  

The program supports both **encoding** and **decoding** messages using:

- Caesar shift with incrementing numbers
- Three substitution rotors

---

## How the Task Was Solved

The solution follows these steps:

### 1️⃣ Caesar Shift with Increment

Each letter in the message is shifted by a starting number, and for each next letter, the shift is incremented by 1.  
This simulates the "stepping" mechanism of the Enigma machine.

**Example:**  

- First letter: A + 4 → E  
- Second letter: A + 4 + 1 → F  
- Third letter: A + 4 + 1 + 1 → G  

Result after Caesar shift: `EFG`

---

### 2️⃣ Rotor Substitution

After the Caesar shift, the letters pass sequentially through **three rotors**, each of which is a substitution table of the alphabet.

**Example rotors from the task:**

Each rotor replaces the letter according to its position in the alphabet.

**Continuing the example:**
- Input to Rotor I: `EFG`  
  - E → J  
  - F → L  
  - G → C  
  Result: `JLC`

- Input to Rotor II: `JLC`  
  - J → B  
  - L → H  
  - C → D  
  Result: `BHD`

- Input to Rotor III: `BHD`  
  - B → K  
  - H → Q  
  - D → F  
  Result: `KQF` (final encoded message)

---

### 3️⃣ Decoding

Decoding works in **reverse order**:

1. Pass the encoded message through the **rotors in reverse**, using the inverse substitution.  
2. Apply the **Caesar shift backwards**, subtracting the incrementing values.

---

## Examples

### Example 1

**Input:**

**Steps:**
1. Caesar shift: `AAA` → `EFG`  
2. Rotor I: `EFG` → `JLC`  
3. Rotor II: `JLC` → `BHD`  
4. Rotor III: `BHD` → `KQF`  

**Output:**

**Decoding KQF back:**
1. Rotor III reverse: `KQF` → `BHD`  
2. Rotor II reverse: `BHD` → `JLC`  
3. Rotor I reverse: `JLC` → `EFG`  
4. Caesar shift reverse: `EFG` → `AAA`  

**Recovered message:** `AAA`

---

### Example 2

**Input:**

**Steps:**
1. Caesar shift with increment: `HELLO` → `IFMPS`  
2. Rotor I: `IFMPS` → `PJVUZ`  
3. Rotor II: `PJVUZ` → `WCKYA`  
4. Rotor III: `WCKYA` → `FIVRG`  

**Output:**
