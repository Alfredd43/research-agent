""" Contains some shared types for properties """
import re
from typing import BinaryIO, Generic, List, MutableMapping, Optional, TextIO, Tuple, TypeVar, Union

import attr
from httpx import HTTPError, codes


class Unset:
    def __bool__(self) -> bool:
        return False


UNSET: Unset = Unset()
FileJsonType = Tuple[Optional[str], Union[BinaryIO, TextIO], Optional[str]]


@attr.s(auto_attribs=True)
class File:
    """Contains information for file uploads"""

    payload: Union[BinaryIO, TextIO]
    file_name: Optional[str] = None
    mime_type: Optional[str] = None

    def to_tuple(self) -> FileJsonType:
        """Return a tuple representation that httpx will accept for multipart/form-data"""
        return self.file_name, self.payload, self.mime_type


T = TypeVar("T")


@attr.s(auto_attribs=True)
class Response(Generic[T]):
    """A response from an endpoint"""

    status_code: int
    content: bytes
    headers: MutableMapping[str, str]
    parsed: Optional[T]

    @property
    def is_informational(self) -> bool:
        """
        A property which is `True` for 1xx status codes, `False` otherwise.
        """
        return codes.is_informational(self.status_code)

    @property
    def is_success(self) -> bool:
        """
        A property which is `True` for 2xx status codes, `False` otherwise.
        """
        return codes.is_success(self.status_code)

    @property
    def is_redirect(self) -> bool:
        """
        A property which is `True` for 3xx status codes, `False` otherwise.

        Note that not all responses with a 3xx status code indicate a URL redirect.

        Use `response.has_redirect_location` to determine responses with a properly
        formed URL redirection.
        """
        return codes.is_redirect(self.status_code)

    @property
    def is_client_error(self) -> bool:
        """
        A property which is `True` for 4xx status codes, `False` otherwise.
        """
        return codes.is_client_error(self.status_code)

    @property
    def is_server_error(self) -> bool:
        """
        A property which is `True` for 5xx status codes, `False` otherwise.
        """
        return codes.is_server_error(self.status_code)

    @property
    def is_error(self) -> bool:
        """
        A property which is `True` for 4xx and 5xx status codes, `False` otherwise.
        """
        return codes.is_error(self.status_code)

    @property
    def has_redirect_location(self) -> bool:
        """
        Returns True for 3xx responses with a properly formed URL redirection,
        `False` otherwise.
        """
        return (
            self.status_code
            in (
                # 301 (Cacheable redirect. Method may change to GET.)
                codes.MOVED_PERMANENTLY,
                # 302 (Uncacheable redirect. Method may change to GET.)
                codes.FOUND,
                # 303 (Client should make a GET or HEAD request.)
                codes.SEE_OTHER,
                # 307 (Equiv. 302, but retain method)
                codes.TEMPORARY_REDIRECT,
                # 308 (Equiv. 301, but retain method)
                codes.PERMANENT_REDIRECT,
            )
            and "Location" in self.headers
        )

    def raise_for_status(self):
        """Raises :class:`HTTPError`, if one occurred."""

        http_error_msg = ""
        if isinstance(self.content, bytes):
            # We attempt to decode utf-8 first because some servers
            # choose to localize their reason strings. If the string
            # isn't utf-8, we fall back to iso-8859-1 for all other
            # encodings. (See PR #3538)
            try:
                reason = self.content.decode("utf-8")
            except UnicodeDecodeError:
                reason = self.content.decode("iso-8859-1")
        else:
            reason = self.content

        if 400 <= self.status_code < 500:
            http_error_msg = "%s Client Error: %s" % (self.status_code, reason)

        elif 500 <= self.status_code < 600:
            http_error_msg = "%s Server Error: %s" % (self.status_code, reason)

        if http_error_msg:
            raise HTTPError(http_error_msg)


from bs4 import BeautifulSoup, CData, NavigableString, Tag
from dateutil import parser


