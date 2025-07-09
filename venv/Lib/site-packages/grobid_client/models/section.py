from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.text_with_refs import TextWithRefs
from ..types import UNSET, Unset

T = TypeVar("T", bound="Section")


@attr.s(auto_attribs=True)
class Section:
    """
    Attributes:
        name (Union[Unset, str]):
        num (Union[Unset, str]):
        paragraphs (Union[Unset, List[Union[List[TextWithRefs], TextWithRefs]]]):
    """

    name: Union[Unset, str] = UNSET
    num: Union[Unset, str] = UNSET
    paragraphs: Union[Unset, List[Union[List[TextWithRefs], TextWithRefs]]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        num = self.num
        paragraphs: Union[Unset, List[Union[Dict[str, Any], List[Dict[str, Any]]]]] = UNSET
        if not isinstance(self.paragraphs, Unset):
            paragraphs = []
            for paragraphs_item_data in self.paragraphs:
                if isinstance(paragraphs_item_data, list):
                    paragraphs_item = []
                    for paragraphs_item_type_0_item_data in paragraphs_item_data:
                        paragraphs_item_type_0_item = paragraphs_item_type_0_item_data.to_dict()

                        paragraphs_item.append(paragraphs_item_type_0_item)

                else:
                    paragraphs_item = paragraphs_item_data.to_dict()

                paragraphs.append(paragraphs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if num is not UNSET:
            field_dict["num"] = num
        if paragraphs is not UNSET:
            field_dict["paragraphs"] = paragraphs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        num = d.pop("num", UNSET)

        paragraphs = []
        _paragraphs = d.pop("paragraphs", UNSET)
        for paragraphs_item_data in _paragraphs or []:

            def _parse_paragraphs_item(data: object) -> Union[List[TextWithRefs], TextWithRefs]:
                try:
                    if not isinstance(data, list):
                        raise TypeError()
                    paragraphs_item_type_0 = UNSET
                    _paragraphs_item_type_0 = data
                    for paragraphs_item_type_0_item_data in _paragraphs_item_type_0:
                        paragraphs_item_type_0_item = TextWithRefs.from_dict(paragraphs_item_type_0_item_data)

                        paragraphs_item_type_0.append(paragraphs_item_type_0_item)

                    return paragraphs_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                paragraphs_item_type_1 = TextWithRefs.from_dict(data)

                return paragraphs_item_type_1

            paragraphs_item = _parse_paragraphs_item(paragraphs_item_data)

            paragraphs.append(paragraphs_item)

        section = cls(
            name=name,
            num=num,
            paragraphs=paragraphs,
        )

        return section
