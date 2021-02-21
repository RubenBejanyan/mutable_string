from __future__ import annotations
from collections.abc import MutableSequence, Iterable
from typing import Union


class MutableString(MutableSequence):
    def __init__(self, string):
        self.data = list(str(string))

    def __getitem__(self, key: Union[int, slice]) -> MutableString:
        if not isinstance(key, (int, slice)):
            raise TypeError(f'MutableString indices must be integers or slice, not {type(key).__name__}')
        if isinstance(key, int):
            if not -len(self) <= key < len(self):
                raise IndexError(f'MutableString index ({key}) out of range')
        return MutableString(str(self)[key])

    def __setitem__(self, key: Union[int, slice], value: Union[str, MutableString]) -> None:
        if not isinstance(key, (int, slice)):
            raise TypeError(f'MutableString indices must be integers or slice, not {type(key).__name__}')
        if isinstance(key, int):
            if not -len(self) <= key < len(self):
                raise IndexError(f'MutableString index ({key}) out of range')
        if not isinstance(value, (str, type(self))):
            raise TypeError(f'Can change to string or MutableString, not to {type(value).__name__}')
        self.data[key] = value

    def __delitem__(self, key: Union[int, slice]) -> None:
        if not isinstance(key, (int, slice)):
            raise TypeError(f'MutableString indices must be integers or slice, not {type(key).__name__}')
        if isinstance(key, int):
            if not -len(self) <= key < len(self):
                raise IndexError(f'MutableString index ({key}) out of range')
        del self.data[key]

    def __len__(self) -> int:
        return len(self.data)

    def insert(self, index: int, value: Union[str, MutableString]) -> None:
        if not isinstance(index, int):
            raise TypeError(f'Index must be int, not {type(index).__name__}')
        if not isinstance(value, (str, type(self))):
            raise TypeError(f'Can insert string or MutableString, not {type(value).__name__}')
        self.data.insert(index, value)

    def __str__(self) -> str:
        return ''.join(self.data)

    def __iter__(self) -> str:
        for _item in self.data:
            yield _item

    def __repr__(self) -> str:
        return str(self)

    def __add__(self, string: Union[str, MutableString]) -> MutableString:
        if not isinstance(string, (str, type(self))):
            type_string = type(string).__name__
            raise TypeError(f'MutableString can concatenate only other MutableString or string (not "{type_string}")')
        return MutableString(f'{self}{string}')

    def title(self) -> MutableString:
        self.data = list(str(self).title())
        return self

    def capitalize(self) -> MutableString:
        self.data = list(str(self).capitalize())
        return self

    def center(self, width: int, fill: str = ' ') -> MutableString:
        if not isinstance(width, int):
            raise TypeError(f'width must be int, not {type(width).__name__}')
        if not isinstance(fill, (str, type(self))):
            raise TypeError(f'fill must be string or MutableString, not {type(fill).__name__}')
        fill = str(fill)
        self.data = list(str(self).center(width, fill))
        return self

    def upper(self) -> MutableString:
        self.data = list(str(self).upper())
        return self

    def lower(self) -> MutableString:
        self.data = list(str(self).lower())
        return self

    # change original task, for method work like for simple string
    def startswith(self, string: Union[str, MutableString, tuple], start: int = None, end: int = None) -> bool:
        str_tp_err = f'startswith first arg must be str(MutableString) or tuple of str, not {type(string).__name__}'
        if not isinstance(string, (str, type(self), tuple)):
            raise TypeError(str_tp_err)
        if isinstance(string, tuple):
            for _str in string:
                if not isinstance(_str, (str, type(self))):
                    raise TypeError(str_tp_err)
            string = tuple(map(str, string))  # in case if string is tuple of MutableString
        else:
            string = str(string)
        if start and not isinstance(start, int):
            raise TypeError(f'startswith second arg must be int, not {type(start).__name__}')
        if end and not isinstance(start, int):
            raise TypeError(f'startswith third arg must be int, not {type(end).__name__}')
        return str(self).startswith(string, start, end)

    # change original task, for method work like for simple string
    def endswith(self, string: Union[str, MutableString, tuple], start: int = None, end: int = None) -> bool:
        str_tp_err = f'endswith first arg must be str(MutableString) or tuple of str, not {type(string).__name__}'
        if not isinstance(string, (str, type(self), tuple)):
            raise TypeError(str_tp_err)
        if isinstance(string, tuple):
            for _str in string:
                if not isinstance(_str, (str, type(self))):
                    raise TypeError(str_tp_err)
            string = tuple(map(str, string))  # in case if string is tuple of MutableString
        else:
            string = str(string)
        if start and not isinstance(start, int):
            raise TypeError(f'endswith second arg must be int, not {type(start).__name__}')
        if end and not isinstance(start, int):
            raise TypeError(f'endswith third arg must be int, not {type(end).__name__}')
        return str(self).endswith(string, start, end)

    def find(self, string: Union[str, MutableString], start: int = None, end: int = None) -> int:
        if not isinstance(string, (str, type(self))):
            raise TypeError(f'find first arg must be str(MutableString), not {type(string).__name__}')
        if start and not isinstance(start, int):
            raise TypeError(f'find second arg must be int, not {type(start).__name__}')
        if end and not isinstance(start, int):
            raise TypeError(f'find third arg must be int, not {type(end).__name__}')
        if start is None:
            start = 0
        if end is None:
            end = len(self)
        string = str(string)
        return str(self).find(string, start, end)

    def rfind(self, string: Union[str, MutableString], start: int = None, end: int = None) -> int:
        if not isinstance(string, (str, type(self))):
            raise TypeError(f'rfind first arg must be str(MutableString), not {type(string).__name__}')
        if start and not isinstance(start, int):
            raise TypeError(f'rfind second arg must be int, not {type(start).__name__}')
        if end and not isinstance(start, int):
            raise TypeError(f'rfind third arg must be int, not {type(end).__name__}')
        if start is None:
            start = 0
        if end is None:
            end = len(self)
        string = str(string)
        return str(self).rfind(string, start, end)

    def index(self, string: Union[str, MutableString], start: int = None, end: int = None) -> int:
        if not isinstance(string, (str, type(self))):
            raise TypeError(f'index first arg must be str(MutableString), not {type(string).__name__}')
        if start and not isinstance(start, int):
            raise TypeError(f'index second arg must be int, not {type(start).__name__}')
        if end and not isinstance(start, int):
            raise TypeError(f'index third arg must be int, not {type(end).__name__}')
        if start is None:
            start = 0
        if end is None:
            end = len(self)
        string = str(string)
        return str(self).index(string, start, end)

    def rindex(self, string: Union[str, MutableString], start: int = None, end: int = None) -> int:
        if not isinstance(string, (str, type(self))):
            raise TypeError(f'rindex first arg must be str(MutableString), not {type(string).__name__}')
        if start and not isinstance(start, int):
            raise TypeError(f'rindex second arg must be int, not {type(start).__name__}')
        if end and not isinstance(start, int):
            raise TypeError(f'rindex third arg must be int, not {type(end).__name__}')
        if start is None:
            start = 0
        if end is None:
            end = len(self)
        string = str(string)
        return str(self).rindex(string, start, end)

    def split(self, symbol: Union[str, MutableString] = None, max_split: int = -1) -> list[MutableString]:
        if symbol and not isinstance(symbol, (str, type(self))):
            raise TypeError(f'split first arg must be str(MutableString), not {type(symbol).__name__}')
        if not isinstance(max_split, int):
            raise TypeError(f'split second arg must be int, not {type(max_split).__name__}')
        if symbol:
            symbol = str(symbol)
        return [MutableString(split_elem) for split_elem in str(self).split(symbol, max_split)]

    def rsplit(self, symbol: Union[str, MutableString] = None, max_split: int = -1) -> list[str]:
        if symbol and not isinstance(symbol, (str, type(self))):
            raise TypeError(f'rsplit first arg must be str(MutableString), not {type(symbol).__name__}')
        if max_split and not isinstance(max_split, int):
            raise TypeError(f'rsplit second arg must be int, not {type(max_split).__name__}')
        if symbol:
            symbol = str(symbol)
        return str(self).rsplit(symbol, max_split)

    def replace(self, old: Union[str, MutableString], new: Union[str, MutableString], count: int = -1) -> MutableString:
        if not isinstance(old, (str, type(self))):
            raise TypeError(f'replace first arg must be str(MutableString), not {type(old).__name__}')
        if not isinstance(new, (str, type(self))):
            raise TypeError(f'replace second arg must be str(MutableString), not {type(new).__name__}')
        if not isinstance(count, int):
            raise TypeError(f'replace third arg must be int, not {type(count).__name__}')
        old, new = str(old), str(new)
        self.data = list(str(self).replace(old, new, count))
        return self

    def isdigit(self) -> bool:
        return str(self).isdigit()

    def isalpha(self) -> bool:
        return str(self).isalpha()

    def isalnum(self) -> bool:
        return str(self).isalpha()

    def islower(self) -> bool:
        return str(self).islower()

    def isupper(self) -> bool:
        return str(self).isupper()

    def isspace(self) -> bool:
        return str(self).isspace()

    def istitle(self) -> bool:
        return str(self).istitle()

    def join(self, array: Iterable[Union[str, MutableString]]) -> MutableString:
        if not isinstance(array, Iterable):
            raise TypeError('join argument must be iterable')
        for _item in array:
            if not isinstance(_item, (str, type(self))):
                raise TypeError(f'join argument must be str(MutableString), not {type(_item).__name__}')
        array = tuple(map(str, array))
        self.data = list(str(self).join(array))
        return self

    def format(self, *args: any, **kwargs: any) -> MutableString:
        self.data = list(str(self).format(*args, **kwargs))
        return self

    def count(self, string: Union[str, MutableString], start: int = None, end: int = None) -> int:
        if not isinstance(string, (str, type(self))):
            raise TypeError(f'count first arg must be str(MutableString), not {type(string).__name__}')
        if start and not isinstance(start, int):
            raise TypeError(f'count second arg must be int, not {type(start).__name__}')
        if end and not isinstance(start, int):
            raise TypeError(f'count third arg must be int, not {type(end).__name__}')
        if start is None:
            start = 0
        if end is None:
            end = len(self)
        string = str(string)
        return str(self).count(string, start, end)

    def lstrip(self, symbol: Union[str, MutableString] = None) -> MutableString:
        if symbol and not isinstance(symbol, (str, type(self))):
            raise TypeError(f'lstrip arg must be str(MutableString), not {type(symbol).__name__}')
        if symbol:
            symbol = str(symbol)
        self.data = list(str(self).lstrip(symbol))
        return self

    def rstrip(self, symbol: Union[str, MutableString] = None) -> MutableString:
        if symbol and not isinstance(symbol, (str, type(self))):
            raise TypeError(f'rstrip arg must be str(MutableString), not {type(symbol).__name__}')
        if symbol:
            symbol = str(symbol)
        self.data = list(str(self).rstrip(symbol))
        return self

    def strip(self, symbol: Union[str, MutableString] = None) -> MutableString:
        if symbol and not isinstance(symbol, (str, type(self))):
            raise TypeError(f'strip arg must be str(MutableString), not {type(symbol).__name__}')
        if symbol:
            symbol = str(symbol)
        self.data = list(str(self).strip(symbol))
        return self

    @classmethod
    def ord(cls, symbol: Union[str, MutableString]) -> int:
        if not isinstance(symbol, (str, MutableString)):
            raise TypeError(f'ord argument must be str(MutableString), not {type(symbol).__name__}')
        if len(symbol) != 1:
            raise TypeError('ord argument must be one character')
        return ord(str(symbol))

    @staticmethod
    def chr(number: int) -> MutableString:
        if not isinstance(number, int):
            raise TypeError(f'chr argument must be int, not {type(number).__name__}')
        return MutableString(chr(number))


if __name__ == '__main__':
