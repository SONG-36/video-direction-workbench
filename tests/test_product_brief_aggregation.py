import unittest

from pydantic import ValidationError

from video_direction_workbench.domain import (
    ConfirmedFact,
    FactCategory,
    ProductBrief,
    ProhibitedClaim,
    SourceReference,
    SourceType,
    UnknownItem,
)


def make_source(source_id: str = "source_001") -> SourceReference:
    return SourceReference(
        source_id=source_id,
        source_type=SourceType.SPECIFICATION,
        title="商品说明文本",
    )


def make_fact(
    fact_id: str = "fact_001",
    statement: str = "支持吸尘",
    source_ids: list[str] | None = None,
) -> ConfirmedFact:
    return ConfirmedFact(
        fact_id=fact_id,
        category=FactCategory.FUNCTION,
        statement=statement,
        source_ids=source_ids if source_ids is not None else ["source_001"],
    )


def make_unknown(item_id: str = "unknown_001") -> UnknownItem:
    return UnknownItem(
        item_id=item_id,
        category=FactCategory.PARAMETER,
        question="当前无法确认吸力参数是多少？",
    )


def make_claim(
    claim_id: str = "claim_001",
    statement: str = "吸力达到 100000Pa",
    source_ids: list[str] | None = None,
) -> ProhibitedClaim:
    return ProhibitedClaim(
        claim_id=claim_id,
        statement=statement,
        reason="未经商品资料确认，不得作为视频卖点",
        source_ids=source_ids if source_ids is not None else [],
    )


def first_error_message(error: ValidationError) -> str:
    return str(error.errors()[0]["msg"])


