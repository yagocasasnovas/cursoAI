import math

"""commmon functions"""


def file_print(ss,t,f):
	
	string = ''
	for row in range(9):
		for col in range(9):
			string = string + str(ss[row][col])
	
	"print string + ' ' + t"
	ww = string + ' ' + t + '\n'
	f.write(ww)


def pretty_print(sak):
	
	print '-----------------------------'
	for ll in range(9):
		
		print str(sak[ll])
	print '-----------------------------'


def pretty_print_domain(dom):
	
	ii = 0
	for ll in dom:

		print str(ii) + '   ' + str(ll)
		ii = ii + 1


#converts list of strings to list of arrays
def string_to_list(item):
	
	list = []
	
	for c in item:
		
		list.append(int(c))

		
	return list

#converts list of 81 values to list of 9 lists of 9 values.
def convert_to_r_c(item):
	
	sud_lines = []
	
	
	
	for col in range(9):
		row_a = []
		for row in range(9):
			
			row_a.append(item[row + col*9])
		sud_lines.append(row_a)
		
	return sud_lines


def get_lines(row,col):
	
	ii = col + row*9
	out = []
	line = math.floor((ii)/9)
	
	for j in range(9):
		s = int(j + line*9)
		out.append(s)
	return out
	

def get_columns(row,col):
	
	
	out = []
	
	
	for j in range(9):
		s = int(j*9 + col)
		out.append(s)
	
	return out


"AC3 Functions"


def create_initial_queue():
	
	q = set()
	
	for row in range(9):
		for col in range(9):
			"lines"
			for col1 in range(9):
				if col1 != col:
					q.add(((row,col),(row,col1)))
			
			"columns"
			for row1 in range(9):
				if row1 != row:
					q.add(((row,col),(row1,col)))
					
			"cubes"
			pos = row*9 + col
			for row1 in range(9):
				for col1 in range(9):
					pos1 = row1*9+col1
					if cubes_id[pos] == cubes_id[pos1] and pos != pos1:
						q.add(((row,col),(row1,col1)))
		
	return q


def revise_arc(arc_l,sud_l):
	
	global domains_AC3
	
	
	row1 = arc[0][0]
	col1 = arc[0][1]
	pos1 = row1*9 + col1
	
	row2 = arc[1][0]
	col2 = arc[1][1]
	pos2 = row2*9 + col2
	
	if sud_l[row1][col1] == 0:
		if sud_l[row2][col2] == 0 and len(domains_AC3[pos2]) == 1:
			for value in domains_AC3[pos1]:
				if value == domains_AC3[pos2][0]:
					domains_AC3[pos1].remove(value)
					return True
		
		if sud_l[row2][col2] != 0:
			for value in domains_AC3[pos1]:
				if value == sud_l[row2][col2]:
					domains_AC3[pos1].remove(value)
					return True

	return False
	
	

def add_neighbours(arc_l):
	
	global arc_queue
	row1 = arc_l[0][0]
	col1 = arc_l[0][1]
	pos1 = row1*9 + col1
	
	row2 = arc_l[1][0]
	col2 = arc_l[1][1]
	pos2 = row2*9 + col2

	"lines"
	for colx in range(9):
		if colx != col1 and colx != col2:
			arc_queue.add(((row1,colx),(row1,col1)))
			
	"columns"
	for rowx in range(9):
		if rowx != row1 and rowx != row2:
			arc_queue.add(((rowx,col1),(row1,col1)))
					
	"cubes"
	
	for rowx in range(9):
		for colx in range(9):
			posx = rowx*9+colx
			if cubes_id[posx] == cubes_id[pos1] and posx != pos2 and posx != pos1:
				arc_queue.add(((rowx,colx),(row1,col1)))


"backtrack functions"


