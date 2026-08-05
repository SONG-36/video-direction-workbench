"""Foundational domain models for N01 product facts."""

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, field_validator


class SourceType(StrEnum):
    """Allowed source types for product fact evidence."""

    PRODUCT_IMAGE = "product_image"
    MANUAL = "manual"
    PACKAGING = "packaging"
    SPECIFICATION = "specification"
    OPERATOR_INPUT = "operator_input"
    OTHER = "other"


class FactCategory(StrEnum):
    """Allowed categories for confirmed product facts."""

    BASIC_INFORMATION = "basic_information"
    FUNCTION = "function"
    SELLING_POINT = "selling_point"
    USAGE_SCENARIO = "usage_scenario"
    ACCESSORY = "accessory"
    TARGET_USER = "target_user"
    PARAMETER = "parameter"
    APPEARANCE_CONSTRAINT = "appearance_constraint"


class SourceReference(BaseModel):
    """Stable reference to source material that supports product facts."""

    model_config = ConfigDict(extra="forbid")

    # 商品事实必须能稳定回溯来源，所以 source_id 需要可复用，而不是依赖标题或描述文本。
    source_id: str
    source_type: SourceType
    title: str
    locator: str | None = None
    note: str | None = None

    @field_validator("source_id", "title")
    @classmethod
    def validate_required_text(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("source_id and title must not be blank")
        return cleaned


class ConfirmedFact(BaseModel):
    """已经确认并允许进入后续业务流程的商品事实。

    ConfirmedFact 表示已经由人工或可靠资料确认，后续允许作为视频分析、方向决策和脚本生成依据的商品事实。
    """

    model_config = ConfigDict(extra="forbid")

    fact_id: str
    category: FactCategory
    statement: str
    source_ids: list[str]

    @field_validator("fact_id", "statement")
    @classmethod
    def validate_required_text(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("text must not be blank")
        return cleaned

    @field_validator("source_ids")
    @classmethod
    def validate_source_ids(cls, values: list[str]) -> list[str]:
        if not values:
            raise ValueError("source_ids must contain at least one source")

        cleaned_values: list[str] = []
        seen: set[str] = set()

        for value in values:
            cleaned = value.strip()

            if not cleaned:
                raise ValueError("source ID must not be empty")

            if cleaned in seen:
                raise ValueError("source_ids must not contain duplicates")

            seen.add(cleaned)
            cleaned_values.append(cleaned)

        return cleaned_values
