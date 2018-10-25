# The number,197 , is called a circular prime because
# all rotations of the digits: 197,971 and 719  are themselves prime.
# There are thirteen such primes below 100: 2,3,5,7,11,13,17,31,37,71,73,79 and 97.
# Sum of which is 446.
# Find the sum of circular primes that are below N?
# <b> Rotations can exceed N </b>
# #### Input Format
# Input contains an integer <b>N</b>.
# #### Output Format
# Print the required answer.
# #### CONSTRAINTS
# 10≤ N ≤ 10^6
# #### Sample Input
# ```
# 100
# ```
# #### Sample Output
# ```
# 446
# ```

require 'prime'

def find_circular_primes
  puts 'Enter an integer number between 10 and 1000000'
  input_string = gets
  number = input_string.chomp.to_i
  if number < 10 || number > 10**6
    puts 'The number exceeds the range. Exiting!'
  else
    list_circular_primes(number)
  end
end

def list_circular_primes(max_number)
  circular_primes = []
  (1...max_number).each do |number|
    next unless prime?(number)
    circular_primes << number if circular_prime?(number)
  end
  puts "Circular primes below #{max_number}"
  puts circular_primes.join(', ')
  puts "Count: #{circular_primes.count}"
  puts "Sum: #{circular_primes.sum}"
end

def prime?(number)
  Prime.prime?(number)
end

def circular_prime?(number)
  circular_numbers = unique_circular_numbers(number)
  circular_numbers.all? { |num| prime?(num) }
end

def unique_circular_numbers(number)
  splitted_numbers = number.digits
  splitted_numbers
    .permutation(splitted_numbers.size)
    .uniq
    .map(&:join)
    .map(&:to_i)
end

# running the program
find_circular_primes
