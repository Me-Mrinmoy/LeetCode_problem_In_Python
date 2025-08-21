MOD = 10**9 + 7

class Solution:
    def rectangleArea(self, rectangles):
        # Step 1: Collect events (x, y1, y2, type)
        events = []  # type: 1 = add, -1 = remove
        ys = set()
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, y1, y2, 1))   # rectangle starts
            events.append((x2, y1, y2, -1))  # rectangle ends
            ys.add(y1)
            ys.add(y2)
        
        # Step 2: Coordinate compression
        ys = sorted(ys)
        y_i = {y:i for i, y in enumerate(ys)}  # map original y to index
        
        # Segment tree helpers
        count = [0] * (len(ys) * 4)
        length = [0] * (len(ys) * 4)

        def update(node, l, r, ql, qr, val):
            if ql >= r or qr <= l:  # no overlap
                return
            if ql <= l and r <= qr:  # fully inside
                count[node] += val
            else:  # partial overlap
                mid = (l + r) // 2
                update(node*2, l, mid, ql, qr, val)
                update(node*2+1, mid, r, ql, qr, val)
            
            if count[node] > 0:
                length[node] = ys[r] - ys[l]
            else:
                if l + 1 >= r:
                    length[node] = 0
                else:
                    length[node] = length[node*2] + length[node*2+1]

        # Step 3: Sweep line
        events.sort()
        prev_x = events[0][0]
        area = 0
        for x, y1, y2, typ in events:
            area += (x - prev_x) * length[1]
            area %= MOD
            update(1, 0, len(ys)-1, y_i[y1], y_i[y2], typ)
            prev_x = x

        return area % MOD
