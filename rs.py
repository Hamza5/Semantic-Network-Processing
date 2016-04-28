#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys

graph={}
print "\nVeuillez saisir vos relations\nLa relation is_a doit être écrite avec cet orthographe.\nTerminez avec une ligne vide :\n"
while True :
	relation = raw_input("> ")
	if not relation :
		break
	relationNodes = relation.split(" ")
	if len(relationNodes) != 3 :
		print "Syntax erronée. Re-écrivez votre phrase :"
		continue
	if relationNodes[1] not in graph : # If the node doesn't exist
		graph[relationNodes[1]] = set() # Set of tuples, each tuple contains 2 nodes
	graph[relationNodes[1]].add((relationNodes[0], relationNodes[2]))

if not graph : # No graph was given
    sys.exit()

print "Graphe :"
print graph
print "\n"

question = raw_input("Saisir votre question en cette syntax : amine mange soterelle\n> ")
question = question.split(" ")

m1 = set()
m2 = set()

m1.add(question[0])
m2.add(question[2])

dontstop = True

while dontstop:
	dontstop = False
	temp = set()
	for element in m1:
		for tupl in graph["is_a"]:
			if element == tupl[1] and tupl[0] not in m1:
				temp.add(tupl[0])
				dontstop = True
        m1.update(temp)
print "\n"
print "M1 propagé"
print m1

dontstop = True
while dontstop:
	dontstop = False
	temp = set()
	for element in m2:
		for tupl in graph["is_a"]:
			if element == tupl[1] and tupl[0] not in m2:
				temp.add(tupl[0])
				dontstop = True
        m2.update(temp)
print "M2 propagé"
print m2
print "\n"

solutions = set()
for a in m1 :
	for b in m2 :
		if (a,b) in graph[question[1]]:
			solutions.add((a,b))

if not solutions :
	print "Il n y a pas de solutions"
else :
	print "Solutions :"
	for (a,b) in solutions :
		print a+" "+question[1]+" "+b


