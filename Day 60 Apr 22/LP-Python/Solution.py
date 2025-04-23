class LinearProbingHashST:
    def __init__(self):
        self.cap = 4
        self.len = 0
        self.siz = self.cap
        self.key = [None] * self.siz
        self.val = [None] * self.siz

    def is_empty(self):
        return self.len == 0

    def size(self):
        return self.len

    def get(self, inp_key):
        idx = hash(inp_key) % self.siz
        while self.key[idx] != None:
            if self.key[idx] == inp_key:
                return self.val[idx]
            idx = (idx + 1) % self.siz
        return None

    def put(self, inp_key, inp_val):
        if self.len >= self.siz // 2:
            self.resize(2 * self.siz)

        idx = hash(inp_key) % self.siz
        while self.key[idx] != None:
            if self.key[idx] == inp_key:
                self.val[idx] = inp_val
                return
            idx = (idx + 1) % self.siz

        self.key[idx] = inp_key
        self.val[idx] = inp_val
        self.len += 1

    def contains(self, chk_key):
        return self.get(chk_key) != None

    def delete(self, del_key):
        if not self.contains(del_key):
            return

        idx = hash(del_key) % self.siz
        while self.key[idx] != del_key:
            idx = (idx + 1) % self.siz

        self.key[idx] = None
        self.val[idx] = None
        self.len -= 1

        idx = (idx + 1) % self.siz
        while self.key[idx] != None:
            tmp_key = self.key[idx]
            tmp_val = self.val[idx]
            self.key[idx] = None
            self.val[idx] = None
            self.len -= 1
            self.put(tmp_key, tmp_val)
            idx = (idx + 1) % self.siz

        if 0 < self.len <= self.siz // 8:
            self.resize(self.siz // 2)

    def keys_iter(self):
        a = [k for k in self.key if k != None]
        return a

    def resize(self, new_siz):
        new_tab = LinearProbingHashST()
        new_tab.siz = new_siz
        new_tab.key = [None] * new_siz
        new_tab.val = [None] * new_siz
        new_tab.len = 0

        for idx in range(self.siz):
            if self.key[idx] != None:
                new_tab.put(self.key[idx], self.val[idx])

        self.key = new_tab.key
        self.val = new_tab.val
        self.siz = new_tab.siz
