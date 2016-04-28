#!/usr/bin/env python2
# -*- coding: utf-8 -*-

relation="a"
graph={}
print "\nVeuillez saisir vos relations\nLa relation is_a doit être écrite avec cet orthographe.\nTerminez avec une ligne vide :\n"
while len(relation) !=0:
	relation = raw_input("> ")
	if len(relation)==0:
		break

	relation=relation.split(" ")

	if len(relation)!=3:
		print "Syntax erronée. Re-écrivez votre phrase :"
		continue

	if not relation[1] in graph:
		graph[relation[1]]=[]

	#a=relation.pop(0)
	#b=relation.pop(-1)
	#relation='_'.join(relation)
	graph[relation[1]].append((relation[0],relation[2]))

print "Graphe :"
print graph
print "\n"

question= raw_input("Saisir votre question avec la syntax suivante (sans les '<,>'):\n< amine mange soterelle ? >\n") #<qui mange amine ?> \n2- <amine mange qui ?>\n3- <amine mange sautrelle ?>")
question=question.split(" ")

m1=[]
m2=[]

m1.append(question[0])
m2.append(question[2])

dontstop=True

while dontstop:
	dontstop=False
	for element in m1:
		for tupl in graph["is_a"]:
			if element == tupl[1] and not (tupl[0] in m1):
				m1.append(tupl[0])
				dontstop=True
print "M1 propagé"
print m1
print "\n"

dontstop=True

while dontstop:
	dontstop=False
	for element in m2:
		for tupl in graph["is_a"]:
			if element == tupl[1] and not (tupl[0] in m2):
				m2.append(tupl[0])
				dontstop=True
print "M2 propagé"
print m2
print "\n"

solution=[]
for a in m1:
	for b in m2:
		if (a,b) in graph[question[1]]:
			solution.append((a,b))

if len(solution)==0:
	print "Il n y a pas de solutions"
else:
	print "Solutions :"
	for (a,b) in solution:
		print a+" "+question[1]+" "+b




