#!/usr/bin/env python3
"""
app.py

eBook Library Parser
"""
from dataclasses import dataclass
from pathlib import Path
from sys import argv
from typing import Tuple

store = Path("/home/mohh/Downloads/eBooks/English/all")


@dataclass(order=True)
class Ebook:
    path: Path

    def __post_init__(self):
        self.loc = self.path.parent
        self.filename = self.path.name
        divider = self.filename.find("-")
        self.title = self.path.stem[:divider].replace("_", " ")
        self.isbn = self.path.stem[divider + 1 :]
        self.extension = self.path.suffix

    def __str__(self):
        return f"{self.isbn:>25} {self.title}{self.extension}"


@dataclass
class Library:
    directory: Path
    book_types: Tuple[str] = ("epub", "pdf")

    @property
    def books(self):
        yield from sorted(Ebook(book) for book in self.directory.iterdir())

    def report(self, search=None, ext=None):
        header = f"Library Report {'[' + ext + ']' if ext else ''}"
        header += f"{'search: ' + search if search else '':>{80 - len(header)}}\n"
        header += f"{'-' * 80}"
        print(header)

        for book in self.books:
            if ext is None:
                if search:
                    if self._search(search, book.filename):
                        print(book)
                else:
                    print(book)
            elif ext in self.book_types:
                if f".{ext}" == book.extension:
                    if search:
                        if self._search(search, book.filename):
                            print(book)
                    else:
                        print(book)

    @staticmethod
    def _search(term: str, title: str) -> bool:
        return term.lower() in title.lower().replace("_", " ")


def main(loc: Path = store):
    library = Library(loc)
    args = argv
    if "pytest" in args[0]:
        args = ["test", "computer vision", "pdf"]

    if len(args) > 1:
        library.report(*args[1:])
    else:
        library.report()


if __name__ == "__main__":
    main()
