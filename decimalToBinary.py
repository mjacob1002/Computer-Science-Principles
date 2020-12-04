def decimalToBinary(x : int):
  z = []
  # go through 64, 32, 16, 8, 4, 2, 1 and test
  for i in range(6,-1, -1):
    if x >= 2 ** i:
      z.append(1)
    else
      z.append(0)
    x -= 2 ** i
  return z
