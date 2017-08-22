
import math
from datetime import datetime


"LOAD DATA"



letters = ['A','B','C','D','E','F','G','H','I']
numbers = ['1','2','3','4','5','6','7','8','9']


with open('sudokus_start.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content] 


"function to convert item in content to dictionary"
"dictionary considers columns from A to I, rows from 1 to 9"

def pretty_print(sak):
	
	for ll in numbers:
		print sak['A'+ll] + sak['B'+ll] + sak['C'+ll] + ' ' + sak['D'+ll] + sak['E'+ll] + sak['F'+ll] + ' ' + sak['G'+ll] + sak['H'+ll] + sak['I'+ll]
	

def string_to_dictionary(item):
	
	dict = {}
	i = 0
	for c in item:
		

		
		key = str(chr((i % 9) + 65)) + str(int(1 + math.floor(i/9)))
		
		dict[key] = c
		
		
		i = i + 1
		
	return dict
	



def create_initial_queue(sud):
	
	q = set()
	
	for k1,k2 in sud:
		"linea"
		
		for nn in numbers:
			if nn != k2:
				q.add((k1+k2,k1+nn))
				
		
		"columna"
		
		for kk in letters:
			if kk != k1:
				q.add((k1+k2,kk+k2))
				
		
		"cubo"
		
		for h1,h2 in sud:
			
			kkk = k1+k2
			hhh = h1+h2
			if get_cube(k1,k2) == get_cube(h1,h2) and kkk != hhh:
				q.add((k1+k2,h1+h2))
				
	
	return q
	
	
def get_cube(letter,number):
	
	if letter in ['A','B','C'] and number in ['1','2','3']:
		return 1
	if letter in ['D','E','F'] and number in ['1','2','3']:
		return 2
	if letter in ['G','H','I'] and number in ['1','2','3']:
		return 3
	if letter in ['A','B','C'] and number in ['4','5','6']:
		return 4
	if letter in ['D','E','F'] and number in ['4','5','6']:
		return 5
	if letter in ['G','H','I'] and number in ['4','5','6']:
		return 6
	if letter in ['A','B','C'] and number in ['7','8','9']:
		return 7
	if letter in ['D','E','F'] and number in ['7','8','9']:
		return 8
	if letter in ['G','H','I'] and number in ['7','8','9']:
		return 9


def update_domains(var,val):
	
	global domains_BTS
	letra = var[0]
	numero = var[1]
	cubo = get_cube(letra,numero)
	
	
	"lineas"
	for nn in numbers:
		if nn != numero:
			xj = letra+nn
			if xj !=  var:
				if val in domains_BTS[xj]:
					domains_BTS[xj].remove(val)
				


	"columnas"
	for kk in letters:
		if kk != letra:
			xj = kk+numero

			if xj !=  var:
				if val in domains_BTS[xj]:
					domains_BTS[xj].remove(val)



	"cubos"
	for kk in letters:
		for nn in numbers:
			code = kk+nn
			if code != var and cubo == get_cube(kk,nn):
				if val in domains_BTS[code]:
					domains_BTS[code].remove(val)
	
	
def update_domains2(var,val):
	
	global domains_BTS
	letra = var[0]
	numero = var[1]
	cubo = get_cube(letra,numero)
	
	
	"lineas"
	for nn in numbers:
		if nn != numero:
			xj = letra+nn
			if xj !=  var:
				if val in domains_BTS[xj]:
					domains_BTS[xj].add(val)
				


	"columnas"
	for kk in letters:
		if kk != letra:
			xj = kk+numero

			if xj !=  var:
				if val in domains_BTS[xj]:
					domains_BTS[xj].add(val)



	"cubos"
	for kk in letters:
		for nn in numbers:
			code = kk+nn
			if code != var and cubo == get_cube(kk,nn):
				if val in domains_BTS[code]:
					domains_BTS[code].add(val)
	


def create_domains(sud):
	
	dict = {}

	
	for k1,k2 in sud:
		
		code = k1+k2

		if sud[code] == '0':
			dict[code] = ['1','2','3','4','5','6','7','8','9']
		else:
			dict[code] = []
		
	for k1,k2 in sud:	
		var = k1+k2
		if sud[var] != 0:
			letra = k1
			numero = k2
			cubo = get_cube(letra,numero)
			
			val = sud[var]
			"lineas"
			for nn in numbers:
				if nn != numero:
					xj = letra+nn
					if xj !=  var:
						if val in dict[xj]:
							dict[xj].remove(val)
				


			"columnas"
			for kk in letters:
				if kk != letra:
					xj = kk+numero

					if xj !=  var:
						if val in dict[xj]:
							dict[xj].remove(val)



			"cubos"
			for kk in letters:
				for nn in numbers:
					code = kk+nn
					if code != var and cubo == get_cube(kk,nn):
						if val in dict[code]:
							dict[code].remove(val)

	return dict


def revise_arc(arc2,sud,domains1):
	
	
	answer = 0
	if sud[arc2[0]] == '0':

		if sud[arc2[1]] == '0' and len(domains1[arc2[1]]) == 1:
			for val in domains1[arc2[0]]:
				if domains1[arc2[1]][0] == val:

					domains1[arc2[0]].remove(val)
					answer = 1
		
		if sud[arc2[1]] != '0':
		
			for val in domains1[arc2[0]]:
			
				if sud[arc2[1]] == val:
				
					domains1[arc2[0]].remove(val)
					answer = 1
	
	
	return answer


def add_neighbours(arc1):
	
	
	letra = arc1[0][0]
	numero = arc1[0][1]
	cubo = get_cube(letra,numero)
	
	"print 'add ' + str(arc1[0]) + str(arc1[1])"
	
	"lineas"
	for nn in numbers:
		if nn != numero:
			xj = letra+nn
			if xj !=  arc1[1]:
				arc_queue.add((xj,arc1[0]))
				


	"columnas"
	for kk in letters:
		if kk != letra:
			xj = kk+numero

			if xj !=  arc1[1]:
				arc_queue.add((xj,arc1[0]))



	"cubos"
	for kk in letters:
		for nn in numbers:
			code = kk+nn
			if code != arc1[0] and code != arc1[1] and cubo == get_cube(kk,nn):
				arc_queue.add((code,arc1[0]))



				

def bts_assignment_complete(assign):
	
	respuesta = 1
	for kk in letters:
		for nn in numbers:
			code = kk+nn
			if assign[code] == '0':
				respuesta = 0
	return respuesta


def select_unassigned_mrv(sud):
	
	output = 'ZZ'
	
	
	initial_length = 10
	for kk in letters:
		for nn in numbers:
			code = kk+nn

			if sud[code] == '0':
				length1 = len(domains_BTS[code])
				if length1 < initial_length:
					initial_length = length1
					output = code
	"print str(output) + ' ' + str(domains1[output])"
	return output
	
	
	

def order_domain_values_random(var):
	
	return domains_BTS[var]

def check_consistency(var,value,assignment):
	
	respuesta = 1
	letra = var[0]
	numero = var[1]
	cubo = get_cube(letra,numero)
	
	
	
	"lineas"
	for nn in numbers:
		if nn != numero:
			xj = letra+nn
			if assignment[xj] == value:
				respuesta = 0
				
				


	"columnas"
	for kk in letters:
		if kk != letra:
			xj = kk+numero
			if assignment[xj] == value:
				respuesta = 0



	"cubos"
	for kk in letters:
		for nn in numbers:
			code = kk+nn
			if get_cube(kk,nn) == cubo and code != var:
				if assignment[code] == value:
					respuesta = 0
	return respuesta


def forward_checking(var,val):
	
	letra = var[0]
	numero = var[1]
	cubo = get_cube(letra,numero)
	
	
	"lineas"
	for nn in numbers:
		if nn != numero:
			xj = letra+nn
			if xj !=  var:
				if val in domains[xj]:
					domains[xj].remove(val)
				


	"columnas"
	for kk in letters:
		if kk != letra:
			xj = kk+numero

			if xj !=  var:
				if val in domains[xj]:
					domains[xj].remove(val)



	"cubos"
	for kk in letters:
		for nn in numbers:
			code = kk+nn
			if code != var and cubo == get_cube(kk,nn):
				if val in domains[code]:
					domains[code].remove(val)


def print_line(sud,alg):
	
	empty_string = ''
	for nn in numbers:
		for kk in letters:
			empty_string = empty_string + sud[kk+nn]
	print empty_string+' ' + alg




def backtrack(assignment):
	
	

	if bts_assignment_complete(assignment) == 1:

		"""raw_input('press key end')"""
		"pretty_print(assignment)"
		return 'break'
	
	var1 = select_unassigned_mrv(assignment)
	

	for value in domains_BTS[var1]:
		if check_consistency(var1,value,assignment) == 1:
			"print str(var1)+ ' ' + str(value) + str(domains_BTS[var1])"
			assignment[var1] = value
			update_domains(var1,value)
			"pretty_print(assignment)"
			"""raw_input('press key alg')"""
			result = backtrack(assignment)
			"print result"
			if result == 'break':
				return 'break'
			if result != 'Failure':
				"forward_checking(var1,value)"
				"print str(var1)+ ' ' + str(value)"
				return 'Ok'
				
			
			
			
		
		if assignment[var1] == value:
			
			"print str(var1)+ ' ' + str(value) + str(domains_BTS[var1])"
			assignment[var1] = '0'
			
		
	
	return 'Failure'
			



"""------------------------------------------------------------------------"""



list_of_sudokus = []



for con in content:
	
	
	list_of_sudokus.append(string_to_dictionary(con))


	
	





rr = 1
for sudok in list_of_sudokus:
	
	t1 = datetime.now()
	
	

	sudok_AC3 = sudok.copy()


	kao = 0
	arc_queue = create_initial_queue(sudok_AC3)
	
	domains_AC3 = create_domains(sudok_AC3)
	

	
	

	ii = 1
	while len(arc_queue) != 0:
		
		arc = arc_queue.pop()
		
		if arc[0] == 'A6':

			ii = ii + 1
		
		
		if revise_arc(arc,sudok_AC3,domains_AC3) == 1:
			
			
			if len(domains_AC3[arc[0]]) == 0:
				print 'no hay solucion'
				
			
			add_neighbours(arc)
			

	
	for nn in numbers:
		for kk in letters:
			
			key = kk + nn

			if sudok_AC3[key] == '0':

				if len(domains_AC3[key]) == 1:
					sudok_AC3[key] = domains_AC3[key][0]
				else:
					kao = 1
					
	
	if kao == 0:
		
		print_line(sudok_AC3,'AC3')
		delta = datetime.now() - t1
		"print delta.total_seconds()"



	
	
	"""BTS"""
	
	
	sudok_BTS = sudok.copy()
	
	
	"""print 'inicio BTS'
	pretty_print(sudok_BTS)"""
	
	
	
	domains_BTS = create_domains(sudok_BTS)
	
	result = backtrack(sudok_BTS)
	if kao != 0:
		print_line(sudok_BTS,'BTS')
		"""print 'BTS'"""
		delta = datetime.now() - t1
		"print delta.total_seconds()"
		
		"""pretty_print(sudok_BTS)"""
	























	rr = rr + 1




	
	
	







































