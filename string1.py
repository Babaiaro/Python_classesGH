#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic string exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in string2.py.


# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
def donuts(count):
  # +++your code here+++
  if count < 10 :
    return f'Number of donuts: {count}'
  else:
    return 'Number of donuts: many'


# B. both_en  ds
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
  # +++your code here+++
  if len(s) < 2:
    return ''
  else:
    return s[2:]+s[:-2]



# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
  # +++your code here+++
  first_char = s[0]
  rest = s[1:].replace(first_char, "*")
  return


# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
  # +++your code here+++
mix_char_a = b[:2] + a[2:]
  mix_char_b = a[:2] + b[2:]
  return mix_char_a + '' + mix_char_b


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print('donuts')
  # Each line calls donuts, compares its result to the expected for that call.
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')

  print()
  print('both_ends')
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyyz')


  print()
  print('fix_start')
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')

  print()
  print('mix_up')
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()

  # ==============================================================
  # Google-Style String Practice 2
  # Each task has:
  #   - description in comments
  #   - your code placeholder
  #   - expected outputs for testing
  # ==============================================================

  # --------------------------------------------------------------
  # A. first_last_two
  # Task:
  #   Return a string made of the first 2 and last 2 chars.
  #   If the string length < 2, return ''.
  # Example:
  #   first_last_two('spring') → 'spng'
  #   first_last_two('a') → ''
  # Expected outputs in tests below.
  def first_last_two(s):
    # +++ your code here +++
    if len(s) <2:
      return ""
    else:
      return s[2:]+s[:-2]
 


  # --------------------------------------------------------------
  # B. count_hi
  # Task:
  #   Count how many times 'hi' appears in the string (non-overlapping).
  # Example:
  #   count_hi('hihi') → 2
  #   count_hi('hello hi') → 1
  def count_hi(s):
    # +++ your code here +++
    return 0


  # --------------------------------------------------------------
  # C. ends_same
  # Task:
  #   Return True if the string starts and ends with the same 2 characters.
  # Example:
  #   ends_same('edited') → True
  #   ends_same('coding') → False
  def ends_same(s):
    # +++ your code here +++
    return False


  # --------------------------------------------------------------
  # D. remove_middle
  # Task:
  #   Remove all occurrences of a given character (c) from the middle of the string,
  #   keeping the first and last occurrence (if they exist).
  # Example:
  #   remove_middle('abracadabra','a') → 'abracada bra'.replace(' ', '')
  #   remove_middle('xxxyxx','x') → 'x y x'.replace(' ', '')
  def remove_middle(s, c):
    # +++ your code here +++
    return s


  # --------------------------------------------------------------
  # E. front_back_swap
  # Task:
  #   Given strings a and b, swap the first 2 characters of each,
  #   return '<new_a> <new_b>'.
  # Example:
  #   front_back_swap('mix','pod') → 'pox mid'
  #   front_back_swap('dog','dinner') → 'dig donner'
  def front_back_swap(a, b):
    # +++ your code here +++
    return ''


  # --------------------------------------------------------------
  # F. x_balance
  # Task:
  #   Move all 'x' characters to the end of the string,
  #   keeping other characters in their original order.
  # Example:
  #   x_balance('xxabxc') → 'ab c xxx'.replace(' ','')
  #   x_balance('xyz') → 'yzx'
  def x_balance(s):
    # +++ your code here +++
    return ''


  # --------------------------------------------------------------
  # G. repeat_sep
  # Task:
  #   Return word repeated n times, separated by sep.
  # Example:
  #   repeat_sep('Hi','-',3) → 'Hi-Hi-Hi'
  #   repeat_sep('A','*',1) → 'A'
  def repeat_sep(word, sep, n):
    # +++ your code here +++
    return ''


  # --------------------------------------------------------------
  # H. middle_out
  # Task:
  #   Remove the middle character(s) from a string.
  #   - Remove 1 char if length is odd
  #   - Remove 2 chars if length is even
  # Example:
  #   middle_out('abc') → 'ac'
  #   middle_out('code') → 'ce'
  def middle_out(s):
    # +++ your code here +++
    return ''


  # --------------------------------------------------------------
  # I. is_palindrome_clean
  # Task:
  #   Return True if the string is a palindrome,
  #   ignoring spaces and case.
  # Example:
  #   is_palindrome_clean('Race car') → True
  #   is_palindrome_clean('hello') → False
  def is_palindrome_clean(s):
    # +++ your code here +++
    return False


  # --------------------------------------------------------------
  # J. compress_basic
  # Task:
  #   Return a run-length encoding string:
  #   'aaabbc' → 'a3b2c1'
  #   'abcd' → 'a1b1c1d1'
  def compress_basic(s):
    # +++ your code here +++
    return ''


  # --------------------------------------------------------------
  # Testing helper
  def test(got, expected):
    if got == expected:
      prefix = ' OK '
    else:
      prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


  # --------------------------------------------------------------
  # Test runner
  def main():
    print('first_last_two')
    test(first_last_two('spring'), 'spng')
    test(first_last_two('Hello'), 'Helo')
    test(first_last_two('a'), '')
    test(first_last_two('xy'), 'xyxy')

    print('\ncount_hi')
    test(count_hi('hihi'), 2)
    test(count_hi('hi there, hiii'), 2)
    test(count_hi('abc'), 0)

    print('\nends_same')
    test(ends_same('edited'), True)
    test(ends_same('coding'), False)
    test(ends_same('aa'), True)

    print('\nremove_middle')
    test(remove_middle('abracadabra', 'a'), 'abracadabra'.replace('a', '', 2))  # for reference
    test(remove_middle('xxxyxx', 'x'), 'x y x'.replace(' ', ''))
    test(remove_middle('hello', 'z'), 'hello')

    print('\nfront_back_swap')
    test(front_back_swap('mix', 'pod'), 'pox mid')
    test(front_back_swap('dog', 'dinner'), 'dig donner')
    test(front_back_swap('gnash', 'sport'), 'spash gnort')

    print('\nx_balance')
    test(x_balance('xxabxc'), 'ab c xxx'.replace(' ', ''))
    test(x_balance('xyz'), 'yzx')
    test(x_balance('abc'), 'abc')

    print('\nrepeat_sep')
    test(repeat_sep('Hi', '-', 3), 'Hi-Hi-Hi')
    test(repeat_sep('A', '*', 1), 'A')
    test(repeat_sep('yo', '_', 4), 'yo_yo_yo_yo')

    print('\nmiddle_out')
    test(middle_out('abc'), 'ac')
    test(middle_out('code'), 'ce')
    test(middle_out('a'), '')

    print('\nis_palindrome_clean')
    test(is_palindrome_clean('Never odd or even'), True)
    test(is_palindrome_clean('Race car'), True)
    test(is_palindrome_clean('hello'), False)

    print('\ncompress_basic')
    test(compress_basic('aaabbc'), 'a3b2c1')
    test(compress_basic('abcd'), 'a1b1c1d1')
    test(compress_basic(''), '')


  if __name__ == '__main__':
    main()


