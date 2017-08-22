import math

"""commmon functions"""


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
		print 'Motherfucker'
		pretty_print(sud_l)
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



for c in content:
	

	sudok = string_to_list(c)
	
	sudok = convert_to_r_c(sudok)
	
	
	
	list_of_sudoks.append(sudok)


i = 0
for sudok in list_of_sudoks:
	
	if i > 410:
		break
		
	
	"print get_domains( sudok )"
	
	backtrack_forward(sudok)
	i = i + 1
	
	
	
		





	
	
	
	