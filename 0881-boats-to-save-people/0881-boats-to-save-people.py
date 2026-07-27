class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        boats =0
        res =0
        while left<=right:
            curr = people[left] + people[right]
            if curr <= limit :
                boats+=1 
                left +=1
                right -=1  
            else:
                right-=1
                boats+=1         
        return boats        
