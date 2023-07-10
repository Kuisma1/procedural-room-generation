from getpointsbetween import get_points_between

def centers_to_path(rooms):
	point_distance = lambda p1, p2: ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
	centers = [room.get_center() for room in rooms]
	new_centers = [centers[0]]
	centers.pop(0)

	while len(centers) > 0:
		centers.sort(key=lambda p: point_distance(p, new_centers[-1]))
		new_centers.append(centers[0])
		centers.pop(0)

	path_points = []

	for center1, center2 in zip(new_centers[:-1], new_centers[1:]):
		path_points += get_points_between(center1, center2)

	path_points = list(set(path_points))

	return path_points