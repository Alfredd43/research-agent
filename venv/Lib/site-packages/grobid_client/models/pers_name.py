from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersName")


@attr.s(auto_attribs=True)
class PersName:
    """ """

    firstname: Union[Unset, str] = UNSET
    middlename: Union[Unset, str] = UNSET
    surname: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    suffix: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        firstname = self.firstname
        middlename = self.middlename
        surname = self.surname
        title = self.title
        suffix = self.suffix

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if middlename is not UNSET:
            field_dict["middlename"] = middlename
        if surname is not UNSET:
            field_dict["surname"] = surname
        if title is not UNSET:
            field_dict["title"] = title
        if suffix is not UNSET:
            field_dict["suffix"] = suffix

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        firstname = d.pop("firstname", UNSET)

        middlename = d.pop("middlename", UNSET)

        surname = d.pop("surname", UNSET)

        title = d.pop("title", UNSET)

        suffix = d.pop("suffix", UNSET)

        pers_name = cls(
            firstname=firstname,
            middlename=middlename,
            surname=surname,
            title=title,
            suffix=suffix,
        )

        return pers_name
