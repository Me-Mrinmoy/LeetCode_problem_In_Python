from collections import defaultdict

class Solution:
    def findDuplicate(self, paths):
        content_map = defaultdict(list)

        for entry in paths:
            parts = entry.split()
            directory = parts[0]
            for file_info in parts[1:]:
                name, content = file_info.split('(')
                content = content[:-1]  # remove trailing ')'
                full_path = "{}/{}".format(directory, name)
                content_map[content].append(full_path)

        return [group for group in content_map.values() if len(group) > 1]