#called to get the empty slots of the sudoku (to check if we have finished or not)
def get_empty_slots ( sud_l ):
	empty_slots = []

	for row in range(len( sud_l )):
		for col in range(len( sud_l[1] )):
			if sud_l[row][col] == 0:
				empty_slots.append( [row,col] ) 
	return empty_slots


# returns domains from 1 to 81 (list of possible values for each slot)

def get_domains( sud_l ):
	domains = []

	
	for i in range(81):
		domains.append([1,2,3,4,5,6,7,8,9])
	for row in range(9):
		for col in range(9):
			
			if sud_l[row][col] != 0:

				value = sud_l[row][col]

				domains = delete_values_neighbours( row, col, value, domains)

	return domains



#takes out values from domains from neighbours given a value

def delete_values_neighbours( row, col, value, domains ):

	global cubes_pos
	position = row*9 + col
		
	#domain of given slot set to empty
	domains[position] = []
	
	"lines"
	line = get_lines(row,col)
	for slot in line:
		if slot != position and value in domains[slot]:
			domains[slot].remove(value)
			
	
	"columns"
	column = get_columns(row,col)
	for slot in column:
		if slot != position and value in domains[slot]:
			domains[slot].remove(value)
	
	"Cubes"
	cube_array = cubes_pos[position]
	for slot in cube_array:
		if slot != position and value in domains[slot]:
			domains[slot].remove(value)
	
	
	return domains


#select unasgined with minimum remaining value
def select_unassigned_mrv(sud_l,domains_l):
	
	
	output = 100
	
	
	initial_length = 10
	for row in range(9):
		for col in range(9):
			pos = row*9 + col

			if sud_l[row][col] == 0:
				length1 = len(domains_l[pos])
				if length1 < initial_length:
					initial_length = length1
					output = (row,col)

	return output


def forward_check( domains_l, val, row, col ):
	
	
	pos = row*9+col
	
	"print str(pos) + ' ' + str(row) + ' ' + str(col)"
	"lines"
	lines = get_lines(row,col)
	for lin in lines:
		if lin != pos:
			if val in domains_l[lin] and len(domains_l[lin]) == 1:

				return False
	
	
	"columns"
	columns = get_columns(row,col)
	for col in columns:
		if col != pos:
			if val in domains_l[col] and len(domains_l[col]) == 1:
				return False


	"cubes"
	cubel = cubes_pos[pos]
	for cub in cubel:
		if cub != pos:
			if val in domains_l[cub] and len(domains_l[cub]) == 1:
				return False

	return True





def backtrack_forward(sud_l):
	
	
	empty = get_empty_slots ( sud_l )
	
	if len(empty) == 0:

		return True
	
	domains_l = get_domains(sud_l)
	"pretty_print_domain(domains_l)"
	row = select_unassigned_mrv(sud_l,domains_l)[0]
	col = select_unassigned_mrv(sud_l,domains_l)[1]
	
	for value in domains_l[row*9 + col]:
		if forward_check(domains_l,value,row,col):
			
			sud_l[row][col] = value
			if backtrack_forward(sud_l):
				return True
			else:
				sud_l[row][col] = 0
	return False



"inicio main -----------------------------"

