class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        n = len(transactions)
        parsed = [t.split(',') for t in transactions]
        invalid = set()
        print(parsed)
        for i in range(n):
            name_i, time_i, amount_i, city_i = parsed[i]
            time_i, amount_i = int(time_i), int(amount_i)
            
            if amount_i > 1000:
                invalid.add(i)
                
            for j in range(n):
                if i != j:
                    name_j, time_j, amount_j, city_j = parsed[j]
                    time_j = int(time_j)
                    if name_i == name_j and city_i != city_j and abs(time_i - time_j) <= 60:
                        invalid.add(i)
                        invalid.add(j)
        
        return [transactions[i] for i in invalid]
