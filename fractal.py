import turtle as tl

def draw_koch_line(size, n):
  if n == 0: 
    tl.fd(size)
    return

  s = size/3        
  draw_koch_line(s, n-1)
  tl.left(60)
  draw_koch_line(s, n-1)
  tl.right(120)
  draw_koch_line(s, n-1)
  tl.left(60)
  draw_koch_line(s, n-1)
                    


size = 200
n = 5

tl.delay(1)  # уменьшение задержки для скорости
tl.penup()
tl.color('green')
tl.goto(0, -size * 2)
tl.setheading(90)
tl.pendown()

draw_koch_line(size, n)
tl.done()