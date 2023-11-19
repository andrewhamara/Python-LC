class Solution:
    def distributeCandies(self, candies: int, num_people:int) -> List[int]:
        distribution = [0 for i in range(num_people)]
        giving = 1
        while candies > 0:
            for i in range(num_people):
                if candies >= giving:
                    distribution[i] += giving
                    candies -= giving
                    giving += 1
                else:
                    distribution[i] += candies
                    candies = 0; break
        return distribution    
