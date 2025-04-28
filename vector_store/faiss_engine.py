import faiss
import numpy as np
import os
import pickle

class FaissEngine:
    def __init__(self, dim=384, index_path="data/faiss_index.index", use_gpu=False):
        self.dim = dim
        self.index_path = index_path
        self.use_gpu = use_gpu
        self.index = None
        self.id_map = []

    def build_index(self, vectors: np.ndarray, ids: list):
        assert vectors.shape[1] == self.dim, f"Expected dimension {self.dim}, got {vectors.shape[1]}"
        self.index = faiss.IndexFlatIP(self.dim)
        if self.use_gpu:
            res = faiss.StandardGpuResources()
            self.index = faiss.index_cpu_to_gpu(res, 0, self.index)
        self.index.add(vectors)
        self.id_map = ids

    def save_index(self):
        faiss.write_index(faiss.index_gpu_to_cpu(self.index), self.index_path)
        with open(self.index_path + ".meta", "wb") as f:
            pickle.dump(self.id_map, f)

    def load_index(self):
        if not os.path.exists(self.index_path):
            raise FileNotFoundError(f"Index not found at {self.index_path}")
        self.index = faiss.read_index(self.index_path)
        with open(self.index_path + ".meta", "rb") as f:
            self.id_map = pickle.load(f)

    def search(self, query_vector: np.ndarray, top_k: int = 5):
        if self.index is None:
            raise ValueError("Index not loaded or built.")
        scores, indices = self.index.search(query_vector, top_k)
        results = []
        for score_row, idx_row in zip(scores, indices):
            row = []
            for score, idx in zip(score_row, idx_row):
                if idx < len(self.id_map):
                    row.append((self.id_map[idx], float(score)))
            results.append(row)
        return results