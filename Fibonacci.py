def is_fibonacci(num):
  a,b = 0,1

  if num == 0 or num == 1:
    return True

  while b < num:
    a,b = b, a + b

  return b == num

number = int(input("Digite um número: "))

if is_fibonacci(number):
  print(f"O número {number} pertence à sequência de Fibonacci.")
else:
  print(f"O número {number} não pertence à sequência de Fibonacci.")