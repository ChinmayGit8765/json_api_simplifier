"""
Script to strip values from JSON/dict data and replace with 0s.
Preserves the structure while removing actual data values.
"""

import json

# PASTE YOUR API DATA HERE
json_to_be_stripped = {
  "abc": {
    "def": {
      "qw": "ert",
      "be": "rt"
    },
    "fd": {
      "xyz": 123,
      "items": ["a", "b", "c"]
    }
  }
}


def strip_values(obj):
    """
    Recursively strip values from a data structure, replacing with 0.
    
    Args:
        obj: The object to process (dict, list, or primitive)
    
    Returns:
        The same structure with all leaf values replaced by 0
    """
    if isinstance(obj, dict):
        return {key: strip_values(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [strip_values(item) for item in obj]
    else:
        # Replace any primitive value (string, number, bool, null) with 0
        return 0


def main():
    """Main function to strip values and output result."""
    
    # Strip the values
    stripped_data = strip_values(json_to_be_stripped)
    
    # Output the result
    print(json.dumps(stripped_data, indent=2))


if __name__ == "__main__":
    main()
