from pathlib import Path
import re
import time

input_txt = Path("input.txt")
input_txt.touch()
output_txt = Path("output.txt")
output_txt.touch()

# dollar regex; optional $ and .00
dollar_pattern = r'^\$?-?(\d{1,3}(,\d{3})*|\d+)(\.\d{2})?$'

def is_dollar(input):
  # Matches input to the dollar regex. Returns True if valid dollar amount; else False.
  return bool(re.match(dollar_pattern, input.strip()))

# Checks input.txt for content; validates content & writes to output.txt when detected
while True:
  content = input_txt.read_text().strip()
  if content:
    time.sleep(0.9)
    if is_dollar(content):
      output_txt.write_text("True")
    else:
      output_txt.write_text("False")
  input_txt.write_text("")