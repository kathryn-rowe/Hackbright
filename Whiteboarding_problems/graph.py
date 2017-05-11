import Queue


class PersonNode(object):
    """A person node in a graph"""

    def __init__(self, name, adjacent=None):
        self.name = name

        if adjacent:
            assert isinstance(adjacent, set)
            self.adjacent = adjacent
        else:
            self.adjacent = set()


class FriendGraph(object):

    def __init__(self):
        self.nodes = set()

    def add_person(self, person):
        self.nodes.add(person)

    def set_friends(self, person1, person2):
        """Make friendships"""
        person1.adjacent.add(person2)
        person2.adjacent.add(person1)

    def are_connected(self, person1, person2):
        """Are they friends?"""

        to_visit = Queue()
        to_visit.enqueue(person1)
        seen = set()
        seen.add(person1)

        while not to_visit.is_empty():
            current = to_visit.dequeue()
            if current is person2:
                return True
            else:
                for friend in current.adjacent - seen:
                    to_visit.enqueue(friend)
                    seen.add(friend)

        return False
