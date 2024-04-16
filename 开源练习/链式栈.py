
class Node():
    def __init__(self,val,next=None):
        self.val =val
        self.next =next



class Linkea():
    def __init__(self):
        self.top = None


    def pushi(self,val):
        node = Node(val)
        node.next = self.top
        self.top = node



    def pop(self):
        if self.top is None:
            raise Exception("栈内没有值哦")
        value = self.top.val
        self.top =self.top.next
        return value

    def tod(self):
        if self.top is None:
            raise Exception("栈内没有数据")
        return self.top.val


if __name__ == '__main__':
    ls = Linkea()
    ls.pushi(1)
    ls.pushi(2)
    ls.pushi(3)
    print(ls.pop())
    print(ls.tod())