## BULLY ALGORITHM
In distributed computing, the bully algorithm is a method for dynamically electing a coordinator or leader from a group of distributed computer processes. The process with the highest process ID number from amongst the non-failed processes
is selected as the coordinator.

Here is a simple implementation in python


```python
from group import Group
from member import Member
grp = Group("bittech")
alioune = Member("alioune", grp)
medoune = Member("medoune", grp)
moussa = Member("moussa", grp)
alex = Member("alex", grp)
grp.choose_leader()
```


```python
print(grp.members)
print("Current group leader:",grp.leader)
```

    [alioune - 4, medoune - 3, moussa - 6, alex - 1]
    Current group leader: moussa



```python
grp.leader.is_active = False
```


```python
alex.send("hi", grp.leader)
```

    [alex]: sending msg to moussa
    [!] Election request sent by [alex]
    [alex]: sending msg to alioune
    [!] Election request sent by [alioune]
    Updating the group leader...
    [alioune]: sending msg to medoune
    [medoune] Got a new leader: alioune
    [alioune]: sending msg to moussa
    [alioune]: sending msg to alex
    [alex] Got a new leader: alioune
    [alex]: sending msg to medoune
    [!] Election request sent by [medoune]
    [medoune]: sending msg to moussa
    [alex]: sending msg to moussa



```python
grp.leader
```




    alioune - 4


