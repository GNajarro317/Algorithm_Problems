class RouteTrieNode:
    def __init__(self, part=None, handler=None):
        # Initialize RouteTrieNode with part and handler
        self.part = part
        self.handler = handler
        self.children = {}

    def insert(self, part, handler=None):
        # Insert a new node with part and handler
        if part not in self.children:
            self.children[part] = RouteTrieNode(part, handler)
        return self.children[part]

class RouteTrie:
    def __init__(self, root_part=None, root_handler=None):
        # Initialize RouteTrie with root part and handler
        self.root = RouteTrieNode(root_part, root_handler)

    def insert(self, path_parts, handler):
        # Insert a path with its parts and handler
        node = self.root
        for part in path_parts:
            node = node.insert(part)
        node.handler = handler

    def find(self, path_parts):
        # Find the handler for a given path
        node = self.root
        for part in path_parts:
            if part not in node.children:
                return None
            node = node.children[part]
        return node.handler

class Router:
    def __init__(self, not_found_handler=None):
        # Initialize the Router with a not found handler
        self.route_trie = RouteTrie('/', not_found_handler)

    def add_handler(self, path, handler):
        # Add a handler for a specific path
        path_parts = self.split_path(path)
        self.route_trie.insert(path_parts, handler)

    def lookup(self, path):
        # Lookup the handler for a given path
        path_parts = self.split_path(path)
        return self.route_trie.find(path_parts)

    def split_path(self, path):
        # Split the path into parts
        if path == '/' or path == '':
            return ['']
        return path.strip('/').split('/')

# Test Case 1: Add and lookup a simple path
router = Router()
router.add_handler('/about/me', 'About Me handler')
print(router.lookup('/about/me'))

# Test Case 2: Add and lookup a path with multiple parts
router.add_handler('/home/index', 'Home Index handler')
print(router.lookup('/home/index'))

# Test Case 3: Lookup a path that doesn't exist
print(router.lookup('/404'))

# Test Case 4: Test handling of trailing slashes
router.add_handler('/about', 'About handler')
print(router.lookup('/about'))

# Test Case 5: Test handling of empty path
print(router.lookup(''))
