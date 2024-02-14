import os
import sys

n = int(input("n = "))

with open(os.path.join("docker-compose", f"docker-compose-{n}.yaml"), "w") as f:
    sys.stdout = f
    print("services:")
    for i in range(n):
        print(
            f"""  searcher{i}:
      image: searcher-worker
      ports:
        - {8000+i}:80
      volumes:
        - ../data:/code/data"""
        )
