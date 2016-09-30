import shelve
from user_class import User

s = shelve.open("./user.db")
user1 =User('h', 'j') 
print user1
user1=s['user73647361']
print user1