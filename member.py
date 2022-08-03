from random import randrange

class Member:
    """Member class
        - name : name of the member
        - score : the score of the member
        - group : the group of the member
        - is_active : if member is reachable or not
    """

    def __init__(self, name, group, active=True):

        self.name = name
        self.group = group
        self.score = randrange(10)
        self.is_active = active
        #add the member to the given group
        self.group.add_member(self)

    def send(self, msg, target):
        """send message to another member"""
        
        print(f"[{self}]: sending msg to {target.name}")
        reply = target.recv(msg, self)
        #if no answer received and the target is the leader
        #we hold an election
        if not reply and target == self.group.leader:
            replies = self.group.hold_election(self)
            #if no reply the the sender become the new leader
            if not any(replies):
                self.group.update_leader(self)
        else:
            return reply

    def recv(self, msg, sender):
        """reveiving a message"""
        
        #we can't answer if not active
        if not self.is_active:
            return None

        if msg == "ELECTION":
            replies = self.group.hold_election(self)
            #if no reply the the sender become the new leader
            if not replies:
                self.group.update_leader(self)
            #if the sender has a lower score we tell him to stop(bully)
            if self > sender:
                return "OK"

        elif msg.startswith("New Leader"):
            print(f"[{self}] Got a new leader: {self.group.leader}")

        else:
            return msg

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.score > other.score

    def __lt__(self, other):
        return other > self

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name} - {self.score}"