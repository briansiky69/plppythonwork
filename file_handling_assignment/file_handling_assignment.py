def write_to_file(filename, content):
  """
  Writes content to a file in write mode.

  Args:
      filename: The name of the file to write to.
      content: The content to write to the file (string or list of strings).
  """
  try:
    with open(filename, 'w') as file:
      if isinstance(content, list):
        file.writelines(content)
      else:
        file.write(content + "\n")
    print(f"Successfully wrote to {filename}")
  except (IOError, OSError) as e:
    print(f"Error writing to file: {e}")

def read_from_file(filename):
  """
  Reads the contents of a file and displays them on the console.

  Args:
      filename: The name of the file to read from.
  """
  try:
    with open(filename, 'r') as file:
      content = file.read()
      print(f"Contents of {filename}:\n{content}")
  except FileNotFoundError:
    print(f"File '{filename}' not found.")
  except (IOError, OSError) as e:
    print(f"Error reading from file: {e}")

def append_to_file(filename, content):
  """
  Appends content to a file in append mode.

  Args:
      filename: The name of the file to append to.
      content: The content to append to the file (string or list of strings).
  """
  try:
    with open(filename, 'a') as file:
      if isinstance(content, list):
        file.writelines(content)
      else:
        file.write(content + "\n")
    print(f"Successfully appended to {filename}")
  except (IOError, OSError) as e:
    print(f"Error appending to file: {e}")

# Create a new file and write some content
write_to_file("my_file.txt", ["Line 1: This is some text.\n", "Line 2: You can write numbers too: 42\n", "Line 3: And mix data types!\n"])

# Read the contents of the file
read_from_file("my_file.txt")

# Append more content to the file
append_to_file("my_file.txt", ["Line 4: This is appended content.\n", "Line 5: You can add more lines easily.\n", "Line 6: The file grows bigger! \n"])

# Try reading a non-existent file (shows error handling)
read_from_file("non_existent_file.txt")
