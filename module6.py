class Point:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __str__(self):
		return f'({self.x}, {self.y})'

class Rectangle:
	def __init__(self,posn,w,h):
		self.corner = posn
		self.width = w
		self.height = h
	def __str__(self):
		return f'{self.corner}, {self.width}, {self.height}'

def create_rectangle(x,y,width,height):
	return Rectangle(Point(x,y),width,height)

def str_rectangle(rect):
	return str(rect)

def shift_rectangle(rect,dx,dy):
	ax, ay = rect.corner.x, rect.corner.y
	rect.corner.x = ax + dx
	rect.corner.y = ay + dy

def offset_rectangle(rect, dx, dy):
	ax, ay = rect.corner.x, rect.corner.y
	return create_rectangle(ax +dx, ay+dy, rect.width, rect.height)



r1 = create_rectangle(10,20,30,40)
print(str_rectangle(r1))
shift_rectangle(r1,-10,-20)
print(str_rectangle(r1))

r2 = offset_rectangle(r1,100,100)
print(str_rectangle(r1))
print(str_rectangle(r2))

