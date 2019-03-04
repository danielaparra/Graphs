"""
Simple graph implementation
"""

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return (len(self.queue))

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return (len(self.stack))


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")
    
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist")
    
    def bft(self, starting_vertex_id):
        # Create an empty queue
        q = Queue()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Queue
        q.enqueue(starting_vertex_id)
        # While the queue is not empty....
        while q.size() > 0:
           # Dequeue the first node from the queue
           v = q.dequeue()
           # If that node has not been visted...
           if v not in visited:
              # Mark it as visited
              print(v)
              visited.add(v)
              # Then, put all of it's children into the queue
              for neighbor in self.vertices[v]:
                  q.enqueue(neighbor)
    
    def dft(self, starting_vertex_id):
        # Create an empty stack
        s = Stack()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Stack
        s.push(starting_vertex_id)
        # While the stack is not empty....
        while s.size() > 0:
           # Pop the top node from the stack
           v = s.pop()
           # If that node has not been visted...
           if v not in visited:
              # Mark it as visited
              print(v)
              visited.add(v)
              # Then, put all of it's children into the stack
              for neighbor in self.vertices[v]:
                  s.push(neighbor)

    def dft_recursive(self, starting_vertex_id, visited=set()):

        # Check that current vertex has been visited.
        if starting_vertex_id not in visited:
            # If not, print vertex and add to visited set.
            print(starting_vertex_id)
            visited.add(f'{starting_vertex_id}')

        # Iterate through its neighbors
        for neighbor in self.vertices[f'{starting_vertex_id}']:
            # If neighbor is already visited, move to the next neighbor.
            if neighbor in visited:
                return
            # Otherwise call recursive function.
            else:    
                self.dft_recursive(neighbor, visited)

    def bfs(self, start, target):
        # Create an empty queue
        q = Queue()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in a list in our Queue
        q.enqueue([start])
        # While the queue is not empty....
        while q.size() > 0:
            # Grab the current path.
            path = q.dequeue()
            # Grab the last vertex in the path.
            curr_vertex = path[-1]

            # If current vertex is the target, return the path.
            if curr_vertex == target:
                return path
            
            # If current vertex has not been visited, add to visited list.
            if curr_vertex not in visited:
                visited.add(curr_vertex)

                # Iterate through all neighbors.
                for neighbor in self.vertices[f'{curr_vertex}']:
                    # Create new path and add current neighbor.
                    new_path = list(path)
                    new_path.append(neighbor)
                    # Add that new path to the queue.
                    q.enqueue(new_path)

            
            


