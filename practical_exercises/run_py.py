import os
import subprocess

def list_py_files():
    """List all .py files in the current directory."""
    return [f for f in os.listdir() if f.endswith('.py')]

def select_file(files):
    """Prompt the user to select a file from the list."""
    if not files:
        print("No .py files found in the current directory.")
        return None

    print("Select a .py file to run:")
    for i, file in enumerate(files):
        print(f"{i + 1}. {file}")

    try:
        choice = int(input("Enter the number of the file: ")) - 1
        if 0 <= choice < len(files):
            return files[choice]
        else:
            print("Invalid selection.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

def run_python_file(file):
    """Run the selected Python file using the default Python interpreter."""
    if file:
        try:
            subprocess.run(['python', file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running {file}: {e}")
        except FileNotFoundError:
            print("Python interpreter not found. Make sure Python is installed and in your PATH.")

def main():
    py_files = list_py_files()
    selected_file = select_file(py_files)
    run_python_file(selected_file)

if __name__ == "__main__":
    main()