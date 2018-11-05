# Find the largest palindrome made from the product of two 3-digit numbers which is less than N .

# #### Input Format

# First line contains <b>T</b> that denotes the number of test cases. This is followed by <b>T</b>  lines, each containing an integer,<b>N</b> .


# #### Output Format

# Print the required answer for each test case.

# #### CONSTRAINTS
# 1≤ T ≤ 100

# 101101≤ N ≤ 1000000

# #### Sample Input
# ```
# 2
# 101110
# 800000
# ```

# #### Sample Output
# ```
# 101101
# 793397
# ```

def main
  # read the test cases
  puts "Enter number of Test Cases (1-100)"
  test_cases = gets.to_i
  return "Number of test cases exceeds the range" if test_cases < 1 || test_cases > 100

  # read the numbers
  numbers = []
  puts "Enter numbers in the range of 101101 - 999999 "
  test_cases.times do |n|
    puts "Enter number #{n} : "
    number = gets.to_i
    return "Number out of range" if number < 101101 || number > 999999
    numbers << number
  end
  puts "********* OUTPUT ***********"
  palindromes = []
  numbers.each do |num|
    palindromes << largest_palindrome(num)
  end
  puts palindromes
end

def largest_palindrome(number)
  (101_101..number).to_a.reverse.each do |num|
    next unless palindrome?(num)
    return num if three_digit_product?(num)
  end
  101_101
end

def three_digit_product?(number)
  max_num = 999
  first_num = max_num
  second_num = 101 # 999 * 101 gives the first 6 digit number
  while first_num > second_num
    product = first_num * second_num
    return true if product == number
    if product > number
      first_num -= 1
    else
      second_num += 1
    end
  end
  false
end

def palindrome?(number)
  digits = number.digits
  digits == digits.reverse
end


# running the program
main
