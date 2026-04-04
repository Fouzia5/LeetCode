import numpy as np
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText: return ""
        n = len(encodedText)
        cols = n // rows
        r_idx = np.arange(rows).reshape(-1, 1)
        k_idx = np.arange(cols).reshape(1, -1)
        indices = r_idx * (cols + 1) + k_idx
        mask = (k_idx + r_idx < cols)
        flat_indices = indices.T[mask.T]
        arr = np.frombuffer(encodedText.encode(), dtype='S1')
        return arr[flat_indices].tobytes().decode().rstrip()     