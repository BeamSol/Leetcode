class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sortedCost = sorted(costs, key = lambda x: abs(x[0] - x[1]), reverse = True)
        print(sortedCost)
        ans = 0
        n = len(costs) / 2
        count = {0:0, 1:0}
        for i in range(len(costs)):
            if sortedCost[i][0] <= sortedCost[i][1] and count[0] < n:
                ans += sortedCost[i][0]
                count[0] += 1
            elif count[1] < n:
                ans += sortedCost[i][1]
                count[1] += 1
            elif count[1] == n:
                ans +=  sortedCost[i][0]
            else:
                ans += sortedCost[i][1]
        return ans

            