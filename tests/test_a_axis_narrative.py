from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

EXPECTED = {
    "A1": ("11-A1-发现母体.md", "找源", "什么持续生成我的不同？"),
    "A2": ("12-A2-回到母体.md", "归源", "哪些东西真正属于我，哪些只是外界塑造？"),
    "A3": ("13-A3-获得原力.md", "炼源", "如何把潜在生成结构训练成真实能力？"),
    "A4": ("14-A4-显化原力.md", "证源", "这种原力进入真实世界后，是否真正创造价值？"),
}

SOUL_MERGES = {
    "459": "8a3fec26a7a9428577cbdb171ba4b2d4eab8f78e",
    "460": "7055adee537dd535c8f85f4a5aaf6fb76726150c",
    "461": "ac61e755fbe3722e1d3278fadc8e146fe8fddacb",
}


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


class AAxisNarrativeGuard(unittest.TestCase):
    def test_public_overview_keeps_part_one_as_force_asset(self):
        text = read("README.md")
        self.assertIn("第一部 · 原力资产", text)
        self.assertNotIn("第一部 · 原力母体", text)
        self.assertIn("原力母体", text)
        self.assertIn("第一因", text)
        self.assertIn("第一部不叫“原力母体”", text)

    def test_four_module_articles_have_exact_actions_and_questions(self):
        for module_id, (filename, action, question) in EXPECTED.items():
            text = read(f"10-yuanli-asset/{filename}")
            self.assertIn(f"教学动作：{action}", text, module_id)
            self.assertIn(f"第一性问题：{question}", text, module_id)

    def test_twelve_module_map_matches_a_axis_questions(self):
        text = read("00-canon/06-十二模块总图.md")
        for _, (_, action, question) in EXPECTED.items():
            self.assertIn(action, text)
            self.assertIn(question, text)

    def test_glossary_separates_teaching_actions_from_canon_names(self):
        text = read("80-governance/83-术语表.md")
        self.assertIn("找源 / 归源 / 炼源 / 证源 = 教学动作词、生成链词", text)
        self.assertIn("发现母体 / 回到母体 / 获得原力 / 显化原力 = 正典模块名", text)

    def test_b4_uses_exactly_four_control_rights(self):
        text = read("20-yuanli-venture/24-B4-壁垒锁定.md")
        for term in ["心智控制权", "交付控制权", "入口控制权", "留存控制权"]:
            self.assertIn(term, text)
        self.assertIn("飞轮是强化机制", text)
        self.assertIn("母体是生成源头", text)
        self.assertNotIn("六层壁垒全量", text)
        self.assertNotIn("B4 六层壁垒", text)

    def test_self_diagnosis_does_not_route_to_six_moats(self):
        text = read("50-spine/53-自诊-你卡在哪一关.md")
        self.assertNotIn("按六层壁垒排查", text)
        self.assertIn("不要再用“六层壁垒”分诊", text)

    def test_upstream_status_records_merged_soul_and_no_public_authority(self):
        text = read("90-sources/A-AXIS-SYNC-RECEIPT-v1.md")
        for pr, sha in SOUL_MERGES.items():
            self.assertIn(f"upstream_soul_pr_{pr}: MERGED", text)
            self.assertIn(sha, text)
        self.assertIn("upstream_soul_tip_for_this_sync: ac61e755fbe3722e1d3278fadc8e146fe8fddacb", text)
        self.assertIn("public_canon_authority: NONE", text)
        self.assertIn("live_reader_validation: NOT_ESTABLISHED", text)
        self.assertIn("market_outcome: NOT_ESTABLISHED", text)
        self.assertIn("feishu_projection: NOT_RUN", text)
        self.assertIn("publication_readiness: READY_FOR_PUBLIC_NARRATIVE_MERGE", text)


if __name__ == "__main__":
    unittest.main()
