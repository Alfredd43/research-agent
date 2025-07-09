from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ref import Ref
from ..types import UNSET, Unset

T = TypeVar("T", bound="TextWithRefs")


@attr.s(auto_attribs=True)
class TextWithRefs:
    """ """

    text: str
    refs: Union[Unset, List[Ref]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        refs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.refs, Unset):
            refs = []
            for refs_item_data in self.refs:
                refs_item = refs_item_data.to_dict()

                refs.append(refs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "text": text,
            }
        )
        if refs is not UNSET:
            field_dict["refs"] = refs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text")

        refs = []
        _refs = d.pop("refs", UNSET)
        for refs_item_data in _refs or []:
            refs_item = Ref.from_dict(refs_item_data)

            refs.append(refs_item)

        text_with_refs = cls(
            text=text,
            refs=refs,
        )

        return text_with_refs
