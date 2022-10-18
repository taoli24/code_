class ChineseBox:
    def __init__(self, inner_box=None):
        self.inner_box = inner_box

    def get_number_inner_box(self):
        inner_count = 0
        if self.inner_box is not None:
            inner_count += self.inner_box.get_number_inner_box()
        return inner_count

print(ChineseBox(ChineseBox(ChineseBox(ChineseBox(ChineseBox(ChineseBox()))))).get_number_inner_box())
