class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkList:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node=ListNode(data)
        if self.head==None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    def delete(self,count):
        p=self.head
        prev_p=None
        if self.head==None:
            return
        while p and p.data!=count:
            prev_p=p
            p=p.next
        if p:
            return
        prev_p.next=p.next
        p=None
    def print_list(self):
        p=self.head
        while p:
            print(p.data,end="->")
            p=p.next
        print("null")
    def chlist(self,a,data):
        p=self.head
        i=1
        if self.head==None:
            return
        while p:
            p=p.next
            i+=1
            if i==a:
                p.data=data
                break
    def insert(self,a,data):
        new_node=ListNode(data)
        p=self.head
        i=1
        if a== 1:
            new_node.next = p
            self.head = new_node
            return
        while p and i<a-1:
            p=p.next
            i+=1
        if p is None:
            print("位置错误")
            return
        new_node.next = p.next
        p.next = new_node








train = LinkList()
train.append("车厢1-煤炭")
train.append("车厢2-木材")
train.append("车厢3-钢材")
print("初始列车：")
train.print_list()
train.insert(2,"大帅哥")
train.chlist(3,"帅哥")
train.print_list()