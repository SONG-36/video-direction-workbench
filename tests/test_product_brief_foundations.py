import unittest

from pydantic import ValidationError

from video_direction_workbench.domain import (
    ConfirmedFact,
    FactCategory,
    SourceReference,
    SourceType,
)


class SourceReferenceTest(unittest.TestCase):
    def test_valid_source_reference_can_be_created(self) -> None:
        source = SourceReference(
            source_id="manual-001",
            source_type=SourceType.MANUAL,
            title="User manual",
            locator="page 3",
            note="Motor specification section",
        )

        self.assertEqual(source.source_id, "manual-001")
        self.assertEqual(source.source_type, SourceType.MANUAL)
        self.assertEqual(source.title, "User manual")
        self.assertEqual(source.locator, "page 3")
        self.assertEqual(source.note, "Motor specification section")

    def test_source_id_and_title_are_stripped(self) -> None:
        source = SourceReference(
            source_id="  packaging-front  ",
            source_type=SourceType.PACKAGING,
            title="  Front packaging  ",
        )

        self.assertEqual(source.source_id, "packaging-front")
        self.assertEqual(source.title, "Front packaging")

    def test_blank_source_id_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            SourceReference(
                source_id="   ",
                source_type=SourceType.MANUAL,
                title="User manual",
            )

        error = context.exception.errors()[0]
        self.assertEqual(error["loc"], ("source_id",))
        self.assertIn("must not be blank", error["msg"])

    def test_blank_title_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            SourceReference(
                source_id="manual-001",
                source_type=SourceType.MANUAL,
                title="   ",
            )

        error = context.exception.errors()[0]
        self.assertEqual(error["loc"], ("title",))
        self.assertIn("must not be blank", error["msg"])

    def test_extra_field_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            SourceReference(
                source_id="manual-001",
                source_type=SourceType.MANUAL,
                title="User manual",
                confidence=0.9,
            )

        error = context.exception.errors()[0]
        self.assertEqual(error["loc"], ("confidence",))
        self.assertEqual(error["type"], "extra_forbidden")

    def test_enum_values_are_correct(self) -> None:
        self.assertEqual(SourceType.PRODUCT_IMAGE.value, "product_image")
        self.assertEqual(SourceType.MANUAL.value, "manual")
        self.assertEqual(SourceType.PACKAGING.value, "packaging")
        self.assertEqual(SourceType.SPECIFICATION.value, "specification")
        self.assertEqual(SourceType.OPERATOR_INPUT.value, "operator_input")
        self.assertEqual(SourceType.OTHER.value, "other")

        self.assertEqual(FactCategory.BASIC_INFORMATION.value, "basic_information")
        self.assertEqual(FactCategory.FUNCTION.value, "function")
        self.assertEqual(FactCategory.SELLING_POINT.value, "selling_point")
        self.assertEqual(FactCategory.USAGE_SCENARIO.value, "usage_scenario")
        self.assertEqual(FactCategory.ACCESSORY.value, "accessory")
        self.assertEqual(FactCategory.TARGET_USER.value, "target_user")
        self.assertEqual(FactCategory.PARAMETER.value, "parameter")
        self.assertEqual(
            FactCategory.APPEARANCE_CONSTRAINT.value,
            "appearance_constraint",
        )


class ConfirmedFactLearningTest(unittest.TestCase):
    def test_valid_confirmed_fact_is_created_and_trimmed(self) -> None:
        fact = ConfirmedFact(
            fact_id="  fact_001  ",
            category=FactCategory.FUNCTION,
            statement="  支持吸尘  ",
            source_ids=["  source_001  ", "source_002"],
        )

        self.assertEqual(fact.fact_id, "fact_001")
        self.assertEqual(fact.category, FactCategory.FUNCTION)
        self.assertEqual(fact.statement, "支持吸尘")
        self.assertEqual(fact.source_ids, ["source_001", "source_002"])

    def test_blank_fact_id_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ConfirmedFact(
                fact_id="   ",
                category=FactCategory.FUNCTION,
                statement="支持吸尘",
                source_ids=["source_001"],
            )

        error = context.exception.errors()[0]
        self.assertEqual(error["loc"], ("fact_id",))

    def test_blank_statement_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ConfirmedFact(
                fact_id="fact_001",
                category=FactCategory.FUNCTION,
                statement="\t\n",
                source_ids=["source_001"],
            )

        error = context.exception.errors()[0]
        self.assertEqual(error["loc"], ("statement",))

    def test_empty_source_ids_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ConfirmedFact(
                fact_id="fact_001",
                category=FactCategory.FUNCTION,
                statement="支持吸尘",
                source_ids=[],
            )

        error = context.exception.errors()[0]
        self.assertEqual(error["loc"], ("source_ids",))
        self.assertIn("at least one source", error["msg"])

    def test_blank_source_id_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ConfirmedFact(
                fact_id="fact_001",
                category=FactCategory.FUNCTION,
                statement="支持吸尘",
                source_ids=["source_001", "   "],
            )

        error = context.exception.errors()[0]
        self.assertEqual(error["loc"], ("source_ids",))
        self.assertIn("must not be empty", error["msg"])

    def test_duplicate_source_ids_after_trimming_are_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ConfirmedFact(
                fact_id="fact_001",
                category=FactCategory.FUNCTION,
                statement="支持吸尘",
                source_ids=["source_001", " source_001 "],
            )

        error = context.exception.errors()[0]
        self.assertEqual(error["loc"], ("source_ids",))
        self.assertIn("duplicates", error["msg"])

    def test_extra_field_is_rejected(self) -> None:
        with self.assertRaises(ValidationError) as context:
            ConfirmedFact(
                fact_id="fact_001",
                category=FactCategory.FUNCTION,
                statement="支持吸尘",
                source_ids=["source_001"],
                confidence=0.9,
            )

        error = context.exception.errors()[0]
        self.assertEqual(error["loc"], ("confidence",))
        self.assertEqual(error["type"], "extra_forbidden")
