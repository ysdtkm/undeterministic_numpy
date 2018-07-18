#!/usr/bin/env python3

import unittest
import numpy as np

class TestNumpy(unittest.TestCase):
    def test_eigvals(self):
        b0 = np.load("b0.npy")
        for i in range(10):
            e1 = np.linalg.eigvals(b0)
            _ = b0 ** 2  # do something irrelevant
            e2 = np.linalg.eigvals(b0)
            self.assertEqual(np.max(np.abs(e1 - e2)), 0.0, "trial %d failed" % i)

unittest.main()


