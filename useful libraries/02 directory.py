from pathlib import Path
import shutil

def create_directory(dir_path):
    """Create a directory if it doesn't exist."""
    path = Path(dir_path)
    path.mkdir(parents=True, exist_ok=True)
    print(f"✅ Directory '{dir_path}' created.")

def list_directory(dir_path):
    """List all files and subdirectories in a given path."""
    path = Path(dir_path)
    if path.exists() and path.is_dir():
        print(f"📂 Contents of '{dir_path}':")
        for item in path.iterdir():
            print("  -", item)
    else:
        print(f"⚠️ Directory '{dir_path}' does not exist.")

def delete_directory(dir_path):
    """Delete a directory and all its contents."""
    path = Path(dir_path)
    if path.exists() and path.is_dir():
        shutil.rmtree(dir_path)
        print(f"🗑️ Directory '{dir_path}' deleted.")
    else:
        print(f"⚠️ Directory '{dir_path}' does not exist.")

def copy_file(source, destination):
    """Copy a file from source to destination."""
    src_path = Path(source)
    dest_path = Path(destination)
    if src_path.exists() and src_path.is_file():
        shutil.copy(src_path, dest_path)
        print(f"✅ File copied from '{source}' to '{destination}'.")
    else:
        print(f"❌ Source file '{source}' does not exist.")

def move_file(source, destination):
    """Move or rename a file."""
    src_path = Path(source)
    dest_path = Path(destination)
    if src_path.exists() and src_path.is_file():
        src_path.rename(dest_path)
        print(f"🚀 File moved from '{source}' to '{destination}'.")
    else:
        print(f"❌ Source file '{source}' does not exist.")

def check_existence(path):
    """Check if a file or directory exists."""
    path_obj = Path(path)
    if path_obj.exists():
        print(f"✅ Path '{path}' exists.")
    else:
        print(f"⚠️ Path '{path}' does not exist.")

if __name__ == "__main__":
    # Example usage:
    create_directory("test_folder")
    list_directory(".")  # List contents of current directory
    check_existence("test_folder")
    copy_file("example.txt", "test_folder/example_copy.txt")
    move_file("test_folder/example_copy.txt", "example_moved.txt")
    delete_directory("test_folder")
