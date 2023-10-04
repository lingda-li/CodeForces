import sys
import random

def generate_input_for_codeforces_16b(n, m):
  """Generates a random input for the CodeForces 16B problem.

  Args:
    n: The number of matchboxes that the burglar's rucksack can hold.
    m: The number of containers in the warehouse.

  Returns:
    A string containing the random input.
  """

  # Generate the number of matchboxes and matches per matchbox for each container.
  containers = []
  for i in range(m):
    a = random.randint(1, 10)
    b = random.randint(1, 100)
    containers.append([a, b])

  # Generate the input string.
  input_string = f"{n} {m}\n"
  for container in containers:
    input_string += f"{container[0]} {container[1]}\n"

  return input_string

if __name__ == "__main__":
  # Set the random seed.
  random.seed(sys.argv[1])

  n = 30000
  m = 30000

  # Generate the input string.
  input_string = generate_input_for_codeforces_16b(n, m)

  print(input_string)

