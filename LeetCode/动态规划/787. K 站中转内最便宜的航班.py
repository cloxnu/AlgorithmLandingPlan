import heapq
import threading

class Solution:
    def findCheapestPrice(self, n: int, flights: list, src: int, dst: int, K: int) -> int:
        dic = {}
        for one_flight in flights:
            dic.setdefault(one_flight[0], {})[one_flight[1]] = one_flight[2]
        
        min_pri = {}
        heap = [(0, 0, src)]
        while heap:
            price, k, s = heapq.heappop(heap)
            print(price, k, s)
            if s == dst:
                return price
            if k >= K + 1 or s not in dic:
                continue
            for d, s_d_pri in dic[s].items():
                # heapq.heappush(heap, (s_d_pri + price, k + 1, d))
                pri, min_k = min_pri.get(d, (float('inf'), 0))
                if k + 1 < min_k or s_d_pri + price < pri:
                    min_pri[d] = s_d_pri + price, k + 1
                    heapq.heappush(heap, (s_d_pri + price, k + 1, d))
                    
        return -1
            

