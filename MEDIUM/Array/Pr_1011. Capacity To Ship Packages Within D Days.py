def shipWithinDays(self, weights, D):
		low, high = max(weights), sum(weights)
		while low < high:
			# guess the capacity of ship
			mid = (low+high)//2

			cur_cap = 0 # loaded capacity of current ship
			num_ship = 1 # number of ship needed

			#----simulating loading the weight to ship one by one----#
			for w in weights:
				cur_cap += w
				if cur_cap > mid: # current ship meets its capacity
					cur_cap = w
					num_ship += 1
			#---------------simulation ends--------------------------#

			# we need too many ships, so we need to increase capacity to reduce num of ships needed
			if num_ship > D:
				low = mid+1
			# we are able to ship with good num of ships, but we still need to find the optimal max capacity
			else:
				high = mid

		return low
