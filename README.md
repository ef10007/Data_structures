# Data structures 

1. [Heaps](https://github.com/ef10007/Data_structures/blob/master/heaps.py)

Heaps are suited for maintaining a list of items in order of priority. For example, if a marketing agency wants to prioritize projects that come up for higher-paying clients, it would lend itself to helping the agency achieve this by using a max-heap (opposite of min-heap) to constantly re-adjust our heap such that the highest paying client is the root of the heap.

2. [Queues](https://github.com/ef10007/Data_structures/blob/master/queue.py)

Queues follow a FIFO (first in, first out) protocol, making them ideally suited to help a customer service desk, for instance, building some software that allows representatives to reply to tickets in the order they are received. Hence, the first customer ticket added will be the first one addressed.

3. [Linked lists](https://github.com/ef10007/Data_structures/blob/master/linkedlists.py)

Linked lists are helpful in situations where you need to traverse a list or add to the end. If you've decided to build your own music playlist command line program, you may want to be able to select songs that starting with the first, add a new song to the end of the playlist and most importantly, skip to the next song. Stacks do not allow you to traverse a list. Therefore, you would model our playlist with a linked list and traverse the nodes to move to the next song. We can also enqueue() a song to the end of the playlist.
 
4. [Stacks](https://github.com/ef10007/Data_structures/blob/master/stack.py)

Stacks follow a LIFO (last in, first out) protocol. When you've been asked to add "undo" functionality to a custom text editor, it would be ideally suited to implement this feature. The last change added should be the first change removed for an undo functionality.


5. [Hash tables](https://github.com/ef10007/Data_structures/blob/master/hashmaps2.py)

Hash tables are ideal for assigning and retrieving data in the fastest way possible, not for tracking the most recently added item. For example, if you are building an application that needs to keep track of each user's permissions, you can map each user_id to either True or False in the Hash table for each given permission respectively. It allows you to add and retrieve user permissions by user_id.


6. [Graphs](https://github.com/ef10007/Data_structures/blob/master/graphs.py)

Graphs are ideal for keeping track of various pathways between nodes. If you're helping an airline keep track of its various flight paths, as well as connecting flights available, you want to model this using a data structure that will allow you to introduce additional airports as the airline gets set up in new cities. The airline's flight paths can be modeled by a graph with the airports as vertices and the flights as edges.

7. [Trees](https://github.com/ef10007/Data_structures/blob/master/trees.py)

Trees are ideal for modeling hierarchical relationships, making them ideally suited for modeling the control flow of possible moves given a limited number of choices. For example, assume that you are building a tic-tac-toe game so that a player can play against the computer. In order to do this, you need the game to keep track of possible moves given different player choices and with the trees structure, the computer can use a tree to branch to its next move, depending on the player’s move.

8. [Nodes](https://github.com/ef10007/Data_structures/blob/master/nodes.py)

Nodes contain data, which can be a variety of data types and links to other nodes. If a node has no links, or they are all null, you have reached the end of the path you were following returning 'None'. It can be orphaned if there are no existing links to them. For instance, consider the following nodes and links: a -> n -> t. If you want to remove node n, but preserve node t, you can do this by changing the link on a to point to t using a.set_link_node(t).

# Asymptotic Notation

Instead of timing a program, through asymptotic notation, we can calculate a program’s runtime by looking at how many instructions the computer has to perform based on the size of the program’s input: N, positive integer.

1. Big Theta (Θ)

```
Function with input that is a list of size N: 

   For each value in list:
    Print the value
````

With a list of size N, the program has a runtime of N because the program has to print a value N times. Thus, we would say the runtime is Θ(N) in this case.

```
Function that has integer input N:

    Set a count variable to 0
    
    Loop while N is not equal to 1:
        Increment count
        N = N/2
    Return count
```
In every case, with an integer N, the loop will iterate log2(N) times(= log(2,N) times). However, because we drop constants in asymptotic notation, we would say that the runtime of this program is Θ(log N).

2. Common Runtimes

 Below is a list of common runtimes that run from fastest to slowest.

* Θ(1) Constant runtime. This is the runtime when a program will always do the same thing regardless of the input.
* Θ(log N). Logarithmic runtime. Often used to search algorithms.
* Θ(N). Linear runtime. Often used when you have to iterate through an entire dataset.
* Θ(N\*logN). You will see this runtime in sorting algorithms.
* Θ(N2). An example of a polynomial runtime. Often used to search through a two-dimensional dataset (like a matrix) or nested loops.
* Θ(2N). Exponential runtime. Often used in recursive algorithms.
* Θ(N!). Factorial runtime. Often used to generate all of the different permutations(arrangement) of something. For instance, a program that generates all the different ways to order the letters “abcd” would run in this runtime.

3. Big Omega (Ω) and Big O (O)

 We use big Omega(Ω) to describe the best case and big O(O) to describe the worst case.
 ```
 This program has a best case runtime of Θ(1) and a worst case runtime of Θ(N).
 This program has a runtime of Ω(1) and a runtime O(N).
 ```
 However, presenting runtime of Θ(N) only is not true as the program does not have a linear runtime in every case, only the worst case.
 
 4. Adding Runtimes
 
 ```
 Function that takes a positive integer N:
    Set a variable i equal to 1
    Loop until i is equal to N:
        Print i
        Increment i

    Set a count variable to 0
    Loop while N is not equal to 1:
        Increment count
        N = N/2
    Return count
 ```
 
In the first loop, we iterate until we reach N. Thus the runtime of the first loop is linear runtime Θ(N). In other hands, the second loop runs in Logarithmic runtime Θ(log N). The overall runtime of this function will be Θ(N) + Θ(log N). However, when analyzing the runtime of a program, we only care about the slowest part of the program, hence, take a dominant term N grows much faster then log and the runtime of the function is going to be just Θ(N).
It is also appropriate to say the runtime is O(N) because if it runs in Θ(N) for every case, then it also runs in Θ(N) for the worst case. Most of the time people will just use big O notation.
