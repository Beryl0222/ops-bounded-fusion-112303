"""检查交换数据中用于回查的事实。"""
import unittest

import numpy as np

from bounded_fusion_input import load_record


class ExchangeRecordTests(unittest.TestCase):
    def test_exchange_contract(self):
        record = load_record()
        self.assertTrue(record["inputs"]["x"]["offsets"]["lane-a/c0"][0] == record["inputs"]["y"]["offsets"]["lane-a/c0"][0] != 0)
        self.assertTrue(record["inputs"]["x"]["base"][0] > record["nodes"][2][3][1])
        self.assertTrue(record["relation_changes"][0]["with"] in record["generators"] and record["relation_changes"][1]["with"] is None)
        self.assertTrue({n[1] for n in record["nodes"]} == {"linear","add","relu","clamp"})
        self.assertTrue([r["before_change"] for r in record["point_reads"]] == [0,1,2])
        self.assertTrue(record["point_reads"][-1]["unlinked"]["y"]["lane-b/c0"] == record["point_reads"][1]["values"]["lane-b/c0"])
        self.assertTrue(record["generators"]["lane-a/c0"][0] < record["refinements"][0]["range"][0])
