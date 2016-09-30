from user_class import User
import shelve
s = shelve.open("./user.db")
user1=user2=User("Vasa", "Pupkin")
user3=user4=User("Vasa1", "Pupkin1")
s['user73647361']=user1
s['user2']=user2
s['user3']=user3
s['user4']=user4
s.close()