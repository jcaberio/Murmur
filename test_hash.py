import murmur
import string
import unittest


class TestMurmur(unittest.TestCase):
    def test_string_hash(self):
        expected_dict = {'a': 2456313694, 'c': 754329161, 'b': 2260187636, 'e': 3115762238, 'd': 4163039750, 'g': 1545794298, 'f': 4226522672, 'i': 3451942824, 'h': 1069002520, 'k': 3288208012, 'j': 3131388162, 'm': 3020367812, 'l': 2169669117, 'o': 1720432690, 'n': 1785613168, 'q': 2083633015, 'p': 834694889, 's': 389143345, 'r': 744399309, 'u': 1479000828, 't': 2418444476, 'w': 1340422676, 'v': 3414904798, 'y': 3657681515, 'x': 372604132, 'z': 2195360465}

        actual_dict = {letter: murmur.string_hash(letter) for letter in string.ascii_lowercase}

        unmatched_items = set(expected_dict.items()) ^ set(actual_dict.items())

        self.assertEqual(len(unmatched_items), 0)

    def test_file_hash(self):
        self.assertEqual(murmur.file_hash('test.txt'), 1575581059)
