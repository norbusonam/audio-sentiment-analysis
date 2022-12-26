import sys
import os
from dotenv import load_dotenv
import openai

# load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# arguments
statement = sys.argv[1].strip()

# prompt
prompt = f"Give this statement: \"{statement}\" a score from 0 to 100. 0 is negative, 100 is positive.\n\n"

# completion
completion = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
)

# print result
print(completion["choices"][0]["text"].strip())