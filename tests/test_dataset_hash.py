import os
import hashlib
import tempfile
import pytest
from openverifiablellm.dataset_hash import compute_sha256


def test_correct_sha256_output(tmp_path):
    # Create a temporary file
    file = tmp_path / "sample.txt"
    content = "hello wikipedia"
    file.write_text(content)

    # Expected hash using standard hashlib
    expected = hashlib.sha256(content.encode()).hexdigest()

    # Hash using your function
    actual = compute_sha256(str(file))

    # Verify correctness
    assert actual == expected


def test_different_content_different_hash():
    with tempfile.NamedTemporaryFile(delete=False, mode="w") as f1:
        f1.write("Content A")
        path1 = f1.name

    with tempfile.NamedTemporaryFile(delete=False, mode="w") as f2:
        f2.write("Content B")
        path2 = f2.name

    hash1 = compute_sha256(path1)
    hash2 = compute_sha256(path2)

    assert hash1 != hash2

    os.remove(path1)
    os.remove(path2)


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        compute_sha256("non_existent_file.txt")