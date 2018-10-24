# program to reverse words in ruby

def reverse_word(sentence)
  puts sentence.split(" ").reverse.join(" ")
end

print "Input text: "; input = gets.strip; reverse_word(input)
