import chardet

def detect_file_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw = file.read()
        result = chardet.detect(raw)
    return result['encoding']

if __name__ == "__main__":
    # This block will only run if the script is executed directly
    import sys
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        encoding = detect_file_encoding(file_path)
        print(f"Detected encoding for {file_path}: {encoding}")
    else:
        print("Please provide a file path as an argument.")