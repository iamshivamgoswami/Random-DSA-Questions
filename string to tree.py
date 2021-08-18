

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:

        return self.tree(s,0)[0]

    def get_num(self,s,i):
        is_negative=False
        if s[i]=="-":
            is_negative=True
            i+=1
        num=0
        while i<len(s) and s[i].isdigit():
            num=num*10+int(s[i])
            i+=1
        return num if not is_negative else -num,i
    def tree(self,s,i):
        if i==len(s):
            return None,i

        val,i=self.get_num(s,i)
        node=TreeNode(val)
        if i<len(s) and s[i]=="(":
            node.left,i=self.tree(s,i+1)
        if node.left and i<len(s) and s[i]=="(":
            node.right,i=self.tree(s,i+1)
        return node,i+1



