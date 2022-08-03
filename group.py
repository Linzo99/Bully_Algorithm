class Group:
    """Group holding all members
        - name : name of the group
        - members : list of members: Member
        - leader : the leader of the group
    """

    def __init__(self, name):
        self.name = name
        self.members = []
        self.leader = None

    def add_member(self, *members):
        """add a member if not existing"""
        for m in members:
            if m not in self.members:
                self.members.append(m)
    
    def hold_election(self, sender):
        """hold an election if the leader is not reachable"""
        print(f"[!] Election request sent by [{sender}]")
        replies = []
        for m in self.members:
            #send the election request to members with higher score
            if sender!=m and m!=self.leader and m>sender:
                ans = sender.send("ELECTION", m)
                replies.append(ans)
        #return the list of replies to the sender
        return replies

    def choose_leader(self):
        """choose a leader if no available one(self.leader=None)"""
        
        if not self.members:
            raise Exception("No member to choose in")
        #choose the one with the best one
        self.leader = max(self.members)

    def update_leader(self, new_leader):
        """update leader after election and notify other members"""
        
        print(f"Updating the group leader...")
        self.leader = new_leader
        for m in self.members:
            if m != new_leader:
                new_leader.send("New Leader: "+str(self.leader), m)