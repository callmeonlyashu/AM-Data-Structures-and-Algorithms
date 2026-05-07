"""Link: https://leetcode.com/problems/gas-station/"""

from typing import List
# Working solution
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas is less than total cost, no solution exists
        if sum(gas) < sum(cost):
            return -1
        
        total_tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            
            # If we run out of gas at this station
            if total_tank < 0:
                # Every station between the old start and 'i' is invalid
                # So we try starting from the next station
                start_index = i + 1
                total_tank = 0
                
        return start_index

# TLE Solution 

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Get the starting index where cost[i] is less than the gas[i]
        # Get the max diff between cost and gas
        starting_indices = []
        for i in range(0, len(gas)):
            if gas[i] >= cost[i]:
                starting_indices.append(i)
    
        for starting_index in starting_indices:
            curr_gas = 0
            n = len(gas)
            possible = True
            for i in range(n):
                # Use (start + i) % n to get the "circular" index
                current_idx = (starting_index + i) % n

                curr_gas += gas[current_idx]
                curr_gas -= cost[current_idx]

                # Check if enough gas to move to next one. Negative means you are stuck
                if curr_gas < 0:
                    possible = False

            # Check remaining gas is more than what we started with
            if possible:
                return starting_index
        
        return -1



        
