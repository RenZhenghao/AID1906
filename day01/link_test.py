from linklist import *

l01 = LinkList()
l02 = LinkList()

l01.init_list([5, 5, 7, 8, 10, 12])
l02.init_list([2, 3, 4, 9, 16, 17, 20])

l01.merge(l01, l02)
l01.show()
