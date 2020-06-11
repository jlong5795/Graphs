import random

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
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        
        # Add users
        for i in range(0, num_users):
            self.add_user(f'User {i}')

        # generate possible friendships
        possible = []

        # avoid dups by making sure the first number is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible.append((user_id, friend_id))

        # shuffle the possible friendships
        random.shuffle(possible)

        # Create friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id, visited=None):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path..
        
        First we need to search, recording the path as we go
        Once we get to our destination, add the destination and path to visited
        ( destination:[path] )
        Repeat for each friendship
        """
        q = Queue()
        q.enqueue([user_id])

        if visited == None:
            visited = {}  # Note that this is a dictionary, not a set

        # visited[user_id] = [user_id]
        # start with the provided ID and get its friends
        # for each of those friends, add to the dict { friend: [user_id, friend] }


        while q.size() > 0:
            # remove first element which is a node in a list
            path = q.dequeue()
            # get the last element in that list
            last_friend = path[-1]
            print(last_friend)

            if last_friend not in visited:
                # check neighbors
                visited[last_friend] = path
                for friend in self.friendships[last_friend]:
                    new_path = list(path)
                    # add a path to the neighbors
                    new_path.append(friend)
                    print(new_path)
                    q.enqueue(new_path)
        
        return visited
       


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

