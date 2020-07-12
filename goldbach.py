def check_goldbach(n):
  list_for_primes = prime_gen(n)
  factors = []
  for x in list_for_primes:
    target = n - x
    if(target in list_for_primes):
      if(len(factors) < 2):
        factors.append(x)
        factors.append(target)

  return factors
  print(list_for_primes)

check_goldbach(84)
