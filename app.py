"""
Script to strip values from JSON/dict data and replace with 0s.
Preserves the structure while removing actual data values.

USAGE:
1. Save your API response to a file called 'input.json' in the same directory
2. Run: python app.py
3. The stripped JSON will be printed to console and saved to 'output.json'
"""

import json
import sys


def strip_values(obj):
    """
    Recursively strip values from a data structure, preserving data types.
    
    Args:
        obj: The object to process (dict, list, or primitive)
    
    Returns:
        The same structure with values stripped but types preserved:
        - Booleans remain as True/False
        - None/null remains as None
        - Numbers become 0
        - Strings become ""
    """
    if isinstance(obj, dict):
        return {key: strip_values(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [strip_values(item) for item in obj]
    elif isinstance(obj, bool):
        # Must check bool before int/float since bool is a subclass of int
        return obj
    elif obj is None:
        return None
    elif isinstance(obj, (int, float)):
        return 0
    elif isinstance(obj, str):
        return ""
    else:
        # Fallback for any other type
        return 0


def main():
    """Main function to read JSON from file, strip values, and output result."""
    
    input_file = "input.json"
    
    # Check if file exists
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: '{input_file}' not found in the current directory.")
        print("\nPlease create a file called 'input.json' and paste your API response into it.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        print(f"\nThe JSON in '{input_file}' is not valid.")
        print("Make sure you copied the complete API response.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    # Strip the values
    stripped_data = strip_values(data)
    
    # Output the result
    print(json.dumps(stripped_data, indent=2))
    
    # Optionally save to output file
    try:
        with open('output.json', 'w', encoding='utf-8') as f:
            json.dump(stripped_data, f, indent=2)
        print("\n✓ Stripped JSON also saved to 'output.json'", file=sys.stderr)
    except Exception as e:
        print(f"\n⚠ Could not save output file: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
