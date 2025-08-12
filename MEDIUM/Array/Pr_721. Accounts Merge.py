class Solution:
    def accountsMerge(self, accounts):
        parent = {}   # email -> parent email
        owner = {}    # email -> account owner name

        # Step 1: Initialize parent & owner
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                parent[email] = email
                owner[email] = name

        # Union-Find helper functions
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(x, y):
            parent[find(x)] = find(y)

        # Step 2: Union emails in the same account
        for acc in accounts:
            first_email = acc[1]
            for email in acc[2:]:
                union(first_email, email)

        # Step 3: Group emails by root parent
        unions = {}
        for email in parent:
            root = find(email)
            unions.setdefault(root, []).append(email)

        # Step 4: Build result (sort emails inside each group)
        result = []
        for root, emails in unions.items():
            result.append([owner[root]] + sorted(emails))

        return result
