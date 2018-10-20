#!/usr/bin/env ruby
# The Bastards Book of Ruby
# http://ruby.bastardsbook.com/chapters/regexes/

str="My cat gets catatonic when I attempt to concatenate his food with Muscat grapes"
puts str.gsub(/\bcat\b/, 'dog')
