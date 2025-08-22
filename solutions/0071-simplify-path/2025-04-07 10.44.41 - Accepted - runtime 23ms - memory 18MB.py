import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []

        while path:
            if re.match(p := r"^/+", path):
                s = re.findall(p, path)[0]
                path = path[len(s):]
            elif re.match(p := r"^\./", path):
                s = re.findall(p, path)[0]
                path = path[len(s):]
            elif re.match(p := r"^\.$", path):
                s = re.findall(p, path)[0]
                path = path[len(s):]
                break
            elif re.match(p := r"^\.\./", path):
                s = re.findall(p, path)[0]
                path = path[len(s):]
                if stack: stack.pop()
            elif re.match(p := r"^\.\.$", path):
                s = re.findall(p, path)[0]
                path = path[len(s):]
                if stack: stack.pop()
                break
            elif re.match(p := r"^(.*?)/", path):
                s = re.findall(p, path)[0]
                path = path[len(s)+1:]
                stack.append(s)
            elif re.match(p := r"^(.*)", path):
                s = re.findall(p, path)[0]
                path = path[len(s):]
                stack.append(s)
                break
        return "/" + "/".join(stack)