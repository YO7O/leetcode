class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        left = True
        count, i = 0, 0
        while i < n:
            if left:
                if target[i] == 'L':
                    count -= 1
                if start[i] == 'L':
                    count += 1
                if count > 0:
                    return False

                if target[i] == 'R' or start[i] == 'R':
                    if count != 0:
                        return False
                    left = False
                    continue
            
            else:
                if start[i] == 'R':
                    count += 1
                if target[i] == 'R':
                    count -= 1
                if count < 0:
                    return False
                
                if target[i] == 'L' or start[i] == 'L':
                    if count != 0:
                        return False
                    left = True
                    continue
            
            i += 1
        
        return count == 0