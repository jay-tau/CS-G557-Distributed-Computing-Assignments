from fastapi import FastAPI


import os


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

def search(x, num_chunks: int = 1, chunk_index: int = 0) -> int:
    if num_chunks < 1:
        print("num_chunks must be > 1")
        return -2
    if chunk_index < 0:
        print("chunk_index must be >= 0")
        return -3
    if not chunk_index < num_chunks:
        print("chunk_index must be < num_chunks")
        return -4

    file_path = "master_file.txt"
    file_size = os.stat(file_path).st_size

    start_byte = chunk_index * (file_size // num_chunks)
    end_byte = (chunk_index + 1) * (file_size // num_chunks)

    with open(file_path) as f:

        if not x > 1:
            print("Enter a value > 1")
            return -1

        f.seek(start_byte, 0)

        while f.tell() <= end_byte:
            line = f.readline().split()
            try:
                assert len(line) == 3
            except AssertionError:
                # print(f"Error: {line}")
                continue

            try:
                x_val = float(line[0])
                pi_x = int(line[1])
            except ValueError:
                # print(f"Error: {line}")
                continue

            if x == x_val:
                # print(f"pi({x_val}) = {pi_x}")
                return (x_val, pi_x)

        return -1


if __name__ == "__main__":
    # x = 29990000000000
    # num_chunks = 32
    # for i in range(num_chunks):
    #     print(f"Searching chunk {i}...", end="\t")
    #     if search(x, num_chunks, i) != -1:
    #         print(search(x, num_chunks, i))
    #         break
    #     print()
    pass
