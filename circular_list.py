class Clist(list):
    def __getitem__(self, key):
        return super(Clist, self).__getitem__( int(key) % self.__len__() )

class Clist2(list):
    def __getitem__(self, key):
        
        # try normal list behavior
        try:
            return super(Clist2, self).__getitem__(key)
        except IndexError:
            pass
        # key can be either integer or slice object,
        # only implementing int now.
        try:
            index = int(key)
            index = index % self.__len__()
            return super(Clist2, self).__getitem__(index)
        except ValueError:
            raise TypeError

l = Clist()
for i in range(1,100):
    l.append(i)
    for j in range(1,100):
        l[j]
