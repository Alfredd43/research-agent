from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.article_citations import ArticleCitations
from ..models.citation import Citation
from ..models.section import Section
from ..types import UNSET, Unset

T = TypeVar("T", bound="Article")


@attr.s(auto_attribs=True)
class Article:
    """ """

    identifier: str
    title: str
    bibliography: Union[Unset, Citation] = UNSET
    sections: Union[Unset, List[Section]] = UNSET
    citations: Union[Unset, ArticleCitations] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        identifier = self.identifier
        title = self.title
        bibliography: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bibliography, Unset):
            bibliography = self.bibliography.to_dict()

        sections: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sections, Unset):
            sections = []
            for sections_item_data in self.sections:
                sections_item = sections_item_data.to_dict()

                sections.append(sections_item)

        citations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.citations, Unset):
            citations = self.citations.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "identifier": identifier,
                "title": title,
            }
        )
        if bibliography is not UNSET:
            field_dict["bibliography"] = bibliography
        if sections is not UNSET:
            field_dict["sections"] = sections
        if citations is not UNSET:
            field_dict["citations"] = citations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identifier = d.pop("identifier")

        title = d.pop("title")

        _bibliography = d.pop("bibliography", UNSET)
        bibliography: Union[Unset, Citation]
        if isinstance(_bibliography, Unset):
            bibliography = UNSET
        else:
            bibliography = Citation.from_dict(_bibliography)

        sections = []
        _sections = d.pop("sections", UNSET)
        for sections_item_data in _sections or []:
            sections_item = Section.from_dict(sections_item_data)

            sections.append(sections_item)

        _citations = d.pop("citations", UNSET)
        citations: Union[Unset, ArticleCitations]
        if isinstance(_citations, Unset):
            citations = UNSET
        else:
            citations = ArticleCitations.from_dict(_citations)

        article = cls(
            identifier=identifier,
            title=title,
            bibliography=bibliography,
            sections=sections,
            citations=citations,
        )

        return article
