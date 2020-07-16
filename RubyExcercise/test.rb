puts "Welcome to Ruby!"
print "Welcome to Ruby!" #I am a comment as well
print "\n"

=begin
  block of comment
=end

#the following are variable
firstName = "Tashsin"
lastName = "Kobra"

p firstName + lastName

lastName = lastName.reverse.upcase
firstName = firstName.upcase

p firstName + lastName

testAr = [1, 2, 3]

aHash = {
  "Key1" => "Alarm",
  "Key2" => "NoAlarm"
}

puts aHash

i = 0
while i < 5
  puts i
  i = i + 1
end


a = nil
a = "something"
a.b = 7

if a
  puts a
else
  puts "Nah"
end


