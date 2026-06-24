
"""
1. Trie, children - mapping child name to child node
         content - file or None (dir)
    root
    |--- home
    |    --- user
    |           --- file.txt  <- content = 'hello'
    |--- usr  <= content = None
2. `_walk` for ls, mkdir, addContent, readContent, split '/', walk through trie,
  optionally create missing node.
3. `ls` walk to the path, file -> return file name or dir -> return all child in alpha order
    `mkdir`, /a/b/c, walk through path, create missing node
    `addContent`, /a/b/c/d, walks to d, with create=True for missing nodes, append content
    `readContent`, /a/b/c/d, walk to d and read content attribute
4. mkdir('/a/b'): root -> a (create) -> b (create),
   addContentToFile(/a/b/c, hello) -> create c file with content
   ls(/a/b): b content is None, folder, return sorted([c])
5. Time ls O(KlogK + L), L path length, K is children number; Other O(L)
   Space: ls O(#path char + file content)
"""

# Trie
class Node:
    def __init__(self):
        self.content = None
        self.children = {} # {child_name: child_node}


class FileSystem:

    def __init__(self):
        self.root = Node()

    def ls(self, path: str) -> List[str]:
        node = self._walk(path)
        if node.content is None:
            # folder node
            return sorted(node.children.keys())
        else:
            # file node
            return [path.split('/')[-1]]


    def mkdir(self, path: str) -> None:
        self._walk(path, create=True)


    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._walk(filePath, create=True)
        if node.content is None:
            node.content = content
        else:
            node.content += content


    def readContentFromFile(self, filePath: str) -> str:
        return self._walk(filePath).content

    
    def _walk(self, path: str, create: bool = False) -> Node:
        node = self.root
        # edge case for root, no path trasverse
        if path == '/':
            return node
        
        # edge case: "/a" -> ["", 'a']
        for part in path.split('/')[1:]:
            if create and part not in node.children:
                node.children[part] = Node()
            node = node.children[part]
        return node

    
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
