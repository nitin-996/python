def find_palindromes(start, end):
  palindromes = []
  for number in range(start, end + 1):
    num_str = str(number)
    print(num_str)
    if num_str == num_str[::-1]:
      print(num_str[::-1])
      palindromes.append(number)
  return palindromes

# Find palindromes between 100 and 150
print(find_palindromes(100, 150))