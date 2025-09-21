import random
import time
from multiprocessing import Pool, cpu_count

def generate_chunk(n):
    return [f"{random.randint(1, 4000)}\n" for _ in range(n)]

if __name__ == "__main__":
    start = time.time()
    workers=cpu_count()
    chunk_size = 1_000_000 // workers

    with Pool(workers) as pool:
        results = pool.map(generate_chunk, [chunk_size] * workers)

    with open("file2_multi.txt", "w") as f:
        for chunk in results:
            f.writelines(chunk)

    end = time.time()
    print(f"Time taken: {end - start} seconds")