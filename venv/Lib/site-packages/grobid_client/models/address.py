from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@attr.s(auto_attribs=True)
class Address:
    """ """

    addr_line: Union[Unset, str] = UNSET
    post_code: Union[Unset, str] = UNSET
    settlement: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        addr_line = self.addr_line
        post_code = self.post_code
        settlement = self.settlement
        region = self.region
        country = self.country

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if addr_line is not UNSET:
            field_dict["addrLine"] = addr_line
        if post_code is not UNSET:
            field_dict["postCode"] = post_code
        if settlement is not UNSET:
            field_dict["settlement"] = settlement
        if region is not UNSET:
            field_dict["region"] = region
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        addr_line = d.pop("addrLine", UNSET)

        post_code = d.pop("postCode", UNSET)

        settlement = d.pop("settlement", UNSET)

        region = d.pop("region", UNSET)

        country = d.pop("country", UNSET)

        address = cls(
            addr_line=addr_line,
            post_code=post_code,
            settlement=settlement,
            region=region,
            country=country,
        )

        address.additional_properties = d
        return address

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
