import hashlib
import os

def calculate_sha256(file_path):
    """Calculates the SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: An exception occurred - {e}"

if __name__ == "__main__":
    file_to_hash = "AAD_v5.0.md"
    # Säkerställ att skriptet körs från samma mapp som AAD_v5.0.md
    # eller justera sökvägen till file_to_hash vid behov.
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, file_to_hash)
    if not os.path.exists(file_path) and script_dir == "": # Körs från samma mapp, filen finns inte
         file_path = file_to_hash


    print(f"Beräknar SHA256-hash för: {os.path.abspath(file_path)}")
    hash_value = calculate_sha256(file_path)
    print(f"SHA256: {hash_value}") 