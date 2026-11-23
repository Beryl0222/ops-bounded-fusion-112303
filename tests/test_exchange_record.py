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
