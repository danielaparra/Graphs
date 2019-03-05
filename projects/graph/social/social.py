import random
from queue import SimpleQueue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add x amount users where x = numUsers.
        for number in range(numUsers):
            self.addUser(f'{number + 1}')

        # Create friendships
        
        total_no = numUsers * avgFriendships // 2
        possible = []
        for userId in self.users:
            for friendId in range(userId + 1, self.lastID + 1):
                possible.append((userId, friendId))

        fships = random.sample(possible, total_no)
        for friendship in fships:
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # Create an empty dictionary.
        visited = {}  
        
        # Iterate through users to find all social paths.
        for social_connection in self.users:
            self.bfs(userID, social_connection, visited)

        return visited

    def bfs(self, start, target, visited):
        # Create an empty queue.
        q = SimpleQueue()
        # Put the starting userID in a list in our queue.
        q.put([start])
        # While the queue is not empty....
        while not q.empty():
            # Grab the current path.
            path = q.get()
            # Grab the last vertex in the path.
            curr_vertex = path[-1]

            # If current vertex is the target, return the path.
            if curr_vertex == target:
                visited[target] = path
                return

            # Iterate through all neighbors.
            for social_connection in self.friendships[curr_vertex]:
                if social_connection != start and social_connection not in path:
                    # Create new path and add current neighbor.
                    new_path = list(path)
                    new_path.append(social_connection)
                    # Add that new path to the queue.
                    q.put(new_path)

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
