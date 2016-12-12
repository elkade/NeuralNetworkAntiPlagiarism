class AtomizerMock(object):

    def atomize(self, text):
        return [
            {'ratio': 0, 'text': 'abc', 'index': 12443},
            {'ratio': 0.25, 'text': 'def', 'index': 41243},
            {'ratio': 0.33, 'text': 'ghi', 'index': 12243},
            {'ratio': 0.5, 'text': 'jkl', 'index': 91243},
            {'ratio': 0.67, 'text': 'mno', 'index': 12413},
            {'ratio': 0.75, 'text': 'pqr', 'index': 12343},
            {'ratio': 1, 'text': 'stu', 'index': 12432},
            ]