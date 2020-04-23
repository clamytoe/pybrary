"""
test_pybrary.py

Tests for pybrary.
"""
from types import GeneratorType

import pytest

from pybrary import Ebook, Library, Path, __version__, main, store


def test_version():
    assert __version__ == "0.1.1"


@pytest.fixture(scope="class")
def collection():
    return Library(store)


class TestStore:
    def test_store(self):
        assert store.is_dir


class TestLibrary:
    def test_parser_dir(self, collection):
        assert collection.directory.is_dir

    def test_parser_gen(self, collection):
        assert isinstance(collection.books, GeneratorType)


class TestBook:
    def test_empty(self):
        with pytest.raises(TypeError):
            Ebook()

    def test_ebook(self, collection):
        book = next(collection.books)
        assert book.path == Path(
            "/home/mohh/Downloads/eBooks/English/all/"
            "A_Beginners_Guide_to_Python_3_Programming-10-1007-978-3-030-20290-3.epub"
        )
        assert book.filename == (
            "A_Beginners_Guide_to_Python_3_Programming-10-1007-978-3-030-20290-3.epub"
        )
        assert book.title == "A Beginners Guide to Python 3 Programming"
        assert book.isbn == "10-1007-978-3-030-20290-3"
        assert book.extension == ".epub"

    def test_all_books(self, collection):
        books = list(collection.books)
        assert len(books) == 735

    def test_report(self, collection, capfd):
        collection.report()
        output = capfd.readouterr()[0].splitlines()
        assert len(output) == 737

    def test_search_python(self, collection, capfd):
        collection.report("python")
        output = capfd.readouterr()[0].splitlines()
        assert len(output) == 18

    def test_report_ext_epub(self, collection, capfd):
        collection.report(ext="epub")
        output = capfd.readouterr()[0].splitlines()
        assert len(output) == 330

    def test_report_ext_pdf(self, collection, capfd):
        collection.report(ext="pdf")
        output = capfd.readouterr()[0].splitlines()
        assert len(output) == 409

    def test_report_ext_pdf_search_machine(self, collection, capfd):
        collection.report("machine", "pdf")
        output = capfd.readouterr()[0].splitlines()
        idx = output[2].find(" ") + 1
        assert len(output) == 5
        assert output[2][idx:] == "An Introduction to Machine Learning.pdf"


class TestApp:
    def test_main(self, capfd):
        expected = """Library Report [pdf]                                     search: computer vision
--------------------------------------------------------------------------------
10-1007-978-1-84882-935-0 Computer Vision.pdf
"""
        main()
        output = capfd.readouterr()[0]
        assert output == expected
