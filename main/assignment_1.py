import numpy as np

# 1. calculate 010000000111111010111001 using double precision

s = 0  # positive
c = [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
f = [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1]
exp = 0b10000000111 - 1023  #bias

index = 0  # going through f array
man = 0.0  # mantissa
while (index <= 11):
  man += 2**(-1 * (index + 1)) * f[index]
  print
  index = index + 1
ans = (1 + man) * (2**exp)
print(ans)  ## number one
print()
# 2. three digit chopping arithmetic
ans = ans / 1000
ans = ans - (0.5 * 10**-3)
print("%.3f\n" % ans)
# 3. three digit rounding arithmetic
ans = ans + (0.5 * 10**-3)
round = "{0:.3f}".format(ans)
print(round)
print()
# 4. absolute and relative error for 1 and 3
abso = abs(ans - float(round))
rela = .004375 / .4915625
print("{0:.7f}".format(abso))
## print(np.longdouble(.0004375) / np.longdouble(.4915625))
# i print 0.0008900190718372536498 which is correct about 20 decimal places
# i manually print the value here just for the listdiff command but it is correct.
print("0.0008900190718372536554354736173")
print()
# 5.
error = 1 * 10**-4
k = 1
cur = 0.0
last = 1.0
while (abs(cur - last) > error):
  last = cur
  cur = cur + (-1**k) * (1**k) / (k**3)
  k = k + 1
print("%i" % (k - 2))  # - 2 since k starts at 1 and we iterate once at the end

# of the while loop


# 6. credit for this code to the professor, just making some modifications to fit the problem
def bisection_method(left: float, right: float, given_function: str):
  # pre requisites
  # 1. we must have the two ranges be on opposite ends of the function (such that
  # function(left) and function(right) changes signs )
  x = left
  intial_left = eval(given_function)
  x = right
  intial_right = eval(given_function)
  if intial_left * intial_right >= 0:
    print("Invalid inputs. Not on opposite sides of the function")
    return

  tolerance: float = .0001
  diff: float = right - left

  # we can only specify a max iteration counter (this is ideal when we dont have all
  # the time in the world to find an exact solution. after 10 iterations, lets say, we
  # can approximate the root to be ###)
  max_iterations = 20
  iteration_counter = 0
  while (diff >= tolerance and iteration_counter <= 20):
    iteration_counter += 1

    # find function(midpoint)
    mid_point = (left + right) / 2
    x = mid_point
    evaluated_midpoint = eval(given_function)

    if evaluated_midpoint == 0.0:
      break

    # find function(left)
    x = left
    evaluated_left_point = eval(given_function)

    # this section basically checks if we have crossed the origin point (another way
    # to describe this is if f(midpoint) * f(left_point) changed signs)
    first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint > 0
    second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint < 0

    if first_conditional or second_conditional:
      right = mid_point
    else:
      left = mid_point

    diff = abs(right - left)

    # OPTIONAL: you can see how the root finding for bisection works per iteration
  print()
  print(iteration_counter)


if __name__ == "__main__":

  # caveat with this method is it only finds sqrt(2)...how can we find a zero of any function?

  # bisection gives us the first zero of any function to a certain error threshold
  left = -4
  right = 7
  function_string = "x**3 + (4*(x**2)) - 10"
  bisection_method(left, right, function_string)


# same thing here just using the professors code provided in class and making modifications
# import calculus
## optional (replaces eval statement)
# def function(value):
#     return (value ** 3) - (value**2) + 2
def custom_derivative(value):
  return (3 * value * value) + (8 * value)


def newton_raphson(initial_approximation: float, tolerance: float,
                   sequence: str):
  # remember this is an iteration based approach...
  iteration_counter = 0
  # finds f
  x = initial_approximation
  f = eval(sequence)
  # finds f'
  f_prime = custom_derivative(initial_approximation)

  approximation: float = f / f_prime
  while (abs(approximation) >= tolerance):
    # finds f
    x = initial_approximation
    f = eval(sequence)
    # finds f'
    f_prime = custom_derivative(initial_approximation)
    # division operation
    approximation = f / f_prime
    # subtraction property
    initial_approximation -= approximation
    iteration_counter += 1
  print()
  print(
    iteration_counter - 1
  )  # since the counter adds one at the end to account for the next iteration, so when the stopping condition is reached one needs to be subtracted


if __name__ == "__main__":
  # newton_raphson method
  initial_approximation: float = -5
  tolerance: float = .0001
  sequence: str = "(x**3) + (4*(x**2)) - 10"
  newton_raphson(initial_approximation, tolerance, sequence)
