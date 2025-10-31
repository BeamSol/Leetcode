    def countGoodNumbers(self, n: int) -> int:
        def power(b, exp):
            if exp == 0:
                return 1
            else:
                rec = power(b, exp // 2)
                return rec * rec * (b if exp % 2 else 1) % 1000000007

        return power(20, n // 2) * (5 if n % 2 else 1) % 1000000007