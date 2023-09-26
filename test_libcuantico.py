import unittest
import math
import matplotlib.pyplot as plot
import cuantico as ctc

class TestSalto_Clasico_Cuantico(unittest.TestCase):
    def test_canicas(self):
        v1 = [3, 9, 10]
        m1 = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
        click = 6
        resil = [3, 9, 10]
        expect = ctc.canicas(m1, v1, click)
        self.assertEqual(resil, expect)

    def test_canica_2(self):
        v2 = [5, 6, 7, 18]
        m2 = [[0, 1, 0, 1], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0]]
        click2 = 2
        result = [7, 5, 24, 0]
        expect = ctc.canicas(m2, v2, click2)
        self.assertEqual(result, expect)

    def test_fracciones(self):
        v1 = [1, 2, 0]
        m1 = [[1 / 3, 2 / 3, 0], [2 / 3, 1 / 3, 0], [0, 0, 1]]
        click1 = 8
        result = [0.5, 0.5, 0.0]
        expect = ctc.fracciones(m1, v1, click1)
        self.assertEqual(result, expect)

    def test_fracciones_2(self):
        v2 = [0, 0, 1, 0]
        m2 = [[3 / 4, 1 / 4, 0, 0], [1 / 4, 1 / 4, 1 / 4, 1 / 4], [0, 1 / 4, 3 / 4, 0], [0, 1 / 4, 0, 3 / 4]]
        click2 = 3
        result = [0.11, 0.25, 0.53, 0.11]
        expect = ctc.fracciones(m2, v2, click2)
        self.assertEqual(result, expect)


    def test_complejos_fracciones(self):
        v1 = [1 / math.sqrt(3), 2j / math.sqrt(15), math.sqrt(2 / 5)]
        m1 = [[1 / math.sqrt(2), 1 / math.sqrt(2), 0], [-1j / math.sqrt(2), 1j / math.sqrt(2), 0], [0, 0, 1j]]
        click = 1
        result = "Matriz no doblemente estocástica"
        expect = ctc.complex(m1, v1, click)
        self.assertEqual(result, expect)


    def test_exp_rendijas_cuant(self):
        mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1 / math.sqrt(3), 0, 0, 0, 0, 0, 0, 0, 0],
                   [1 / math.sqrt(3), 0, 0, 0, 0, 0, 0, 0, 0], [1 / math.sqrt(3), 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, (-1 + 1j) / math.sqrt(6), 0, 0, 1, 0, 0, 0, 0],
                   [0, (-1 - 1j) / math.sqrt(6), (-1 + 1j) / math.sqrt(6), 0, 0, 1, 0, 0, 0],
                   [0, (1 - 1j) / math.sqrt(6), (-1 - 1j) / math.sqrt(6), (-1 + 1j) / math.sqrt(6), 0, 0, 1, 0, 0],
                   [0, 0, (1 - 1j) / math.sqrt(6), (-1 - 1j) / math.sqrt(6), 0, 0, 0, 1, 0],
                   [0, 0, 0, (1 - 1j) / math.sqrt(6), 0, 0, 0, 0, 1]]
        result = [0j, 0j, 0j, 0j, (-0.2357022603955159 + 0.2357022603955159j), (-0.4714045207910318 + 0j),(-0.2357022603955159 - 0.2357022603955159j), -0.4714045207910318j,
                   (0.2357022603955159 - 0.2357022603955159j)]
        expect = ctc.exp_rendijas_cuant(mat)
        self.assertEqual(result, expect)

    def test_grafica(self):
        result = None
        expect = ctc.graficar(ctc.fracciones([[1 / 3, 2 / 3, 0], [2 / 3, 1 / 3, 0], [0, 0, 1]], [1, 0, 0], 1))
        self.assertEqual(result, expect)

    def test_grafica_2(self):
        result = None
        expect = ctc.graficar(ctc.fracciones([[3 / 4, 1 / 4, 0, 0], [1 / 4, 1 / 4, 1 / 4, 1 / 4], [0, 1 / 4, 3 / 4, 0], [0, 1 / 4, 0, 3 / 4]],[0, 0, 1, 0], 3))
        self.assertEqual(result, expect)

if __name__ == "__main__":
    unittest.main()