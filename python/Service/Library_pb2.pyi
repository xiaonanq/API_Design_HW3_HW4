from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

ART: Genre
AVAILABLE: Status
DESCRIPTOR: _descriptor.FileDescriptor
ENGINEERING: Genre
LITERATURE: Genre
SCIENCE: Genre
TAKEN: Status

class Book(_message.Message):
    __slots__ = ["Id", "author", "genre", "title", "year"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    Id: str
    TITLE_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: Genre
    title: str
    year: int
    def __init__(self, Id: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., year: _Optional[int] = ..., genre: _Optional[_Union[Genre, str]] = ...) -> None: ...

class InventoryCreateBookRequest(_message.Message):
    __slots__ = ["author", "genre", "title", "year"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: Genre
    title: str
    year: int
    def __init__(self, title: _Optional[str] = ..., author: _Optional[str] = ..., year: _Optional[int] = ..., genre: _Optional[_Union[Genre, str]] = ...) -> None: ...

class InventoryCreateBookResponse(_message.Message):
    __slots__ = ["Id", "title"]
    ID_FIELD_NUMBER: _ClassVar[int]
    Id: str
    TITLE_FIELD_NUMBER: _ClassVar[int]
    title: str
    def __init__(self, Id: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class InventoryGetBookRequest(_message.Message):
    __slots__ = ["Id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    Id: str
    def __init__(self, Id: _Optional[str] = ...) -> None: ...

class InventoryGetBookResponse(_message.Message):
    __slots__ = ["title"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    title: str
    def __init__(self, title: _Optional[str] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["Id", "book", "status"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    Id: str
    STATUS_FIELD_NUMBER: _ClassVar[int]
    book: Book
    status: Status
    def __init__(self, Id: _Optional[str] = ..., book: _Optional[_Union[Book, _Mapping]] = ..., status: _Optional[_Union[Status, str]] = ...) -> None: ...

class Genre(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
