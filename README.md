# input-validation-service

This microservice performs basic format validation on user input based on specified validation type. The service continuously checks the input file, input.txt. When content is detected, it processes the text and writes the validation results to the output file, output.txt.
Communication between main programs and this microservice is achieved through text files.


**How to programmatically REQUEST data from the microservice. Includes example calls.**
Instructions:
Step 1: Make sure that input_validate.py is running.
Step 2: Write a request into input.txt in the format “validator|value” where value is the user input, and the validator is “dollar”, “positive”, or “alpha”, depending on checking for valid dollar amount, positive number, or alphabetical respectively.

Dollar Amount Example call:
input_txt.write_text(f”dollar|{user_input}”)

Positive Number Example call:
input_txt.write_text(f”positive|{user_input}”)

Alphabetic Example call:
input_txt.write_text(f”alpha|{user_input}”)

**How to programmatically RECEIVE data from the microservice. Includes an example call.**
Instructions:
After processing the content in input.txt, the microservice writes results to output.txt as string “True” if valid input, or string “False” if invalid input.

Example call:.
output_txt.write_text(str(result))
Example response:
True
