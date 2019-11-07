import itertools
from simpleai.search import (CspProblem, backtrack, min_conflicts,
                             MOST_CONSTRAINED_VARIABLE,
                             LEAST_CONSTRAINING_VALUE,
                             HIGHEST_DEGREE_VARIABLE)
def Problema_csp_Charlas():
	variables = [
	'DjgG', #0   40 personas_   computadoras
	'IntoP',#1                  computadoras_                    turno mañana
	'Div',#2     150 personas_               proyector/audio_    turno tarde     unica charla en horario
	'DevP',#3    150 personas_               proyector/audio_    turno tarde_    unica charla en horario
	'ApiDjg',#4                              proyector
	'DSA',#5                                                                     planta baja
	'Unitst',#6                              proyector
	'EditCP',#7                              proyector/audio
	'MscP',#8    >60 personas_               proyector
	'Neg',#9                                                     turno mañana_   42/lab
	'AnImg',#10                                                                   magna/42
	'SatEsp',#11                              proyector_          turno tarde
	'PubLib',#12                              proyector
	'Pand'#:13                                proyector_                          planta alta
	]

	aulas_disponibles = { 'DjgG':[3],'IntoP':[3],'Div':[1],'DevP':[1],'ApiDjg':[1,2],'DSA':[1,3],'Unitst':[1,2],
	'EditCP':[1],'MscP':[1,2],'AnImg':[1,2],'SatEsp':[1,2],'PubLib':[1,2],'Pand':[2] }

	horarios = [10,11,14,15,16,17]

	dominios = {}

	for charla,aula in aulas_disponibles.items():
		dominios[charla] = []

	for charla, aulas in aulas_disponibles.items():
		dominios = []
		for aula in aulas:
			if charla in dominios:
				for horas in horarios():
					if (horas <12) and ((charla=='IntoP') or (charla=='Neg')): #charlas solo por la mañana
						dominios[charla].append((aula,hora))
					elif horas >=12 and ((charla=='Div') or (charla=='DevP') or (charla=='SatEsp')): #charlas solo por la tarde
						dominios[charla].append((aula,hora))
					dominios[charla].append((aula,hora))

	restricciones = []

	for charla1, charla2 in itertools.combinations(variables,2):
		restricciones.append(((charla1,charla2),charla_asig))

	for var in variables:
		if var != variables[2]:
			restricciones.append(((variables[2],var),charla_unica))
		if var != variables[3]:
			restricciones.append(((variables[3],var),charla_unica))
	

	return CspProblem(variables, dominios, restricciones)


#no debe haber otra charla en horario para Charla[3] y Charla[4]
def charla_unica(vars, vals):
	return vals[0][1] != vals[0][1]


#no debe haber charlas asignadas a un mismo horario misma aula
def charla_asig(vars, vals):
	return vals[0] != vals[1]

def resolver(metodo_busqueda, iteraciones):
	problema = Problema_csp_Charlas()

	if metodo_busqueda == "backtrack":
		resultado = backtrack(problema)

		#resultado = backtrack(problema, variable_heuristic=MOST_CONSTRAINED_VARIABLE, value_heuristic=LEAST_CONSTRAINING_VALUE)
	elif metodo_busqueda == "min_conflicts":
		resultado = min_conflicts(problema, iterations_limit=iteraciones)

	return resultado

metodo = "backtrack"
iteraciones = None
#viewer = BaseViewer()

#metodo = "min_conflicts"
#iteraciones = 100

inicio = datetime.now()
result = resolver(metodo, iteraciones)
print("tiempo {}".format((datetime.now() - inicio).total_seconds()))
print(result)
print(repr(result))