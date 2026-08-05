import unittest

from pydantic import ValidationError

from video_direction_workbench.domain import (
    ConfirmedFact,
    FactCategory,
    ProhibitedClaim,
    UnknownItem,
)


def first_error_from(error: ValidationError) -> dict[str, object]:
    return error.errors()[0]


class UnknownItemTest(unittest.TestCase):
    def test_valid_unknown_item_can_be_created(self) -> None:
        item = UnknownItem(
            item_id="unknown_001",
            category=FactCategory.PARAMETER,
            question="产品型号是什么？",
            impact="不能在脚本中使用具体型号",
        )

        self.assertEqual(item.item_id, "unknown_001")
        self.assertEqual(item.category, FactCategory.PARAMETER)
        self.assertEqual(item.question, "产品型号是什么？")
        self.assertEqual(item.impact, "不能在脚本中使用具体型号")

    def test_item_id_question_and_impact_are_stripped(self) -> None:
        item = UnknownItem(
            item_id="  unknown_001  ",
            category=FactCategory.PARAMETER,
            question="  产品型号是什么？  ",
            impact="  不能在脚本中使用具体型号  ",
        )

        self.assertEqual(item.item_id, "unknown_001")
        self.assertEqual(item.question, "产品型号是什么？")
        self.assertEqual(item.impact, "不能在脚本中使用具体型号")

    def test_impact_none_is_allowed(self) -> None:
        item = UnknownItem(
            item_id="unknown_001",
            category=FactCategory.PARAMETER,
            question="产品型号是什么？",
            impact=None,
        )

        self.assertIsNone(item.impact)

    def test_blank_item_id_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            UnknownItem(
                item_id="   ",
                category=FactCategory.PARAMETER,
                question="产品型号是什么？",
            )

        error = first_error_from(context.exception)
        self.assertEqual(error["loc"], ("item_id",))
        self.assertIn("must not be blank", error["msg"])

    def test_blank_question_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            UnknownItem(
                item_id="unknown_001",
                category=FactCategory.PARAMETER,
                question="\t\n",
            )

        error = first_error_from(context.exception)
        self.assertEqual(error["loc"], ("question",))
        self.assertIn("must not be blank", error["msg"])

    def test_blank_impact_is_rejected_when_provided(self) -> None:
        with self.assertRaises(ValidationError) as context:
            UnknownItem(
                item_id="unknown_001",
                category=FactCategory.PARAMETER,
                question="产品型号是什么？",
                impact="   ",
            )

        error = first_error_from(context.exception)
        self.assertEqual(error["loc"], ("impact",))
        self.assertIn("must not be blank", error["msg"])

    def test_extra_field_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            UnknownItem(
                item_id="unknown_001",
                category=FactCategory.PARAMETER,
                question="产品型号是什么？",
                guessed_answer="VC-001",
            )

        error = first_error_from(context.exception)
        self.assertEqual(error["loc"], ("guessed_answer",))
        self.assertEqual(error["type"], "extra_forbidden")


class ProhibitedClaimTest(unittest.TestCase):
    def test_valid_prohibited_claim_is_created_and_text_is_cleaned(self) -> None:
        claim = ProhibitedClaim(
            claim_id="  claim_001  ",
            statement="  吸力达到 100000Pa  ",
            reason="  未经商品资料确认  ",
            source_ids=["  source_001  "],
        )

        self.assertEqual(claim.claim_id, "claim_001")
        self.assertEqual(claim.statement, "吸力达到 100000Pa")
        self.assertEqual(claim.reason, "未经商品资料确认")
        self.assertEqual(claim.source_ids, ["source_001"])

    def test_empty_source_ids_is_allowed(self) -> None:
        claim = ProhibitedClaim(
            claim_id="claim_001",
            statement="吸力达到 100000Pa",
            reason="未经商品资料确认",
            source_ids=[],
        )

        self.assertEqual(claim.source_ids, [])


