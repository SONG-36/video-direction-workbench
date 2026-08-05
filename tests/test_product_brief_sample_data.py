import json
import unittest
from pathlib import Path

from video_direction_workbench.domain import ProductBrief


SAMPLE_PATH = Path("sample_data/products/car_vacuum_yd_592c.product_brief.json")


class ProductBriefSampleDataTest(unittest.TestCase):
    def load_sample(self) -> dict[str, object]:
        return json.loads(SAMPLE_PATH.read_text(encoding="utf-8"))

    def load_brief(self) -> ProductBrief:
        return ProductBrief.model_validate(self.load_sample())

    def test_json_file_exists(self) -> None:
        self.assertTrue(SAMPLE_PATH.exists())

    def test_json_can_be_read(self) -> None:
        data = self.load_sample()

        self.assertIsInstance(data, dict)
        self.assertEqual(data["product_id"], "car_vacuum_yd_592c")

    def test_product_brief_model_validate_passes(self) -> None:
        brief = self.load_brief()

        self.assertEqual(brief.product_id, "car_vacuum_yd_592c")

    def test_product_id_is_expected(self) -> None:
        brief = self.load_brief()

        self.assertEqual(brief.product_id, "car_vacuum_yd_592c")

    def test_required_sources_are_present(self) -> None:
        brief = self.load_brief()
        source_ids = {source.source_id for source in brief.sources}

        self.assertIn("product_image_001", source_ids)
        self.assertIn("product_text_001", source_ids)
        self.assertIn("spec_image_001", source_ids)
        self.assertIn("operator_confirm_001", source_ids)

    def test_supplier_model_is_confirmed_fact(self) -> None:
        brief = self.load_brief()
        statements = {fact.statement for fact in brief.confirmed_facts}

        self.assertIn("YD-592C 是供应商型号", statements)

    def test_public_runtime_is_confirmed_fact(self) -> None:
        brief = self.load_brief()
        statements = {fact.statement for fact in brief.confirmed_facts}

        self.assertIn("对外续航口径为 15 分钟", statements)

    def test_unknown_items_include_unconfirmed_charging_time(self) -> None:
        brief = self.load_brief()
        questions = {item.question for item in brief.unknown_items}

        self.assertIn("充电时间当前无法确认", questions)

    def test_prohibited_claims_include_suction_over_17000pa(self) -> None:
        brief = self.load_brief()
        statements = {claim.statement for claim in brief.prohibited_claims}

        self.assertIn("吸力超过 17000Pa", statements)

    def test_prohibited_claims_include_all_levels_30_minutes(self) -> None:
        brief = self.load_brief()
        statements = {claim.statement for claim in brief.prohibited_claims}

        self.assertIn("所有档位均可使用 30 分钟", statements)

    def test_all_confirmed_fact_source_ids_exist(self) -> None:
        brief = self.load_brief()
        source_ids = {source.source_id for source in brief.sources}

        for fact in brief.confirmed_facts:
            for source_id in fact.source_ids:
                self.assertIn(source_id, source_ids)

    def test_product_brief_can_dump_json(self) -> None:
        brief = self.load_brief()
        dumped = brief.model_dump_json()

        self.assertIn("car_vacuum_yd_592c", dumped)