class TEI:
    """
    Methods to transform TEI (Text Encoding Initiative) XML into article objects.
    """

    @staticmethod
    def parse(stream, figures=False, back=False):
        """
        Parses a TEI XML datastream and returns a processed article.

        Args:
            stream: handle to input data stream
        Returns:
            Article
        """
        from .models import Article, ArticleCitations

        soup = BeautifulSoup(stream, "xml")
        sentences = soup.find("s") is not None
        title = soup.title.text
        art = Article(identifier=None, title=title)
        source = soup.find("sourceDesc")
        if source:
            struct = source.find("biblStruct")
            art.bibliography = TEI.citation(struct)
            if art.bibliography.ids:
                art.identifier = art.bibliography.ids["MD5"]

        # Parse text sections
        art.sections = TEI.text(soup, title, sentences, figures, back)

        listBibl = soup.find("listBibl")
        if listBibl:
            art.citations = ArticleCitations()
            for struct in listBibl.find_all("biblStruct"):
                name = struct.get("xml:id")
                art.citations.additional_properties[name] = TEI.citation(struct)
        return art

    @staticmethod
    def date(published):
        """
        Attempts to parse a publication date, if available. Otherwise, None is returned.

        Args:
            published: published object

        Returns:
            publication date if available/found, None otherwise
        """

        # Parse publication date
        # pylint: disable=W0702
        try:
            published = parser.parse(published["when"]) if published and "when" in published.attrs else None
        except:
            published = None

        return published

    @staticmethod
    def authors(source):
        """
        Parses authors and associated affiliations from the article.

        Args:
            elements: authors elements

        Returns:
            (semicolon separated list of authors, semicolon separated list of affiliations, primary affiliation)
        """
        from .models import Address, Affiliation, Author, PersName

        authors: List[Author] = []
        for author in source.find_all("author"):
            auth: Author = None
            affiliations: List[Affiliation] = []
            name = author.find("persName")
            if name:
                surname = name.find("surname")
                if surname:
                    pers = PersName(surname=surname.text)
                    auth = Author(pers_name=pers)
                    authors.append(auth)
                    for forename in name.find_all("forename"):
                        if "type" in forename.attrs and forename["type"] == "first":
                            pers.firstname = forename.text
                        elif "type" in forename.attrs and forename["type"] == "middle":
                            pers.middlename = forename.text
            if auth:
                email = author.find("email")
                if email:
                    auth.email = email.text
                for affiliation in author.find_all("affiliation"):
                    aff = Affiliation()
                    affiliations.append(aff)
                    for orgName in affiliation.find_all("orgName"):
                        if "type" in orgName.attrs and orgName["type"] == "institution":
                            aff.institution = orgName.text
                        if "type" in orgName.attrs and orgName["type"] == "department":
                            aff.department = orgName.text
                        if "type" in orgName.attrs and orgName["type"] == "laboratory":
                            aff.laboratory = orgName.text
                    auth.affiliations = affiliations
                    address = author.find("address")
                    if address:
                        aff.address = Address.from_dict(
                            {el.name: el.text for el in address.children if isinstance(el, Tag)}
                        )

        return authors

    @staticmethod
    def citation(struct):
        """
        Extracts article citation.
        """
        from .models import Citation, CitationIds, CitationScopes, CitationTitles

        citation = Citation()
        citation.authors = TEI.authors(struct)
        published = struct.find("date", attrs={"type": "published"})
        if published:
            # Parse publication information
            citation.published = TEI.date(published)
        publisher = struct.find("publisher")
        if publisher:
            citation.publisher = publisher.text
        ids_dict = {}
        for idno in struct.find_all("idno"):
            if "type" in idno.attrs:
                ids_dict[idno["type"]] = idno.text
        if ids_dict:
            citation.ids = CitationIds.from_dict(ids_dict)
        titles_dict = {}
        for title in struct.find_all("title"):
            if "level" in title.attrs:
                titles_dict[title["level"]] = title.text
        if len(titles_dict) > 0:
            citation.titles = CitationTitles.from_dict(titles_dict)
            citation.main_title = citation.titles.additional_properties.get("a", None)
        scopes_dict = {}
        for scope in struct.find_all("biblScope"):
            if "unit" in scope.attrs:
                val = []
                if "from" in scope.attrs:
                    val.append(scope["from"])
                if "to" in scope.attrs:
                    val.append(scope["to"])
                if not val:
                    val = scope.text
                scopes_dict[scope["unit"]] = str(val)
        if len(scopes_dict) > 0:
            citation.scopes = CitationScopes.from_dict(scopes_dict)
        return citation

    @staticmethod
    def abstract(soup, title, sentences=False):
        """
        Builds a list of title and abstract sections.

        Args:
            soup: bs4 handle
            title: article title

        Returns:
            list of sections
        """
        from .models import Section, TextWithRefs

        title_refs = TextWithRefs(text=title)
        sections = [Section("TITLE", paragraphs=[[title_refs]] if sentences else [title_refs])]

        abstract = soup.find("abstract")
        secs = []
        if abstract:
            for div in abstract.find_all("div", recursive=False):
                sec = TEI.section("ABSTRACT", None, div.children, sentences)
                secs.append(sec)
            sections.extend(secs)

        return sections

    @staticmethod
    def section(name, num, children, sentences=False):
        from .models import Section, TextWithRefs

        sec = Section(name=name, num=num, paragraphs=[])
        for p in children:
            if p:
                if sentences:
                    if isinstance(p, Tag) and p.name == "p":
                        sents = []
                        for s in p.children:
                            if isinstance(s, Tag) and s.name == "s":
                                sents.append(TEI.text_with_refs(s))
                            else:
                                sents.append(TextWithRefs(text=TEI.get_text(s)))
                        sec.paragraphs.append(sents)
                    else:
                        sec.paragraphs.append([TextWithRefs(text=TEI.get_text(p))])
                else:
                    if isinstance(p, Tag) and p.name == "p":
                        sec.paragraphs.append(TEI.text_with_refs(p))
                    else:
                        sec.paragraphs.append(TextWithRefs(text=TEI.get_text(p)))
        return sec

    @staticmethod
    def text(soup, title, sentences=False, figures=False, back=False):
        """
        Builds a list of text sections.

        Args:
            soup: bs4 handle
            title: article title

        Returns:
            list of sections
        """

        # Initialize with title and abstract text
        sections = TEI.abstract(soup, title, sentences)

        secs = []
        div_or_fig = re.compile("div|figure") if figures else "div"
        text = soup.find("text")
        divisions = ['body']
        if back:
            divisions.append('back')
        for division in divisions:
            text_div = text.find(division)
            if text_div:
                for section in text_div.find_all(div_or_fig, recursive=False):
                    # Section name and text
                    name = None
                    num = None
                    if section.name == "div" and section.has_attr("type"):
                        name = section["type"]
                        section = section.find("div")
                    if section is not None:
                        children = [child for child in section.children if isinstance(child, Tag)]
                        # Attempt to parse section header
                        if children and children[0].name == "head":
                            name = children[0].text
                            num = children[0]["n"] if "n" in children[0].attrs else None
                            children = children[1:]
                        if section.name == "div":
                            sec = TEI.section(name, num, children, sentences)
                            secs.append(sec)
                        elif section.name == "figure":
                            label = None
                            if children and children[0].name == "label":
                                label = children[0].text
                                children = children[1:]
                            desc = None
                            if children and children[0].name == "figDesc":
                                desc = children[0].find("div") or children[0]
                            children = [name, label]
                            if desc:
                                children.extend(desc.children)
                            # Use XML Id as figure name to ensure figures are uniquely named
                            name = section.get("xml:id")
                            sec = TEI.section(name, num, children, sentences)
                            secs.append(sec)
            # Transform and clean text
            # text = Text.transform(text)
            # Split text into sentences, transform text and add to sections
        sections.extend(secs)

        # Extract text from tables
        # for figure in soup.find("text").find_all("figure"):
        #     name = figure.get("xml:id").upper()
        #
        #     figure.find("table")
        #     # if table:
        #     #     sections.extend([(name, x) for x in Table.extract(table)])

        return sections

    @staticmethod
    def get_text(node):
        return node.get_text() if isinstance(node, Tag) else str(node)

    @staticmethod
    def text_with_refs(node):
        from .models import Ref, TextWithRefs

        str_and_refs = TEI._all_strings_and_refs(node)
        text = ""
        start = 0
        refs = []
        for el in str_and_refs:
            start = len(text)
            if isinstance(el, Tag):
                end = start + len(el.text)
                ref = Ref(start=start, end=end)
                if "type" in el.attrs:
                    ref.type = el["type"]
                if "target" in el.attrs:
                    ref.target = el["target"]
                refs.append(ref)
            else:
                text += str(el)
        return TextWithRefs(text=text, refs=refs)

    @staticmethod
    def _all_strings_and_refs(node, reftag="ref", strip=False):
        types = (NavigableString, CData)
        for descendant in node.descendants:
            if types is None and not isinstance(descendant, NavigableString):
                continue
            descendant_type = type(descendant)
            if isinstance(types, type):
                if descendant_type is not types:
                    # We're not interested in strings of this type.
                    continue
            elif descendant_type is Tag and descendant.name == reftag:
                yield descendant
            elif types is not None and descendant_type not in types:
                # We're not interested in strings of this type.
                continue
            else:
                if strip:
                    descendant = descendant.strip()
                    if len(descendant) == 0:
                        continue
                yield descendant


__all__ = ["File", "Response", "FileJsonType", "TEI"]
