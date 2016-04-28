This is a simple implementation of the propagation-based algorithm for question answering in sementic networks.


We'll take this example to illustrate all the process from the creation of the graph to the question answering.

![Graph](https://raw.githubusercontent.com/SamyMe/Semantic-Network-Processing/master/graph.png)

The graph is constructed by giving a serie of statements.

For our example, the statements would be as follows :
- Asian is_a Human
- European is_a Human
- Chinese is_a Asian
- Japanese is_a Asian
- French is_a European
- French eat snail
- Japanese eat rice
- Chinese eat Grasshopper
- Grasshopper is_a Insect

It is very important to keep the exact same spelling for relations and actors.
Also, *is_a* needs to be in this exact spelling.

This will create the following graph structure :

```python
{'is_a': [('Asian', 'Human'), ('European', 'Human'), ('Chinese', 'Asian'), ('Japanese', 'Asian'), ('French', 'European'), ('Grasshopper', 'Insect')], 'eat': [('French', 'snail'), ('Japanese', 'rice'), ('Chinese', 'Grasshopper')]}
```

In order to answer the question "Which Humans eat Insects" we write : Human eat Insect.
The answer is given to us as: < **Chinese eat Grasshopper** > since chinese are Human, and Grasshoppers are insects.
