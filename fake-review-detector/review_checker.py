class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_review = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, review):
        node = self.root
        for char in review:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_review = True

    def search(self, review):
        node = self.root
        for char in review:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.is_end_of_review

# Initialize Trie with spam templates
spam_trie = Trie()
spam_templates = [
    "Great product! Highly recommend!",
    "Worst experience ever!",
    "This is a must-buy!"
]

for template in spam_templates:
    spam_trie.insert(template.lower())

def detect_template_review(review):
    return spam_trie.search(review.lower())
