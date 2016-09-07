import gauze


class Test(object):
    data = [1,2,3]
    def data_pow(self, pow=2):
        return [i**pow for i in self.data]

Test.data_pow = gauze.patch(Test.data_pow, [("    return [i**pow for i in self.data]", "    return self.data")])
