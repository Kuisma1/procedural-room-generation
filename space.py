import random
from centerstopath import centers_to_path

class Space:
	def __init__(self, left, top, right, bottom):
		self.left = left
		self.top = top
		self.right = right
		self.bottom = bottom
	def get_center(self):
		return ((self.left+self.right)//2,(self.top+self.bottom)//2)
	def split(self, min_size, min_area):
		space_width = self.right-self.left
		space_height = self.bottom-self.top
		space_area = space_width*space_height

		if space_area <= min_area:
			return [self]

		if random.choice(["h", "v"]) == "h":
			if space_width <= 2*min_size:
				return [self]
			else:
				x = random.choice(range(self.left+min_size, self.right-min_size))
				new_left1 = self.left
				new_top1 = self.top
				new_right1 = x
				new_bottom1 = self.bottom
				new_left2 = x+1
				new_top2 = self.top
				new_right2 = self.right
				new_bottom2 = self.bottom
		else:
			if space_height <= 2*min_size:
				return [self]
			else:
				x = random.choice(range(self.top+min_size, self.bottom-min_size))
				new_left1 = self.left
				new_top1 = self.top
				new_right1 = self.right
				new_bottom1 = x
				new_left2 = self.left
				new_top2 = x+1
				new_right2 = self.right
				new_bottom2 = self.bottom
		return [Space(new_left1, new_top1, new_right1, new_bottom1), Space(new_left2, new_top2, new_right2, new_bottom2)]
	def get_sides(self):
		return (self.left, self.top, self.right, self.bottom)
	def get_room(self, min_size, max_size):
		room_width = random.choice(range(min_size-1, max_size))
		room_height = random.choice(range(min_size-1, max_size))
		room_left = random.choice(range(self.left, self.right-room_width))
		room_top = random.choice(range(self.top, self.bottom-room_width))
		room_right = room_left+room_width
		room_bottom = room_top+room_height
		return Room(room_left, room_top, room_right, room_bottom)

class Room(Space):
	pass