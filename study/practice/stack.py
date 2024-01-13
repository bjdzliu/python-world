class Stack():
    def __init__(self,size):
        self.data=["null" for i in range(0,size)]
        self.size=size
        self.top=-1
    def push(self,content):
        if self.Full():
            print("zhsd")
        else:
            self.top=self.top+1
            self.data[self.top]=content
    def out(self):
        if self.Empty():
            print("ssss")
        else:
            print(self.dataa[self.top])
            self.data[self.top]='null'
            self.top=self.top-1
    def Full(self):
        if self.top==self.size-1:
            return True
        else:
            return False
    def Empty(self):
        if self.top==-1:
            return True
        else:
            return False
