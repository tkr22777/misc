#Function
def factorial(number)
  if number > 1
    return number * factorial(number - 1)
  else
    return 1
  end
end

#Array
numbers = Array.new
numbers[0] = "Hundred"
numbers[1] = "Thousand"
numbers[2] = "Million"
numbers[3] = "Billion"

for aNumber in numbers do
  puts aNumber
end

#Range For loop
for i in 0..4
  puts "Factorial of " + i.to_s + " is " +  factorial(i).to_s
end

#While loop
i = 0
while i < 5 do
  puts "i: " + i.to_s
  i = i + 1
end

#Class loop
class CoOrdinate

  def initialize(x, y)
    @x = x
    @y = y
  end

  def toString
    return "X:" + @x.to_s + " Y:" + @y.to_s
  end
end

origin = CoOrdinate.new(0, 0)
tenUp = CoOrdinate.new(0, 20)

puts origin.toString
puts tenUp.toString


