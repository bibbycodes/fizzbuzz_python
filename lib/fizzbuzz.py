def fizzbuzz(input):
  if input == 0:
    return input
  elif input % 3 == 0:
    return 'fizz'
  elif input == 5:
    return 'buzz'
  else:
    return input
