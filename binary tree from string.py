class Solution:
    def str2tree(self, s: str) -> TreeNode:
        return self._str2treeInternal(s, 0)[0]
    def _getNumber(self,s,index):
        is_negative=False
        if s[index]=="-":
            is_negative=True
            index=index+1
        number=0
        while index<len(s) and s[index].isdigit():
            number=number*10+int(s[index])
            index+=1
        return number if not is_negative else -number,index

    def _str2tree(self,s,index):
        if index==len(s):
            return None,index
        value,index=self._getNumber(s,index)
        node=TreeNode(val)
        if index<len(s) and s[index]=="(":
            node.left,index=self._str2tree(s,index+1)
        if node.left and index<len(s) and s[index]=="(":
            node.right,index=self._str2tree(s,index+1)
        return node,index+1

