import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import concurrent.futures
import time

# variables
debug = True


def read_file(filename):
  with open(filename, "r") as f:
    return f.read()


def generate_text(model, tokenizer, inputs):
  inputs = tokenizer(inputs, return_tensors="pt").to(model.device)

  model.config.pad_token_id = 0

  with torch.no_grad():
    tokens = model.generate(
      **inputs,
      max_new_tokens=48,
      temperature=0.2,
      do_sample=True,
    )
  return tokenizer.decode(tokens[0], skip_special_tokens=True, return_token_type_ids=False)


def main():
  # Start the timer
  if debug:
    # Record the start time
    start_time = time.time()

  tokenizer = AutoTokenizer.from_pretrained(
    "stabilityai/stablecode-instruct-alpha-3b",
    use_auth_token=True
  )

  model = AutoModelForCausalLM.from_pretrained(
    "stabilityai/stablecode-instruct-alpha-3b",
    trust_remote_code=True,
    torch_dtype="auto",
    use_auth_token=True
  ).to("cuda:0")

  inputs = read_file("instruction.txt")

  generated_text = generate_text(model, tokenizer, inputs)
  print(generated_text)

  if debug:
    # Record the end time
    end_time = time.time()

    # Calculate and print the execution time
    execution_time = end_time - start_time

    print("")
    print(f"Total Execution Time: {execution_time:.2f} seconds")


if __name__ == "__main__":
  main()
