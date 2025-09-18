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
