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

def is_positive(input):
  try:
    return float(input) > 0
  except:
    return False
  
def is_alpha(input):
  return input.isalpha()

# Checks input.txt for content; processes content based on validator & writes to output.txt when detected
while True:
  content = input_txt.read_text().strip()
  if content:
    try:
      validator, value = content.split("|", 1)

      if validator == "dollar":
        result = is_dollar(value)
      elif validator == "positive":
        result = is_positive(value)
      elif validator == "alpha":
        result = is_alpha(value)
      else:
        result = False
      output_txt.write_text(str(result))

    except:
      output_txt.write_text("False")

    # clear input.txt
    input_txt.write_text("")
  time.sleep(0.1)