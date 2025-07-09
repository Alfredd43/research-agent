from io import BytesIO
from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, File, Unset

T = TypeVar("T", bound="ProcessForm")


@attr.s(auto_attribs=True)
class ProcessForm:
    """ """

    input_: File
    generate_ids: Union[Unset, str] = UNSET
    consolidate_header: Union[Unset, str] = UNSET
    consolidate_citations: Union[Unset, str] = UNSET
    include_raw_citations: Union[Unset, str] = UNSET
    include_raw_affiliations: Union[Unset, str] = UNSET
    tei_coordinates: Union[Unset, str] = UNSET
    segment_sentences: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        input_ = self.input_.to_tuple()

        generate_ids = self.generate_ids
        consolidate_header = self.consolidate_header
        consolidate_citations = self.consolidate_citations
        include_raw_citations = self.include_raw_citations
        include_raw_affiliations = self.include_raw_affiliations
        tei_coordinates = self.tei_coordinates
        segment_sentences = self.segment_sentences

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "input": input_,
            }
        )
        if generate_ids is not UNSET:
            field_dict["generateIDs"] = generate_ids
        if consolidate_header is not UNSET:
            field_dict["consolidateHeader"] = consolidate_header
        if consolidate_citations is not UNSET:
            field_dict["consolidateCitations"] = consolidate_citations
        if include_raw_citations is not UNSET:
            field_dict["includeRawCitations"] = include_raw_citations
        if include_raw_affiliations is not UNSET:
            field_dict["includeRawAffiliations"] = include_raw_affiliations
        if tei_coordinates is not UNSET:
            field_dict["teiCoordinates"] = tei_coordinates
        if segment_sentences is not UNSET:
            field_dict["segmentSentences"] = segment_sentences

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        input_ = self.input_.to_tuple()

        generate_ids = (
            self.generate_ids if self.generate_ids is UNSET else (None, str(self.generate_ids).encode(), "text/plain")
        )
        consolidate_header = (
            self.consolidate_header
            if self.consolidate_header is UNSET
            else (None, str(self.consolidate_header).encode(), "text/plain")
        )
        consolidate_citations = (
            self.consolidate_citations
            if self.consolidate_citations is UNSET
            else (None, str(self.consolidate_citations).encode(), "text/plain")
        )
        include_raw_citations = (
            self.include_raw_citations
            if self.include_raw_citations is UNSET
            else (None, str(self.include_raw_citations).encode(), "text/plain")
        )
        include_raw_affiliations = (
            self.include_raw_affiliations
            if self.include_raw_affiliations is UNSET
            else (None, str(self.include_raw_affiliations).encode(), "text/plain")
        )
        tei_coordinates = (
            self.tei_coordinates
            if self.tei_coordinates is UNSET
            else (None, str(self.tei_coordinates).encode(), "text/plain")
        )
        segment_sentences = (
            self.segment_sentences
            if self.segment_sentences is UNSET
            else (None, str(self.segment_sentences).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "input": input_,
            }
        )
        if generate_ids is not UNSET:
            field_dict["generateIDs"] = generate_ids
        if consolidate_header is not UNSET:
            field_dict["consolidateHeader"] = consolidate_header
        if consolidate_citations is not UNSET:
            field_dict["consolidateCitations"] = consolidate_citations
        if include_raw_citations is not UNSET:
            field_dict["includeRawCitations"] = include_raw_citations
        if include_raw_affiliations is not UNSET:
            field_dict["includeRawAffiliations"] = include_raw_affiliations
        if tei_coordinates is not UNSET:
            field_dict["teiCoordinates"] = tei_coordinates
        if segment_sentences is not UNSET:
            field_dict["segmentSentences"] = segment_sentences

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        input_ = File(payload=BytesIO(d.pop("input")))

        generate_ids = d.pop("generateIDs", UNSET)

        consolidate_header = d.pop("consolidateHeader", UNSET)

        consolidate_citations = d.pop("consolidateCitations", UNSET)

        include_raw_citations = d.pop("includeRawCitations", UNSET)

        include_raw_affiliations = d.pop("includeRawAffiliations", UNSET)

        tei_coordinates = d.pop("teiCoordinates", UNSET)

        segment_sentences = d.pop("segmentSentences", UNSET)

        process_form = cls(
            input_=input_,
            generate_ids=generate_ids,
            consolidate_header=consolidate_header,
            consolidate_citations=consolidate_citations,
            include_raw_citations=include_raw_citations,
            include_raw_affiliations=include_raw_affiliations,
            tei_coordinates=tei_coordinates,
            segment_sentences=segment_sentences,
        )

        return process_form
