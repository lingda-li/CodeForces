import random

def generate_input_for_codeforces_15a(random_seed=0):
  """Generates a random input for the CodeForces 15A problem.

  Args:
    random_seed: The random seed.

  Returns:
    A string containing the random input.
  """

  # Set the random seed.
  random.seed(random_seed)

  n = random.randint(2, 1000)
  t = random.randint(2, 10)

  houses = []
  for i in range(n):
    a = random.randint(1, 1000)
    b = random.randint(1, 10)
    houses.append([a, b])

  # Generate the input string.
  input_string = f"{n} {t}\n"
  for h in houses:
    input_string += f"{h[0]} {h[1]}\n"

  return input_string

if __name__ == "__main__":
  # Generate the input string.
  input_string = generate_input_for_codeforces_15a()

  print(input_string)