class ProductInformationStatusClassificationTest(unittest.TestCase):
    def test_known_parameter_belongs_to_confirmed_fact(self) -> None:
        fact = ConfirmedFact(
            fact_id="fact_suction_001",
            category=FactCategory.PARAMETER,
            statement="吸力为 9000Pa",
            source_ids=["spec_001"],
        )

        self.assertEqual(fact.category, FactCategory.PARAMETER)
        self.assertEqual(fact.statement, "吸力为 9000Pa")
        self.assertEqual(fact.source_ids, ["spec_001"])

    def test_unconfirmed_parameter_question_belongs_to_unknown_item(self) -> None:
        item = UnknownItem(
            item_id="unknown_suction_001",
            category=FactCategory.PARAMETER,
            question="当前无法确认吸力参数是多少？",
            impact="不能在脚本中使用具体吸力数值",
        )

        self.assertEqual(item.category, FactCategory.PARAMETER)
        self.assertEqual(item.question, "当前无法确认吸力参数是多少？")

    def test_unverified_parameter_claim_belongs_to_prohibited_claim(self) -> None:
        claim = ProhibitedClaim(
            claim_id="claim_suction_001",
            statement="吸力达到 100000Pa",
            reason="未经商品资料确认，不得作为视频卖点",
            source_ids=[],
        )

        self.assertEqual(claim.statement, "吸力达到 100000Pa")
        self.assertEqual(claim.reason, "未经商品资料确认，不得作为视频卖点")
        self.assertEqual(claim.source_ids, [])

    def test_source_ids_preserve_order(self) -> None:
        claim = ProhibitedClaim(
            claim_id="claim_001",
            statement="吸力达到 100000Pa",
            reason="未经商品资料确认",
            source_ids=[" source_002 ", "source_001", "source_003"],
        )

        self.assertEqual(
            claim.source_ids,
            ["source_002", "source_001", "source_003"],
        )

    def test_blank_claim_id_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ProhibitedClaim(
                claim_id="   ",
                statement="吸力达到 100000Pa",
                reason="未经商品资料确认",
            )

        error = first_error_from(context.exception)
        self.assertEqual(error["loc"], ("claim_id",))

    def test_blank_statement_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ProhibitedClaim(
                claim_id="claim_001",
                statement="   ",
                reason="未经商品资料确认",
            )

        error = first_error_from(context.exception)
        self.assertEqual(error["loc"], ("statement",))

    def test_blank_reason_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ProhibitedClaim(
                claim_id="claim_001",
                statement="吸力达到 100000Pa",
                reason="\t\n",
            )

        error = first_error_from(context.exception)
        self.assertEqual(error["loc"], ("reason",))

    def test_blank_source_id_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ProhibitedClaim(
                claim_id="claim_001",
                statement="吸力达到 100000Pa",
                reason="未经商品资料确认",
                source_ids=["source_001", "   "],
            )

        error = first_error_from(context.exception)
        self.assertEqual(error["loc"], ("source_ids",))
        self.assertIn("must not be empty", error["msg"])

    def test_duplicate_source_ids_after_trimming_are_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ProhibitedClaim(
                claim_id="claim_001",
                statement="吸力达到 100000Pa",
                reason="未经商品资料确认",
                source_ids=["source_001", " source_001 "],
            )

        error = first_error_from(context.exception)
        self.assertEqual(error["loc"], ("source_ids",))
        self.assertIn("duplicates", error["msg"])

    def test_extra_field_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ProhibitedClaim(
                claim_id="claim_001",
                statement="吸力达到 100000Pa",
                reason="未经商品资料确认",
                severity="high",
            )

        error = first_error_from(context.exception)
        self.assertEqual(error["loc"], ("severity",))
        self.assertEqual(error["type"], "extra_forbidden")

    def test_confirmed_fact_requires_source_but_prohibited_claim_can_have_none(
        self,
    ) -> None:
        with self.assertRaises(ValidationError) as context:
            ConfirmedFact(
                fact_id="fact_001",
                category=FactCategory.FUNCTION,
                statement="支持吸尘",
                source_ids=[],
            )

        error = first_error_from(context.exception)
        self.assertEqual(error["loc"], ("source_ids",))

        claim = ProhibitedClaim(
            claim_id="claim_001",
            statement="吸力达到 100000Pa",
            reason="缺少可靠来源支持，禁止作为商品卖点",
            source_ids=[],
        )

        self.assertEqual(claim.source_ids, [])
