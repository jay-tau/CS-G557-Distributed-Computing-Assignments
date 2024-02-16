import os
import sys

n = int(input("Number of searcher workers: ").strip() or 1)  # Default value is 1

with open(
    os.path.join("docker-compose", f"docker-compose-{n}.yaml"), "w", encoding="utf-8"
) as f:
    sys.stdout = f  # Redirect stdout to file
    print("services:")
    print(
        f"""  load-balancer:
    image: load-balancer
    volumes:
      - ../data:/code/data
    environment:
      - NUM_CHUNKS={n}
    depends_on:"""
    )
    for i in range(n):
        print(f"      - searcher{i}")
    for i in range(n):
        print(
            f"""  searcher{i}:
    image: searcher-worker
    ports:
      - {8000+i}:80
    volumes:
      - ../data:/code/data"""
        )
