from madtypes import MadType
from typing import Optional
from enum import Enum


class Content(str, metaclass=MadType):
    description = "Text body of the item"
    annotation = str


class Summary(str, metaclass=MadType):
    description = "Short version of the content"
    annotation = str


class Picture(str, metaclass=MadType):
    description = "Image linked to the item"
    annotation = str
    pattern = r"^([a-zA-Z0-9]+(-[a-zA-Z0-9]+)*\.)+[a-zA-Z]{2,}"


class Author(str, metaclass=MadType):
    """todo : SHA1 format check ?"""

    description = "SHA1 encoding of the username assigned as creator of the item on its source platform"
    annotation = str


class CreatedAt(str, metaclass=MadType):
    description = "ISO8601/RFC3339 Date of creation of the item"
    annotation = str
    pattern = r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(.[0-9]{1,6})?Z$"


class Title(str, metaclass=MadType):
    description = "Headline of the item"
    annotation = str


class Domain(str, metaclass=MadType):
    description = "Domain name on which the item was retrieved"
    annotation = str


class Url(str, metaclass=MadType):
    description = "Uniform-Resource-Locator"
    annotation = str
    pattern = r"^https?:\/\/[\S]{1,400}$"


class ExternalId(str, metaclass=MadType):
    description = "Identifier used by source"
    annotation = str


class ExternalParentId(str, metaclass=MadType):
    description = "Identifier of parent item, as used by source"
    annotation = str


class CalmItem(dict):
    """Created by a scraping module, it represent a post, article, comment..."""

    created_at: CreatedAt
    title: Optional[Title]  # titre obligatoire si pas de contenu
    content: Optional[Content]
    summary: Optional[Summary]  # <- description or summary available
    picture: Optional[Url]
    author: Optional[Author]
    external_id: Optional[ExternalId]
    external_parent_id: Optional[ExternalParentId]
    domain: Domain
    url: Url
    # type: Type # work in progress

    def is_valid(self, **kwargs) -> bool:
        """object is valid if we either have content or title"""
        return (
            False
            if not kwargs.get("content", None)
            and not kwargs.get("title", None)
            else True
        )


class Item(CalmItem, metaclass=MadType):
    pass


class Translated(str, metaclass=MadType):
    description = "The content translated in English language"
    annotation = str


class Language(str, metaclass=MadType):
    description = (
        "ISO639-1 language code that consists of two lowercase letters"
    )
    annotation = str


class CalmTranslation(dict):
    """Result of argos translate"""

    language: Optional[Language]  # uses content or title
    translation: Translated


class Translation(CalmTranslation, metaclass=MadType):
    pass


class Keywords(list, metaclass=MadType):
    description = "The main keywords extracted from the content field"
    annotation = list[str]


class TopKeywords(dict, metaclass=MadType):
    top_keywords: Keywords


class Classification(dict, metaclass=MadType):
    description = "label and score of zero_shot"
    score: float
    label: str


class Sentiment(float, metaclass=MadType):
    description = "Measure of post sentiment from negative to positive (-1 = negative, +1 = positive, 0 = neutral)"
    annotation = float


class Embedding(list, metaclass=MadType):
    description = "Vector/numerical representation of the translated content (field: translation), produced by a NLP encoder model"
    annotation = list[float]


class LanguageScore(float, metaclass=MadType):
    description = "Readability score of the text"
    annotation = float


class Gender(dict, metaclass=MadType):
    male: float
    female: float
    description = "Probable gender (female or male) of the author"


class SourceType(str, metaclass=MadType):
    description = "Category of the source that has produced the post"
    annotation = str


class TextType(dict, metaclass=MadType):
    assumption: float
    anecdote: float
    none: float
    definition: float
    testimony: float
    other: float
    study: float
    description = "Type (category) of the post (article, etc)"


class Emotion(dict, metaclass=MadType):
    love: float
    admiration: float
    joy: float
    approval: float
    caring: float
    excitement: float
    gratitude: float
    desire: float
    anger: float
    optimism: float
    disapproval: float
    grief: float
    annoyance: float
    pride: float
    curiosity: float
    neutral: float
    disgust: float
    disappointment: float
    realization: float
    fear: float
    relief: float
    confusion: float
    remorse: float
    embarrassment: float
    surprise: float
    sadness: float
    nervousness: float


class Irony(dict, metaclass=MadType):
    irony: float
    non_irony: float
    description = "Measure of how much a post is ironic (in %)"


class Age(dict, metaclass=MadType):
    below_twenty: float
    twenty_thirty: float
    thirty_forty: float
    forty_more: float
    description = "Measure author's age"


class Analysis(dict, metaclass=MadType):
    language_score: LanguageScore
    sentiment: Sentiment
    embedding: Embedding
    gender: Gender
    classification: Classification
    text_type: TextType
    emotion: Emotion
    irony: Irony
    age: Age


class Processed(dict, metaclass=MadType):
    translation: Translation
    top_keywords: Keywords
    classification: Classification
    item: Item


class CollectedAt(str, metaclass=MadType):
    description = "ISO8601/RFC3339 Date of collection of the item"
    annotation = str
    pattern = r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(.[0-9]{1,6})?Z$"


class CollectionClientVersion(str, metaclass=MadType):
    description = (
        "Client identifier with version of the client that collected the item."
    )
    annotation = str


class CollectionModule(str, metaclass=MadType):
    description = "Module that scraped the item."
    annotation = str


class BatchKindEnum(Enum):
    SPOTTING = "SPOTTING"
    VALIDATION = "VALIDATION"


class ProtocolItem(dict, metaclass=MadType):
    """Created by a scraping module, it represent a post, article, comment..."""

    created_at: CreatedAt
    title: Optional[Title]  # titre obligatoire si pas de contenu
    raw_content: Optional[Content]
    translated_content: Optional[Content]
    summary: Optional[Summary]  # <- description or summary available
    picture: Optional[Url]
    author: Optional[Author]
    external_id: Optional[ExternalId]
    external_parent_id: Optional[ExternalParentId]
    domain: Domain
    url: Url
    language: Language
    # type: Type # work in progress

    def is_valid(self, **kwargs) -> bool:
        """object is valid if we either have content or title"""
        return (
            False
            if not kwargs.get("content", None)
            and not kwargs.get("title", None)
            else True
        )


class ProtocolAnalysis(dict, metaclass=MadType):
    classification: Classification
    top_keywords: Keywords
    language_score: LanguageScore
    sentiment: Sentiment
    embedding: Embedding
    #gender: Gender
    source_type: SourceType
    # text_type: TextType
    emotion: Emotion
    # irony: Irony
    # age: Age


class ProcessedItem(dict, metaclass=MadType):
    item: ProtocolItem
    analysis: ProtocolAnalysis
    collection_client_version: CollectionClientVersion
    collection_module: CollectionModule
    collected_at: CollectedAt


class Batch(dict, metaclass=MadType):
    items: list[ProcessedItem]
    kind: BatchKindEnum

