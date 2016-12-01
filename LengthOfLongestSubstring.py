

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rl = []
        
        carry = 0 
        l1.reverse()
        l2.reverse()   
        while l1 or l2 or carry:
            
            if l1:
                a = l1.pop()
            else:
                a = 0
            if l2:
                b = l2.pop()
            else:
                b = 0
            
            sum = a + b + carry
            carry = sum / 10
            sum = sum % 10
                
            rl.append(sum)
         
        
        return rl
    
s = Solution()
a = [2,4,6]
b = [5,6,4]
print(s.addTwoNumbers(a, b))
