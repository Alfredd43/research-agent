from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.address import Address
from ..types import UNSET, Unset

T = TypeVar("T", bound="Affiliation")


@attr.s(auto_attribs=True)
class Affiliation:
    """ """

    institution: Union[Unset, str] = UNSET
    department: Union[Unset, str] = UNSET
    laboratory: Union[Unset, str] = UNSET
    acronym: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    address: Union[Unset, List[Address]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        institution = self.institution
        department = self.department
        laboratory = self.laboratory
        acronym = self.acronym
        url = self.url
        address: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.address, Unset):
            address = []
            for address_item_data in self.address:
                address_item = address_item_data.to_dict()

                address.append(address_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if institution is not UNSET:
            field_dict["institution"] = institution
        if department is not UNSET:
            field_dict["department"] = department
        if laboratory is not UNSET:
            field_dict["laboratory"] = laboratory
        if acronym is not UNSET:
            field_dict["acronym"] = acronym
        if url is not UNSET:
            field_dict["url"] = url
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        institution = d.pop("institution", UNSET)

        department = d.pop("department", UNSET)

        laboratory = d.pop("laboratory", UNSET)

        acronym = d.pop("acronym", UNSET)

        url = d.pop("url", UNSET)

        address = []
        _address = d.pop("address", UNSET)
        for address_item_data in _address or []:
            address_item = Address.from_dict(address_item_data)

            address.append(address_item)

        affiliation = cls(
            institution=institution,
            department=department,
            laboratory=laboratory,
            acronym=acronym,
            url=url,
            address=address,
        )

        return affiliation
