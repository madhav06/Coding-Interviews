# python3
# Return a list of strings, 
# where each entry corresponds to a single line. 
# The strings should not have "\n" character in them.

# Input 1:
#     A = "{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}"
# Output 1:
#     { 
#         A:"B",
#         C: 
#         { 
#             D:"E",
#             F: 
#             { 
#                 G:"H",
#                 I:"J"
#             } 
#         } 
#     }


class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        inc = '\t'    
        ans = []
        text = False
        indentation = ''
        tmp = ''
        for ch in A:
            
            if ch == '{' or ch=='[' :
                if text :
                    ans.append(tmp)
                    text = False
                    
                ans.append(indentation+ch)    
                indentation += inc
                tmp = indentation 
            elif  ch== '}' or ch==']':
                if text :
                    ans.append(tmp)
                    text = False
                indentation = indentation[:-1]
               # ans.append(indentation+ch)
                tmp = indentation + ch
                text = True
            elif ch == ',':
                tmp+=','
                ans.append(tmp)
                tmp = indentation
                text = False
    
            elif ch != ' ':
                tmp+=ch
                text = True
        ans.append(tmp)
        return ans