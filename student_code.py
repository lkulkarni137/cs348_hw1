from expand import expand

def a_star_search (dis_map, time_map, start, end):
	visited = {start: [start]}
	prior_queue = [(0, (start, [start]))]

	while prior_queue:
		_, (curr, path) = prior_queue.pop(0)

		if curr == end:
			return path
		
		expanded_nodes = expand(curr)
		for neighbor in expanded_nodes:
			total_time = visited[curr][0] + dis_map[curr][neighbor]

			if neighbor not in visited or total_time < visited[neighbor][0]:
				visited[neighbor] = [total_time, path + [neighbor]]
				prior_queue.append((total_time, (neighbor, path + [neighbor])))
				prior_queue.sort(key=lambda x: x[0])

		return []

def depth_first_search(time_map, start, end):
	visited = {start: [start]}
	stack = [(start, [start])]

	while stack:
		curr, path = stack.pop()
		
		if curr == end:
			return path
		
		for neighbor, travel_time in reversed(time_map[curr].items()):
			total_time = visited[curr][0] + travel_time

			if neighbor not in visited or total_time < visited[neighbor][0]:
				visited[neighbor] = [total_time, path + [neighbor]]
				stack.append((neighbor, path + [neighbor]))

		return []

def breadth_first_search(time_map, start, end):
	visited = {start: [start]}
	queue = [(start, [start])]

	while queue:
		curr, path = queue.pop(0)

		if curr == end:
			return path
		
		for neighbor, travel_time in time_map[curr].items():
			total_time = visited[curr][0] + travel_time

			if neighbor not in visited or total_time < visited[neighbor][0]:
				visited[neighbor] = [total_time, path + [neighbor]]
				queue.append((neighbor, path + [neighbor]))

		return []


		