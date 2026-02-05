"""
N-Dimensional Array

Supports:
- Arbitrary dimensions (1D, 2D, 3D, ...)
- Row-major storage
"""
class NDArray:
    def __init__(self, shape):
        self.shape = shape 
        self.dimensions = len(shape)
        self.size = 1

        for dim in shape:
            self.size *= dim
        self.data = [0] * self.size
        self.strides = self._compute_strides()

    def _compute_strides(self):
        strides = [1] * self.dimensions

        for i in range(self.dimensions - 2, -1, -1):
            strides[i] = strides[i + 1]* self.shape[i + 1]
        return strides
    def _get_flat_index(self, indices):
        if len(indices) != self.dimensions:
            raise IndexError("invalid indice numbr")
        
        flat_index = 0
        for i in range(self.dimensions):
            if indices[i] < 0 or indices[i] >= self.shape[i]:
                raise IndexError("index out of bounds")
            flat_index += indices[i] * self.strides[i]

        return flat_index
    
    def set(self, indices, value):
        idx = self._get_flat_index(indices)
        self.data[idx] = value

    def get(self, indices):
        idx = self._get_flat_index(indices)
        return self.data[idx]
    
    def __str__(self):
        return f"NDArray(shape={self.shape}, data={self.data})"
    
if __name__ == "__main__":
    arr = NDArray((2, 3, 4))  # 3D array
    arr.set((1, 2, 3), 99)
    print(arr.get((1, 2, 3)))
