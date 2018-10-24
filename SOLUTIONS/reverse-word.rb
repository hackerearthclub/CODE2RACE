def reverse_sentence
puts "Please enter a sentence"
user_input = gets.chomp
puts "Reversed:" + user_input.split(/\b/).reverse.join
end
