from pathlib import Path
import time

input_txt = Path("input.txt")
output_txt = Path("output.txt")

# Valid Dollar Amount Check
user_input = input("Enter dollar amount: ")
input_txt.write_text(f"dollar|{user_input}")

# Positive Number Check
#user_input = input("Enter number: ")
#input_txt.write_text(f"positive|{user_input}")

# Alphabetical Check
#user_input = input("Enter word: ")
#input_txt.write_text(f"alpha|{user_input}")

while True:
  time.sleep(0.1)
  response = output_txt.read_text().strip()
  if response:
    print(response)
    # clear output.txt
    output_txt.write_text("")
    break