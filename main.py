from pathlib import Path
import time

"""
Example Main Program
"""

input_txt = Path("input.txt")
output_txt = Path("output.txt")

user_input = input("Enter dollar amount: ")

# clear any old output
output_txt.write_text("")

input_txt.write_text(user_input)

while True:
  time.sleep(0.1)
  response = output_txt.read_text().strip()
  if response:
    print(response)
    break