from __future__ import annotations
from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Node:
    freq: int
    char: str
    left: Node | None = None
    right: Node | None  = None

    def __str__(self):
        return f"Node: {self.char}, Freq: {self.freq}"

from dataclasses import dataclass, field

@dataclass(frozen=True)
class MinHeap:
    data: list[Node] = field(default_factory=list)

def heapify_up(heap: MinHeap, index: int) -> MinHeap:
    if index == 0:
        return heap  # Base case: reached the root of the heap
    parent_index = (index - 1) // 2
    heap_data = heap.data
    if heap_data[index] < heap_data[parent_index]:
        new_heap_data = heap_data[:]
        new_heap_data[index], new_heap_data[parent_index] = new_heap_data[parent_index], new_heap_data[index]
        return heapify_up(MinHeap(new_heap_data), parent_index)
    else:
        return heap  # No swap needed, return the heap as is

def insert(heap: MinHeap, element: Node) -> MinHeap:
    new_heap_data = heap.data[:] + [element]
    last_index = len(new_heap_data) - 1
    new_heap = heapify_up(MinHeap(new_heap_data), last_index)
    return new_heap

def heapify_down(heap: MinHeap, index: int) -> MinHeap:
    heap_data = heap.data
    current_size = len(heap_data)
    smallest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < current_size and heap_data[left] < heap_data[smallest]:
        smallest = left

    if right < current_size and heap_data[right] < heap_data[smallest]:
        smallest = right

    if smallest != index:
        new_heap_data = heap_data[:]
        new_heap_data[index], new_heap_data[smallest] = new_heap_data[smallest], new_heap_data[index]
        return heapify_down(MinHeap(new_heap_data), smallest)
    else:
        return heap  # No swap needed, return the heap as is

def extract_min(heap: MinHeap) -> tuple[MinHeap, Node]:
    if not heap.data:
        raise ValueError("Heap is empty")

    min_element = heap.data[0]
    new_heap_data = heap.data[:]
    last_index = len(new_heap_data) - 1
    new_heap_data[0] = new_heap_data[last_index]
    new_heap_data = new_heap_data[:last_index]
    new_heap = heapify_down(MinHeap(new_heap_data), 0)
    return new_heap, min_element


        
def count_frequency(s: str)-> dict[str,int]:
    #Generate a dictionary that will be key: value pairs of
    # char:frequency 
    #return the dictionary
    frequency: dict[str, int] = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


def create_priority_queue(frequency: dict[str, int]) -> MinHeap:
    """
    Accepts a frequency dictionary where the keys are characters (as strings)
    and the values are their corresponding frequencies (as integers).
    Returns a priority queue (MinHeap) filled with nodes where each node represents a character and its frequency.

    Parameters:
    - frequency: dict[str, int]: A dictionary mapping characters to their frequencies.

    Returns:
    - MinHeap: A priority queue where each element is a Node containing a frequency and a character,
               and the elements are ordered by frequency in a min-heap structure.
    """
    priority_queue = MinHeap([])

    for key in frequency:
        character_node = Node(frequency[key], key) #frequency, char, left, right
        priority_queue = insert(priority_queue, character_node)

    return priority_queue


def build_tree_from_queue(priority_queue: MinHeap) -> Node:
    """
    Takes a priority queue (min-heap) and constructs the Huffman tree.
    This priority queue should contain all nodes with their frequencies,
    where each node might represent a character or a previously merged subtree.
    """
    def build_recursive(queue):
        if len(queue.data) == 1:
            return extract_min(queue)[1] 
        
        queue, left = extract_min(queue)
        queue, right = extract_min(queue)

        lower = ""
        if left.char < right.char:
            lower = left.char
        else:
            lower = right.char
        combined = Node(left.freq + right.freq, lower, left, right)

        queue = insert(queue, combined)

        return build_recursive(queue)

    return build_recursive(priority_queue)


def generate_codes(node: Node | None, prefix="", code: dict | None =None)-> dict:
    
    if code is None:
        code = {}  

    if node is None:
        return code
    
    if node.left == None and node.right == None:
        code[node.char] = prefix

    if node.left:
        generate_codes(node.left, prefix + "0", code)
    if node.right:
        generate_codes(node.right, prefix + "1", code)

    return code


def encode(s: str, codes: dict)-> str:
    return ''.join(codes[char] for char in s)


def decode(encoded_string: str, root: Node):
    """
    Decode an encoded string using the provided Huffman tree in a purely functional manner,
    now using an index to track position in the string.
    """
    def decode_recursive(encoded: str, node: Node, root: Node, index: int) -> str:

        if index >= len(encoded):
            return node.char
        
        if node.left == None and node.right == None:
            return node.char + decode_recursive(encoded, root, root, index)

        if encoded[index] == "0":
            node = node.left
        else:
            node = node.right
        
        return decode_recursive(encoded, node, root, index + 1)

    return decode_recursive(encoded_string, root, root, 0)




def huffman_encoding(s:str):

    frequency = count_frequency(s)
    pq = create_priority_queue(frequency)
    root = build_tree_from_queue(pq)
    #print(root)
    codes = generate_codes(root)
    #print(codes)
    #check generate codes!!
    encoded_string = encode(s, codes)
    decoded_string = decode(encoded_string,root)
    return encoded_string, decoded_string, codes


#print(huffman_encoding("hello"))
#print(huffman_encoding("google"))
#print(huffman_encoding("potato"))
