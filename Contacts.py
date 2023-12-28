import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

def contacts(queries):
    root = TrieNode()
    result = []

    def add_contact(contact):
        node = root
        for char in contact:
            node = node.children.setdefault(char,TrieNode())
            node.count += 1

    def find(search):
        node = root
        for char in search:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count
    
    for operation, content in queries:
        if operation == 'add':
            add_contact(content)
        elif operation == 'find':
            result.append(find(content))
    return result

if __name__ == '__main__':

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    print(contacts(queries))

    


