class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        arr = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                while stack and stack[-1] != '[':
                    arr.append(stack.pop())
                stack.pop()
                times = []
                while stack and stack[-1].isdigit():
                    times.append(stack.pop())
                times.reverse()
                times = "".join(times)
                arr.reverse()
                stack.extend(arr*int(times))
                arr = []
        return "".join(stack)

                   
                
                

            

            
        
                

