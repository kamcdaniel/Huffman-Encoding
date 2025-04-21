[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/rm9PziGW)
# Huffman Encoding

## Overview
Project3 of CSC202 (Data Structures) is an implementation of Huffman Encoding, a widely used method for data compression. This project includes a detailed exploration of the Huffman encoding process, from frequency counting to tree construction and binary encoding/decoding. Special emphasis is placed on the `Node` and `MinHeap` classes provided, which are pivotal in constructing the Huffman tree and managing the priority queue, respectively.

## Features
- **Frequency Counting:** Analyzes the frequency of each character in the input string.
- **Priority Queue:** Utilizes a MinHeap to maintain the characters sorted by their frequencies.
- **Huffman Tree Construction:** Builds a Huffman tree based on character frequencies.
- **Encoding and Decoding:** Generates binary codes for characters and decodes them back to the original string.

## Tasks
Complete the implementation of the following functions:

1. **`create_priority_queue(frequency: dict[str, int]) -> MinHeap`**:
   - Complete the implementation to accept a frequency dictionary, create nodes for each character and its frequency, and insert them into a priority queue (MinHeap).

   - With the frequency dictionary in hand, create a priority queue that organizes the characters based on their frequencies. This step is crucial for building the Huffman tree and is accomplished by invoking `create_priority_queue`, which returns a `MinHeap` filled with `Node` objects for each character.

2. **`build_tree_from_queue(priority_queue: MinHeap) -> Node`**:
   - Complete the function to construct the Huffman tree from the provided priority queue.

   - Construct the Huffman tree from the priority queue by calling `build_tree_from_queue`. This function iteratively combines the nodes with the least frequencies into new nodes until a single node remains, representing the root of the Huffman tree.

3. **`generate_codes(node: Node | None, prefix="", code: dict | None = None) -> dict`**:
   - Implement the function to traverse the Huffman tree and generate Huffman codes for each character.

   - Generate the Huffman codes for each character by traversing the newly constructed Huffman tree. The `generate_codes` function accomplishes this, returning a dictionary where each character is mapped to its corresponding binary code.

4. **`decode(encoded_string: str, root: Node)`**:
   - Implement this function to decode an encoded string using the provided Huffman tree, utilizing a purely functional manner and tracking position in the string using an index.

   - Decode the binary string back into its original text form to verify the accuracy of the Huffman encoding process. This is achieved through the `decode` function, which utilizes the Huffman tree to interpret the binary sequence back into text.

