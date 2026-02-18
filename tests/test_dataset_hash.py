from openverifiablellm.dataset_hash import compute_sha256


def test_hash_is_deterministic(tmp_path):
    file = tmp_path / "data.txt"
    file.write_text("hello wikipedia")

    h1 = compute_sha256(str(file))
    h2 = compute_sha256(str(file))

    assert h1 == h2
