class User():
    def __init__(self, name, sname):
        self.name=name
        self.sname=sname
    def get_full_name(self):
        return "%s %s"%(self.sname, self.name)
    def __repr__(self):
        return self.get_full_name()
    def __del__(self):
        print "Delete object %s" % self.get_full_name()