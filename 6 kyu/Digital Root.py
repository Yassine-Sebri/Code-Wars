"""In this kata, you must create a digital root function.
A digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n. If that value has more than one digit,
continue reducing in this way until a single-digit number is produced.
This is only applicable to the natural numbers."""

def digital_root(n):
  if n < 10:
    return n
  else:
    return digital_root(sum([int(digit) for digit in str(n)]))
