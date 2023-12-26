import hashlib

def get_file_hash(file_path: str, algorithm: str) -> str:
    with open(file_path, 'rb') as f:
        file_bytes = f.read()
        hash_object = hashlib.new(algorithm)
        hash_object.update(file_bytes)
        return hash_object.hexdigest()

file_path = 'D:/steganografi/example.docx'
algorithm = 'md5' # or 'sha1', 'crc32', etc.
hash_value = get_file_hash(file_path, algorithm)
print(f"Nilai hash dari file {file_path} adalah {hash_value}")