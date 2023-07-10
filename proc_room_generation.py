from space import Space, Room
from centerstopath import centers_to_path

def generate_dungeon(width, height, steps, space_min_size, space_min_area, room_min_size, room_max_size):
	
	spaces = [Space(0, 0, width-1, height-1)]

	for _ in range(steps):
		new_spaces = []
		for space in spaces:
			new_spaces += space.split(space_min_size, space_min_area)
		if len(new_spaces) == len(spaces):
			break
		else:
			spaces = new_spaces

	rooms = [space.get_room(room_min_size, room_max_size) for space in spaces]

	start_point = rooms[0].get_center()
	end_point = rooms[-1].get_center()

	path = centers_to_path(rooms)

	grid = [[0 for x in range(width)] for y in range(height)]

	for room in rooms:
		room_left = room.get_sides()[0]
		room_top = room.get_sides()[1]
		room_right = room.get_sides()[2]
		room_bottom = room.get_sides()[3]
		for i in range(height):
			for j in range(width):
				if room_top <= i <= room_bottom and room_left <= j <= room_right:
					grid[i][j] = 1
	
	for point in path:
		px = point[0]
		py = point[1]
		grid[py][px] = 1
		
	grid[start_point[1]][start_point[0]] = 2
	grid[end_point[1]][end_point[0]] = 3

	for row in grid:
		print("".join([["#",".","S","E"][x] for x in row]))

	

#                width, height, steps, space_min_size, space_min_area, room_min_size, room_max_size

generate_dungeon(100, 100, 100, 15, 100, 10, 15)