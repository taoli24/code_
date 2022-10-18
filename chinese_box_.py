class ChineseBox:
    inner_box_count = 0

    def __init__(self, inner_box=None):
        self.inner_box = inner_box

    def get_number_inner_box(self):
        if self.inner_box is not None:
            self.update_count()
            self.inner_box.get_number_inner_box()

        return self.return_count()

    @classmethod
    def return_count(cls):
        return cls.inner_box_count

    @classmethod
    def update_count(cls):
        cls.inner_box_count += 1


print(ChineseBox(ChineseBox(ChineseBox(ChineseBox(ChineseBox(ChineseBox()))))).get_number_inner_box())
