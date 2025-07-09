import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.author import Author
from ..models.citation_ids import CitationIds
from ..models.citation_scopes import CitationScopes
from ..models.citation_titles import CitationTitles
from ..types import UNSET, Unset

T = TypeVar("T", bound="Citation")


@attr.s(auto_attribs=True)
class Citation:
    """ """

    main_title: Union[Unset, str] = UNSET
    authors: Union[Unset, List[Author]] = UNSET
    titles: Union[Unset, CitationTitles] = UNSET
    published: Union[Unset, datetime.date] = UNSET
    publisher: Union[Unset, str] = UNSET
    scopes: Union[Unset, CitationScopes] = UNSET
    ids: Union[Unset, CitationIds] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        main_title = self.main_title
        authors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.authors, Unset):
            authors = []
            for authors_item_data in self.authors:
                authors_item = authors_item_data.to_dict()

                authors.append(authors_item)

        titles: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.titles, Unset):
            titles = self.titles.to_dict()

        published: Union[Unset, str] = UNSET
        if not isinstance(self.published, Unset):
            published = self.published.isoformat()

        publisher = self.publisher
        scopes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = self.scopes.to_dict()

        ids: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if main_title is not UNSET:
            field_dict["main_title"] = main_title
        if authors is not UNSET:
            field_dict["authors"] = authors
        if titles is not UNSET:
            field_dict["titles"] = titles
        if published is not UNSET:
            field_dict["published"] = published
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if ids is not UNSET:
            field_dict["ids"] = ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        main_title = d.pop("main_title", UNSET)

        authors = []
        _authors = d.pop("authors", UNSET)
        for authors_item_data in _authors or []:
            authors_item = Author.from_dict(authors_item_data)

            authors.append(authors_item)

        _titles = d.pop("titles", UNSET)
        titles: Union[Unset, CitationTitles]
        if isinstance(_titles, Unset):
            titles = UNSET
        else:
            titles = CitationTitles.from_dict(_titles)

        _published = d.pop("published", UNSET)
        published: Union[Unset, datetime.date]
        if isinstance(_published, Unset):
            published = UNSET
        else:
            published = isoparse(_published).date()

        publisher = d.pop("publisher", UNSET)

        _scopes = d.pop("scopes", UNSET)
        scopes: Union[Unset, CitationScopes]
        if isinstance(_scopes, Unset):
            scopes = UNSET
        else:
            scopes = CitationScopes.from_dict(_scopes)

        _ids = d.pop("ids", UNSET)
        ids: Union[Unset, CitationIds]
        if isinstance(_ids, Unset):
            ids = UNSET
        else:
            ids = CitationIds.from_dict(_ids)

        citation = cls(
            main_title=main_title,
            authors=authors,
            titles=titles,
            published=published,
            publisher=publisher,
            scopes=scopes,
            ids=ids,
        )

        return citation
