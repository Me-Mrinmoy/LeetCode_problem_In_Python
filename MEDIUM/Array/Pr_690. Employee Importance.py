class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        # Step 1: Create a map for quick access
        emp_map = {e.id: e for e in employees}

        # Step 2: DFS function
        def dfs(emp_id):
            employee = emp_map[emp_id]
            total = employee.importance
            for sub_id in employee.subordinates:
                total += dfs(sub_id)
            return total

        return dfs(id)

# Example usage
employees = [
    Employee(1, 5, [2, 3]),
    Employee(2, 3, []),
    Employee(3, 3, [])
]
print(Solution().getImportance(employees, 1))  # Output: 11

employees2 = [
    Employee(1, 2, [5]),
    Employee(5, -3, [])
]
print(Solution().getImportance(employees2, 5))  # Output: -3
