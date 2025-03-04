
class Solution:
    def decodedString(self, s):
        # code here
        stack=[]
        for item in s:
            if item=="]":
                curr=""
                while stack and stack[-1]!="[":
                    curr=stack.pop()+curr
                stack.pop()
                val=""
                while stack and stack[-1].isnumeric():
                    val=stack.pop()+val
                stack.append(curr*int(val))
            else:
                stack.append(item)
        ans=""
        while stack:
            ans=stack.pop()+ans
        return ans
