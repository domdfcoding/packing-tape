# stdlib
import gzip
import tarfile
import tempfile
import zipfile
from urllib.parse import urlparse

# 3rd party
import pytest
from pytest_regressions.data_regression import DataRegressionFixture

# this package
from shippinglabel.pypi import bind_requirements, get_file_from_pypi, get_pypi_releases


@pytest.mark.parametrize(
		"input_s, expected_retval, output",
		[
				('', 0, ''),
				('\n', 0, '\n'),
				('# intentionally empty\n', 0, '# intentionally empty\n'),
				('foo\n# comment at end\n', 1, '# comment at end\nfoo>=.1\n'),
				('foo\nbar\n', 1, 'bar>=0.2.1\nfoo>=.1\n'),
				('bar\nfoo\n', 1, 'bar>=0.2.1\nfoo>=.1\n'),
				('a\nc\nb\n', 1, 'a>=1.0\nb>=1.0.0\nc>=0.1.0\n'),
				('a\nb\nc', 1, 'a>=1.0\nb>=1.0.0\nc>=0.1.0\n'),
				('#comment1\nfoo\n#comment2\nbar\n', 1, '#comment1\n#comment2\nbar>=0.2.1\nfoo>=.1\n'),
				('#comment1\nbar\n#comment2\nfoo\n', 1, '#comment1\n#comment2\nbar>=0.2.1\nfoo>=.1\n'),
				('#comment\n\nfoo\nbar\n', 1, '#comment\nbar>=0.2.1\nfoo>=.1\n'),
				('#comment\n\nbar\nfoo\n', 1, '#comment\nbar>=0.2.1\nfoo>=.1\n'),
				('\nfoo\nbar\n', 1, 'bar>=0.2.1\nfoo>=.1\n'),
				('\nbar\nfoo\n', 1, 'bar>=0.2.1\nfoo>=.1\n'),
				('pyramid-foo==1\npyramid>=2\n', 1, 'pyramid>=2\npyramid-foo==1\n'),
				(
						'a==1\n'
						'c>=1\n'
						'bbbb!=1\n'
						'c-a>=1;python_version>="3.6"\n'
						'e>=2\n'
						'd>2\n'
						'g<2\n'
						'f<=2\n',
						1,
						'a==1\n'
						'bbbb!=1\n'
						'c>=1\n'
						'c-a>=1; python_version >= "3.6"\n'
						'd>2\n'
						'e>=2\n'
						'f<=2\n'
						'g<2\n',
						),
				('ocflib\nDjango\nPyMySQL\n', 1, 'django>=3.1.4\nocflib>=2020.12.5.10.49\npymysql>=0.10.1\n'),
				('bar\npkg-resources==0.0.0\nfoo\n', 1, 'bar>=0.2.1\nfoo>=.1\npkg-resources==0.0.0\n'),
				('foo\npkg-resources==0.0.0\nbar\n', 1, 'bar>=0.2.1\nfoo>=.1\npkg-resources==0.0.0\n'),
				('foo???1.2.3\nbar\n', 1, 'foo???1.2.3\nbar>=0.2.1\n'),
				]
		)
@pytest.mark.flaky(reruns=2, reruns_delay=5)
def test_bind_requirements(input_s, expected_retval, output, tmp_pathplus):
	path = tmp_pathplus / "requirements.txt"
	path.write_text(input_s)

	assert bind_requirements(path) == expected_retval

	assert path.read_text() == output


def uri_validator(x):
	# Based on https://stackoverflow.com/a/38020041
	# By https://stackoverflow.com/users/1668293/alemol and https://stackoverflow.com/users/953553/andilabs
	result = urlparse(x)
	return all([result.scheme, result.netloc, result.path])


def test_get_pypi_releases(data_regression: DataRegressionFixture):
	releases = get_pypi_releases("octocheese")
	assert isinstance(releases, dict)

	release_url_list = releases["0.0.2"]
	assert isinstance(release_url_list, list)

	for url in release_url_list:
		print(url)
		assert isinstance(url, str)
		assert uri_validator(url)

	data_regression.check(release_url_list)


def test_get_file_from_pypi(data_regression: DataRegressionFixture, tmp_pathplus):
	url = (
			"https://files.pythonhosted.org/packages/fa/fb"
			"/d301018af3f22bdbf34b624037e851561914c244a26add8278e4e7273578/octocheese-0.0.2.tar.gz"
			)

	get_file_from_pypi(url, tmp_pathplus)

	the_file = tmp_pathplus / "octocheese-0.0.2.tar.gz"
	assert the_file.is_file()

	# Check it isn't a wheel or Windows-built sdist
	assert not zipfile.is_zipfile(the_file)

	with gzip.open(the_file, 'r'):
		# Check can be opened as gzip file
		assert True

	listing = {
			"octocheese-0.0.2",  # top level directory
			"octocheese-0.0.2/octocheese",  # module
			"octocheese-0.0.2/octocheese/__init__.py",
			"octocheese-0.0.2/octocheese/__main__.py",
			"octocheese-0.0.2/octocheese/action.py",
			"octocheese-0.0.2/octocheese/colours.py",
			"octocheese-0.0.2/octocheese/core.py",
			"octocheese-0.0.2/octocheese.egg-info",  # egg-info
			"octocheese-0.0.2/octocheese.egg-info/dependency_links.txt",
			"octocheese-0.0.2/octocheese.egg-info/entry_points.txt",
			"octocheese-0.0.2/octocheese.egg-info/not-zip-safe",
			"octocheese-0.0.2/octocheese.egg-info/PKG-INFO",
			"octocheese-0.0.2/octocheese.egg-info/requires.txt",
			"octocheese-0.0.2/octocheese.egg-info/SOURCES.txt",
			"octocheese-0.0.2/octocheese.egg-info/top_level.txt",
			"octocheese-0.0.2/__pkginfo__.py",  # metadata
			"octocheese-0.0.2/LICENSE",
			"octocheese-0.0.2/MANIFEST.in",
			"octocheese-0.0.2/PKG-INFO",
			"octocheese-0.0.2/README.rst",
			"octocheese-0.0.2/requirements.txt",
			"octocheese-0.0.2/setup.cfg",
			"octocheese-0.0.2/setup.py",
			}

	with tarfile.open(the_file, "r:gz") as tar:
		assert {f.name for f in tar.getmembers()} == listing
		data_regression.check(sorted({f.name for f in tar.getmembers()}))
