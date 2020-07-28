import turtle
t= turtle.Pen()
turtle.bgcolor("black")
colors = ["orange", "purple", "blue", "green", "red"]
for x in range(100):
	t.pencolor(colors[x%5])
	t.backward(x)
	t.left(70)
