import os

from tqdm import tqdm


def split_file(filename, n):
    """
    Splits a text file into n separate text files, based on the number of lines.

    Args:
      filename: The name of the text file to split.
      n: The number of files to split the text file into.

    Raises:
      ValueError: If the number of lines in the file is not divisible by n.
    """

    # Read the total number of lines in the file
    with open(filename, "r") as f:
        total_lines = sum(1 for _ in f)

    # Check if the number of lines is divisible by n
    if total_lines % n != 0:
        raise ValueError("Number of lines is not divisible by n")

    # Calculate the number of lines per file
    lines_per_file = total_lines // n

    # Open the original file and create output files
    with open(filename, "r") as f:
        for i, line in tqdm(enumerate(f)):
            # Calculate the index of the output file
            file_index = i // lines_per_file

            # Open the output file (create if it doesn't exist)
            with open(f"{filename[:-4]}_{n}_{file_index}.txt", "a") as output_file:
                output_file.write(line)


if __name__ == "__main__":
    # Get the filename and number of files from the user
    # filename = input("Enter the filename: ")
    filename = os.path.join("data", "master_file.txt")
    n_chunks = int(input("Enter the number of files to split into: "))

    # Split the file
    # for n_chunks in (2, 4, 8, 16, 32):
    print(f"{n_chunks}:", end="\n")
    split_file(filename, n_chunks)

    # print(f"File '{filename}' successfully split into {n} files.")
    print("DONE")
