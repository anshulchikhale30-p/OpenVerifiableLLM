from openverifiablellm.dataset_hash import compute_sha256


if __name__ == "__main__":
    dataset_path = "examples/sample_wiki.txt"

    print("Dataset Hash:")
    print(compute_sha256(dataset_path))
