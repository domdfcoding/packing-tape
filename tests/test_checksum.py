# stdlib
import os
import tempfile
from typing import Iterator

# 3rd party
import pytest
import requests
from domdf_python_tools.paths import PathPlus

# this package
from shippinglabel.checksum import check_sha256_hash, get_record_entry, get_sha256_hash


@pytest.fixture(scope="session")
def reference_file_a() -> Iterator[PathPlus]:
	with tempfile.TemporaryDirectory() as tmpdir:
		commit_sha = "4f632ed497bffa0cb50d714477de0cf731d34dc6"
		filename = "shippinglabel.svg"
		url = f"https://raw.githubusercontent.com/domdfcoding/shippinglabel/{commit_sha}/{filename}"

		tmpfile = PathPlus(tmpdir) / filename
		tmpfile.write_bytes(requests.get(url).content)

		yield tmpfile


def test_get_sha256_hash(reference_file_a: PathPlus):
	hash = get_sha256_hash(reference_file_a)  # noqa: A001
	assert hash.hexdigest() == "83065efdedd381da9439b85a270ea9629f1ba46d9c7d7b1858bb70e54d5f664c"
	hexdigest = b"\x83\x06^\xfd\xed\xd3\x81\xda\x949\xb8Z'\x0e\xa9b\x9f\x1b\xa4m\x9c}{\x18X\xbbp\xe5M_fL"
	assert hash.digest() == hexdigest


def test_check_sha256_hash(reference_file_a: PathPlus):
	assert check_sha256_hash(
			reference_file_a,
			"83065efdedd381da9439b85a270ea9629f1ba46d9c7d7b1858bb70e54d5f664c",
			)
	assert check_sha256_hash(reference_file_a, get_sha256_hash(reference_file_a))


def test_get_record_entry(reference_file_a: PathPlus):
	entry = get_record_entry(reference_file_a, relative_to=reference_file_a.parent)
	assert entry == f"{os.path.basename(reference_file_a)},sha256=gwZe_e3TgdqUObhaJw6pYp8bpG2cfXsYWLtw5U1fZkw,154911"
