import os
import sys
from datetime import datetime

from fastapi import FastAPI, HTTPException, status

app = FastAPI()


@app.get("/")
def read_root():
    return {"current_time": datetime.now()}


@app.get("/pi_fn/{x}")
def search(x: int, num_chunks: int = 1, chunk_index: int = 0):
    if num_chunks < 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="num_chunks must be > 1"
        )
    if chunk_index < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="chunk_index must be >= 0"
        )
    if not chunk_index < num_chunks:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="chunk_index must be < num_chunks",
        )

    file_name = f"master_file_{num_chunks}_{chunk_index}.txt"
    file_path = os.path.join("data", file_name)

    with open(file_path) as f:
        for line in f:
            split_line = line.split()

            try:
                assert len(split_line) == 3
            except AssertionError:
                continue

            try:
                x_val = int(split_line[0])
                pi_val = int(split_line[1])
            except ValueError:
                continue

            if x_val >= x:
                return {"x": x_val, "pi_x": pi_val}

    return -1
