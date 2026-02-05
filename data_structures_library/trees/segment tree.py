class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4* self.n)
        self.build(arr, 0, 0, self.n -1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid )
            self.build(arr, 2 * node + 2, mid+1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    
    def query(self, l, r, node, start, end):
        if r < start or l > end:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return self.query(l, r, 2 * node + 1, start, mid) + \
                self.query(l, r, 2 * node + 2, mid + 1, end)
    
if __name__=="__main__":
    arr = [2,3,4,3,2,3,45,6,4]
    st = SegmentTree(arr)
    print("Sum(1,3):", st.query(1, 3, 0, 0, len(arr) - 1))

