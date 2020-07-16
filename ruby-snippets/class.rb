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


