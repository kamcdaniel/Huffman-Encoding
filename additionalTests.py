import unittest
from proj3 import count_frequency, create_priority_queue, build_tree_from_queue, generate_codes, encode, decode, Node, MinHeap, extract_min

class StudentTestHuffmanEncoding(unittest.TestCase):
    def test_count_frequency(self):
        result = count_frequency("hello")
        expected = {"l": 2, "e": 1, "h": 1, "o": 1}
        self.assertEqual(result, expected)

    def test_count_frequency_with_new_word(self):
        result = count_frequency("ABBA")
        expected = {"A": 2, "B": 2}
        self.assertEqual(result, expected)

    def test_create_priority_queue(self):
        frequency = count_frequency("ABBA")
        result = create_priority_queue(frequency)
        expected = MinHeap(data = [Node(freq = 2, char = "A", left = None, right = None), Node(freq = 2, char = "B", left = None, right = None)]) 
        self.assertEqual(result, expected)

    def test_build_tree_from_queue(self):
        frequency = count_frequency("ABBA")
        pq = create_priority_queue(frequency)
        result = build_tree_from_queue(pq)
        expected = Node(freq = 4, char = "A", left = Node(freq = 2, char = "A", left = None, right = None), right = Node(freq = 2, char = "B", left = None, right = None))
        self.assertEqual(result, expected)

    def test_build_tree_from_queue_again(self):
        frequency = count_frequency("ABC")
        pq = create_priority_queue(frequency)
        result = build_tree_from_queue(pq)
        expected = Node(freq = 3, char = "C", left = Node(freq = 1, char = "C", left = None, right = None), right = Node(freq = 2, char = "A", left = Node(freq = 1, char = "A", left = None, right = None), right = Node(freq = 1, char = "B", left = None, right = None)))

    def test_generate_codes(self):
        frequency = count_frequency("ABBA")
        pq = create_priority_queue(frequency)
        tree = build_tree_from_queue(pq)
        result = generate_codes(tree)
        expected = {"A": "0", "B": "1"}
        self.assertEqual(result, expected)

    def test_encode(self):
        frequency = count_frequency("ABBA")
        pq = create_priority_queue(frequency)
        tree = build_tree_from_queue(pq)
        code = generate_codes(tree)
        result = encode("ABBA", code)
        expected = "0110"
        self.assertEqual(result, expected)

    def test_decode(self):
        frequency = count_frequency("ABBA")
        pq = create_priority_queue(frequency)
        tree = build_tree_from_queue(pq)
        code = generate_codes(tree)
        encoded = encode("ABBA", code)
        result = decode(encoded, tree)
        expected = "ABBA"
        self.assertEqual(result, expected)
    
    def test_decode_again(self):
        frequency = count_frequency("supercalifragilisticexpialidocious")
        pq = create_priority_queue(frequency)
        tree = build_tree_from_queue(pq)
        code = generate_codes(tree)
        encoded = encode("supercalifragilisticexpialidocious", code)
        result = decode(encoded, tree)
        expected = "supercalifragilisticexpialidocious"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
