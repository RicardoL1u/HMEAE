import unittest
from utils import StanfordCoreNLPv2
import constant

class TestSTF(unittest.TestCase):
    def test_v2(self):
        nlp = StanfordCoreNLPv2(constant.corenlp_path)

if __name__ == '__main__':
    unittest.main()