class ProductBriefAggregationTest(unittest.TestCase):
    def test_minimal_product_brief_is_valid(self) -> None:
        brief = ProductBrief(
            product_id="  product_001  ",
            product_name="  便携式无线车载吸尘器  ",
        )

        self.assertEqual(brief.product_id, "product_001")
        self.assertEqual(brief.product_name, "便携式无线车载吸尘器")
        self.assertEqual(brief.revision, 1)
        self.assertEqual(brief.sources, [])
        self.assertEqual(brief.confirmed_facts, [])
        self.assertEqual(brief.unknown_items, [])
        self.assertEqual(brief.prohibited_claims, [])

    def test_full_product_brief_is_valid(self) -> None:
        brief = ProductBrief(
            product_id="product_001",
            product_name="便携式无线车载吸尘器",
            sources=[
                SourceReference(
                    source_id="source_001",
                    source_type=SourceType.SPECIFICATION,
                    title="商品说明文本",
                ),
                SourceReference(
                    source_id="source_002",
                    source_type=SourceType.PRODUCT_IMAGE,
                    title="商品图片",
                ),
            ],
            confirmed_facts=[
                ConfirmedFact(
                    fact_id="fact_001",
                    category=FactCategory.FUNCTION,
                    statement="支持吸尘",
                    source_ids=["source_001"],
                ),
                ConfirmedFact(
                    fact_id="fact_002",
                    category=FactCategory.APPEARANCE_CONSTRAINT,
                    statement="黑色双筒主体",
                    source_ids=["source_002"],
                ),
            ],
            unknown_items=[
                UnknownItem(
                    item_id="unknown_001",
                    category=FactCategory.PARAMETER,
                    question="当前无法确认吸力参数是多少？",
                )
            ],
            prohibited_claims=[
                ProhibitedClaim(
                    claim_id="claim_001",
                    statement="吸力达到 100000Pa",
                    reason="未经商品资料确认",
                    source_ids=[],
                )
            ],
        )

        self.assertEqual(len(brief.sources), 2)
        self.assertEqual(len(brief.confirmed_facts), 2)
        self.assertEqual(len(brief.unknown_items), 1)
        self.assertEqual(len(brief.prohibited_claims), 1)

    def test_duplicate_source_id_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ProductBrief(
                product_id="product_001",
                product_name="便携式无线车载吸尘器",
                sources=[make_source("source_001"), make_source("source_001")],
            )

        self.assertIn("sources.source_id", first_error_message(context.exception))

    def test_duplicate_fact_id_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ProductBrief(
                product_id="product_001",
                product_name="便携式无线车载吸尘器",
                sources=[make_source()],
                confirmed_facts=[
                    make_fact("fact_001", "支持吸尘"),
                    make_fact("fact_001", "支持清洁座椅缝隙"),
                ],
            )

        self.assertIn("confirmed_facts.fact_id", first_error_message(context.exception))

    def test_duplicate_item_id_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ProductBrief(
                product_id="product_001",
                product_name="便携式无线车载吸尘器",
                unknown_items=[make_unknown("unknown_001"), make_unknown("unknown_001")],
            )

        self.assertIn("unknown_items.item_id", first_error_message(context.exception))

    def test_duplicate_claim_id_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ProductBrief(
                product_id="product_001",
                product_name="便携式无线车载吸尘器",
                prohibited_claims=[
                    make_claim("claim_001", "吸力达到 100000Pa"),
                    make_claim("claim_001", "续航达到 8 小时"),
                ],
            )

        self.assertIn("prohibited_claims.claim_id", first_error_message(context.exception))

    def test_confirmed_fact_missing_source_reference_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ProductBrief(
                product_id="product_001",
                product_name="便携式无线车载吸尘器",
                sources=[make_source("source_001")],
                confirmed_facts=[make_fact(source_ids=["missing_source"])],
            )

        message = first_error_message(context.exception)
        self.assertIn("confirmed_facts.source_ids", message)
        self.assertIn("missing_source", message)

    def test_prohibited_claim_missing_source_reference_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ProductBrief(
                product_id="product_001",
                product_name="便携式无线车载吸尘器",
                sources=[make_source("source_001")],
                prohibited_claims=[make_claim(source_ids=["missing_source"])],
            )

        message = first_error_message(context.exception)
        self.assertIn("prohibited_claims.source_ids", message)
        self.assertIn("missing_source", message)

    def test_prohibited_claim_empty_source_ids_remains_valid(self) -> None:
        brief = ProductBrief(
            product_id="product_001",
            product_name="便携式无线车载吸尘器",
            sources=[make_source("source_001")],
            prohibited_claims=[make_claim(source_ids=[])],
        )

        self.assertEqual(brief.prohibited_claims[0].source_ids, [])

    def test_duplicate_confirmed_statement_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ProductBrief(
                product_id="product_001",
                product_name="便携式无线车载吸尘器",
                sources=[make_source()],
                confirmed_facts=[
                    make_fact("fact_001", " Supports suction "),
                    make_fact("fact_002", "supports   suction"),
                ],
            )

        self.assertIn("confirmed_facts.statement", first_error_message(context.exception))

    def test_duplicate_prohibited_statement_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ProductBrief(
                product_id="product_001",
                product_name="便携式无线车载吸尘器",
                prohibited_claims=[
                    make_claim("claim_001", " Claims 100000Pa "),
                    make_claim("claim_002", "claims   100000pa"),
                ],
            )

        self.assertIn("prohibited_claims.statement", first_error_message(context.exception))

    def test_confirmed_and_prohibited_same_statement_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ProductBrief(
                product_id="product_001",
                product_name="便携式无线车载吸尘器",
                sources=[make_source()],
                confirmed_facts=[make_fact(statement="支持吸尘")],
                prohibited_claims=[make_claim(statement=" 支持吸尘 ")],
            )

        self.assertIn("must not conflict", first_error_message(context.exception))

    def test_revision_less_than_one_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ProductBrief(
                product_id="product_001",
                product_name="便携式无线车载吸尘器",
                revision=0,
            )

        error = context.exception.errors()[0]
        self.assertEqual(error["loc"], ("revision",))

    def test_extra_field_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ProductBrief(
                product_id="product_001",
                product_name="便携式无线车载吸尘器",
                approved=True,
            )

        error = context.exception.errors()[0]
        self.assertEqual(error["loc"], ("approved",))
        self.assertEqual(error["type"], "extra_forbidden")

    def test_blank_notes_becomes_none(self) -> None:
        brief = ProductBrief(
            product_id="product_001",
            product_name="便携式无线车载吸尘器",
            notes="   ",
        )

        self.assertIsNone(brief.notes)
