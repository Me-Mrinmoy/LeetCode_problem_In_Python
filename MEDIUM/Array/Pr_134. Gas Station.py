class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_gas, total_cost = 0, 0
        start, tank = 0, 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]

            # If the tank is negative, we can't start from the current start
            if tank < 0:
                start = i + 1  # Move to the next station
                tank = 0       # Reset tank

        # If total gas is less than total cost, return -1
        return start if total_gas >= total_cost else -1