cubes_pos = [[0,1,2,9,10,11,18,19,20],[0,1,2,9,10,11,18,19,20],[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[3,4,5,12,13,14,21,22,23],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],[6,7,8,15,16,17,24,25,26],[6,7,8,15,16,17,24,25,26],[0,1,2,9,10,11,18,19,20],[0,1,2,9,10,11,18,19,20],[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[3,4,5,12,13,14,21,22,23],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],[6,7,8,15,16,17,24,25,26],[6,7,8,15,16,17,24,25,26],[0,1,2,9,10,11,18,19,20],[0,1,2,9,10,11,18,19,20],[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[3,4,5,12,13,14,21,22,23],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],[6,7,8,15,16,17,24,25,26],[6,7,8,15,16,17,24,25,26],[27,28,29,36,37,38,45,46,47],[27,28,29,36,37,38,45,46,47],[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[30,31,32,39,40,41,48,49,50],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],[33,34,35,42,43,44,51,52,53],[33,34,35,42,43,44,51,52,53],[27,28,29,36,37,38,45,46,47],[27,28,29,36,37,38,45,46,47],[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[30,31,32,39,40,41,48,49,50],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],[33,34,35,42,43,44,51,52,53],[33,34,35,42,43,44,51,52,53],[27,28,29,36,37,38,45,46,47],[27,28,29,36,37,38,45,46,47],[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[30,31,32,39,40,41,48,49,50],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],[33,34,35,42,43,44,51,52,53],[33,34,35,42,43,44,51,52,53],[54,55,56,63,64,65,72,73,74],[54,55,56,63,64,65,72,73,74],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[57,58,59,66,67,68,75,76,77],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80],[60,61,62,69,70,71,78,79,80],[60,61,62,69,70,71,78,79,80],[54,55,56,63,64,65,72,73,74],[54,55,56,63,64,65,72,73,74],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[57,58,59,66,67,68,75,76,77],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80],[60,61,62,69,70,71,78,79,80],[60,61,62,69,70,71,78,79,80],[54,55,56,63,64,65,72,73,74],[54,55,56,63,64,65,72,73,74],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[57,58,59,66,67,68,75,76,77],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80],[60,61,62,69,70,71,78,79,80],[60,61,62,69,70,71,78,79,80]]
cubes_id = [1,1,1,2,2,2,3,3,3,1,1,1,2,2,2,3,3,3,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,4,4,4,5,5,5,6,6,6,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,7,7,7,8,8,8,9,9,9,7,7,7,8,8,8,9,9,9]

with open('sudokus_start.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

list_of_sudoks = []

file = open('output.txt','a')

for c in content:
	

	sudok = string_to_list(c)
	
	sudok = convert_to_r_c(sudok)
	
	
	
	list_of_sudoks.append(sudok)


i = 0
for sudok in list_of_sudoks:
	

	
	sudok_AC3 = sudok
	"pretty_print(sudok_AC3)"

	
	arc_queue = create_initial_queue()

	domains_AC3 = get_domains(sudok_AC3)

	while len(arc_queue) != 0:
		arc = arc_queue.pop()
	
		pos = arc[0][0]*9 + arc[0][1]
		pos1 = arc[1][0]*9 + arc[1][1]
		"print arc"
		"print 'val1 ' + str(sudok_AC3[arc[0][0]][arc[0][1]]) + ' domain1 ' + str(domains_AC3[pos])"
		"print 'val2 ' + str(sudok_AC3[arc[1][0]][arc[1][1]]) + ' domain2 ' + str(domains_AC3[pos1])"
		
		"""raw_input()"""
		if revise_arc(arc,sudok_AC3):
			
			"print 'revise ok'"
			"print 'new domain ' + str(domains_AC3[pos])"
			posx = arc[0][0]*9 + arc[0][1]
			if len(domains_AC3[posx]) == 0:
				"print arc[0][0]"
				"print arc[0][1]"
				break
			
			"""print "ants " + str(len(arc_queue))"""
			add_neighbours(arc)
			"""print "desp " + str(len(arc_queue))"""
		
		"print len(arc_queue)"
	
	"check AC3 succesfull"
	AC3_success = 1
	
	
	for dom in domains_AC3:
		if len(dom) > 1:
			AC3_success = 0
		
	
	if AC3_success == 1:
		
		for row in range(9):
			for col in range(9):
				if sudok_AC3[row][col] == 0:
					sudok_AC3[row][col] = domains_AC3[row*9 + col][0]
		file_print(sudok_AC3,'AC3',file)
	
	else:
		sudok_BTS = sudok
		backtrack_forward(sudok_BTS)
		file_print(sudok_BTS,'BTS',file)
	
	
	i = i + 1
	

	
	
	
		





	
	
	
	