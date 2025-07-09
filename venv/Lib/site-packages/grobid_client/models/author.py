from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.affiliation import Affiliation
from ..models.pers_name import PersName
from ..types import UNSET, Unset

T = TypeVar("T", bound="Author")


@attr.s(auto_attribs=True)
class Author:
    """ """

    pers_name: PersName
    email: Union[Unset, str] = UNSET
    affiliations: Union[Unset, List[Affiliation]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        pers_name = self.pers_name.to_dict()

        email = self.email
        affiliations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.affiliations, Unset):
            affiliations = []
            for affiliations_item_data in self.affiliations:
                affiliations_item = affiliations_item_data.to_dict()

                affiliations.append(affiliations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "persName": pers_name,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if affiliations is not UNSET:
            field_dict["affiliations"] = affiliations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pers_name = PersName.from_dict(d.pop("persName"))

        email = d.pop("email", UNSET)

        affiliations = []
        _affiliations = d.pop("affiliations", UNSET)
        for affiliations_item_data in _affiliations or []:
            affiliations_item = Affiliation.from_dict(affiliations_item_data)

            affiliations.append(affiliations_item)

        author = cls(
            pers_name=pers_name,
            email=email,
            affiliations=affiliations,
        )

        return author
