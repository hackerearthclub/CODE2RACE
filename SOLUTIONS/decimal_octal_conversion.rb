# octal to decimal and decimal to octal conversion

def octal_decimal(int)
  num = int.to_i.digits
  if (num & [8, 9]).present?
    puts "Can't be a octal number please check"
    return
  end
  decimal_number = 0
  num.each_with_index do |val, index|
    decimal_number += (val * (8 ** index))
  end
  puts "Octal #{int} is Decimal #{decimal_number}"
end

def decimal_octal(int)
  quotient = int.to_i
  octal_num = ''
  while quotient != 0
    remainder = quotient % 8
    quotient /= 8
    octal_num = remainder.to_s + octal_num
  end
  puts "Decimal #{int} is Octal #{octal_num}"
end

# To convert decimal to octal
decimal_octal 1792

# To convert octal to decimal
octal_decimal 3400
