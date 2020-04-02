def fizzbuzz(input):
  if input == 0:
    return 0
  elif input % 15 == 0:
    return 'fizzbuzz'
  elif input % 3 == 0:
    return 'fizz'
  elif input % 5 == 0:
    return 'buzz'
  else:
    return input
