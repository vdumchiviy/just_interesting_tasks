"""Given a circular array of size n containing integers from 1 to n. 
Find the last element that would remain in the list after erasing every second element starting from the first element.
Example:
Input: 5
Output: 3
Explanation
Element in circular array are:
1 2 3 4 5
Starting from first element i.e, '1'
delete every second element like this,
1 0 3 4 5
1 0 3 0 5
0 0 3 0 5
0 0 3 0 0
For demonstration purpose erased element
would be treated as '0'.
6
1 2 3 4 5 6
1 0 3 0 5 0

1 2 3 4 5 6 7 8 9 10
1 0 3 4 5 6 7 8 9 10
1 0 3 0 5 0 7 8 9 10
1 0 3 0 5 0 7 0 9 10
1 0 3 0 5 0 7 0 9 0
1 0 0 0 5 0 7 0 9 0
1 0 0 0 5 0 0 0 9 0
0 0 0 0 5 0 0 0 9 0
0 0 0 0 5 0 0 0 0 0

"""

class Solution:
    
    
  def removeAlternate(self,n):
    # Write your Code
    def next_non_0_position(list2, current_position):
        flag = False
        position = current_position
        for x in range(len(list2[current_position+1:])):
            if list2[current_position + x + 1] != "0":
                flag = True
                position = current_position + x + 1
                break
        if not flag:
            for x in range(current_position):
                if list2[x] != "0":
                    flag = True
                    position = x
                    break
        
        return position

        
    l = [x+1 for x in range(n)]
    position = 0
    flag = True
    while flag:
        next_pos = next_non_0_position(l, position)
        if next_pos == position:
            return l[position]
        else:
            l[next_pos] = "0"
            position = next_non_0_position(l, next_pos)
            if position == next_pos:
                return l[next_pos]
 
    
    
sol=Solution()
if sol.removeAlternate(5)==3 and sol.removeAlternate(11)==7 and sol.removeAlternate(6)==5 and sol.removeAlternate(10)==5:
    print("All Test Cases Passed")
else:
    print("Test cases failed")      
