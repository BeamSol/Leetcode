# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def prime_factors(num):
            factors=set()
            while num%2==0:
                factors.add(2)
                num//=2
            i=3
            while i*i<=num:
                while num%i==0:
                    factors.add(i)
                    num//=i
                i+=2
            if num>2:
                factors.add(num)
            return factors
        primes=set()
        for num in nums:
            primes |= prime_factors(num)
        return len(primes)
        