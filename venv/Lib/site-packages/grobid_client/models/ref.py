from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Ref")


@attr.s(auto_attribs=True)
class Ref:
    """ """

    type: Union[Unset, str] = UNSET
    target: Union[Unset, str] = UNSET
    start: Union[Unset, int] = UNSET
    end: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        target = self.target
        start = self.start
        end = self.end

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if target is not UNSET:
            field_dict["target"] = target
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        target = d.pop("target", UNSET)

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        ref = cls(
            type=type,
            target=target,
            start=start,
            end=end,
        )

        return ref
