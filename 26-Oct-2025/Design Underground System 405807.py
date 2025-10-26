# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.dic = defaultdict(list)
        self.checkin = defaultdict(int)
        self.checkout = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        name, time = self.checkin[id]
        self.dic[(name, stationName)].append(t-time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        temp = self.dic[(startStation, endStation)] 
        return sum(temp)/len(temp)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)