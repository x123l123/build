class Hash:
    def __init__(self,size=10):
        self.size=size
        self.table=[[]for i in range(self.size)]
    def _hash(self,key):
        return hash(key) % self.size
    def insert(self,key,value):
        index=self._hash(key)
        bucket=self.table[index]
        for i,(k,v) in enumerate(bucket):
            if k==key:
                bucket[i]=(key,value)
                return
        bucket.append((key,value))
    def get(self,key):
        index = self._hash(key)
        bucket = self.table[index]
        for (k,v) in bucket:
            if k==key:
                return v
        return None
    def delete(self,key):
        index = self._hash(key)
        bucket = self.table[index]
        for i,(k,v) in enumerate(bucket):
            if k==key:
                del bucket[i]
                return
        return None
    def print_hash(self):
        for bucket in self.table:
            print(bucket)


has=Hash()
has.insert("凤凰传奇", "111111")
has.insert("tfboys", "222222")
has.insert("汪峰", "333333")
has.insert("周杰轮", "444444")
has.insert("林俊结", "555555")
has.insert("王丽红", "6666666")
has.print_hash()
print("查找key")
print(has.get("周杰轮"))
print("删除key")
has.delete("周杰轮")