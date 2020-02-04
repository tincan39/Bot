class UrlList:

    def __init__(self):
        self.uList = []

    # adds a link to the list and removes the oldest one if it exceeds 500
    def add_elem(self, emb_list: list):
        if len(self.uList) > 500:
            self.uList.pop(0)
        self.uList.extend(emb_list)

    def last_5(self):
        return self.uList[0:5]

    # returns a specified number of urls
    def get_n_elem(self, num: int) -> list:
        if num > len(self.uList):
            raise IndexError("That number exceeds the amount of urls")
        return self.uList[0:num]

    # returns urls by its extension type
    def get_by_ext(self, num: int, ext: str):
        val_links = [x for x in self.uList if x.endswith(ext)]
        return val_links[0:num]
