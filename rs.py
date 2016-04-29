#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import readline
import fileinput

graph = {}
exceptions = {}
if len(sys.argv) == 1:
    print("Veuillez saisir vos relations.","La relation is_a doit être écrite avec cet orthographe.","Les relations des exceptions doivent être précédées par 'non'.","Terminez avec une ligne vide :", sep='\n')
    while True :
        relation = input("> ")
        relation = relation.strip() # No trailing whitespaces are accepted
        if not relation : # Nothing (maybe some ignored whitespaces)
            break
        relationNodes = relation.split(" ")
        if len(relationNodes) == 3 : # <subject> <relation> <object>
            if relationNodes[1] not in graph : # If the node doesn't exist
                graph[relationNodes[1]] = set() # Set of tuples, each tuple contains 2 nodes
            graph[relationNodes[1]].add((relationNodes[0], relationNodes[2]))
        elif len(relationNodes) == 4 and relationNodes[1] == "non": # Exception : <subject> non <relation> <object>
            if relationNodes[2] not in exceptions :
                exceptions[relationNodes[2]] = set()
            exceptions[relationNodes[2]].add((relationNodes[0], relationNodes[3]))
        else :
            print("Syntax erronée. Re-écrivez votre phrase !", file=sys.stderr)
else : # Read from files
    with fileinput.input(sys.argv[1]) as data_file : # Same operations for files
        for line in data_file :
            line = line.strip()
            if line.startswith("#") :
                continue
            if not line :
                break
            relationNodes = line.split(" ")
            if len(relationNodes) == 3 :
                if relationNodes[1] not in graph :
                    graph[relationNodes[1]] = set()
                graph[relationNodes[1]].add((relationNodes[0], relationNodes[2]))
            elif len(relationNodes) == 4 and relationNodes[1] == "non":
                if relationNodes[2] not in exceptions :
                    exceptions[relationNodes[2]] = set()
                exceptions[relationNodes[2]].add((relationNodes[0], relationNodes[3]))
            else :
                print("Syntax erronée dans le fichier {}, dans la ligne {} ! ignorée.".format(fileinput.filename(), fileinput.lineno()), file=sys.stderr)

if not graph : # No graph was given
    sys.exit()
print("Graphe :", graph, end='\n\n')

question = input("Introduisez votre question sous la syntax : <sujet> <relation> <objet>\n> ")
question = question.split(" ")

if len(question) == 1 :
    sys.exit()
elif len(question) != 3 :
    print("La syntaxe de la requête est erronée !", file=sys.stderr);
    sys.exit(1)

m1 = set()
m2 = set()
m1.add(question[0])
m2.add(question[2])
if "is_a" in graph : # Propagate only if there is some is_a relations
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
print("\nM1 propagé")
print(m1)
print("M2 propagé")
print(m2, end='\n\n')

solutions = set()
for a in m1 :
    for b in m2 :
        if (a,b) in graph[question[1]] and (a,b) not in exceptions.get(question[1], set()) :
            solutions.add((a,b))

if not solutions :
    print("Il n y a pas de solutions")
else :
    print("Solutions :")
    for (a,b) in solutions :
        print(a, question[1], b)
print()
