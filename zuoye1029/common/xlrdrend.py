import xlrd
class Read():
    def __init__(self,xpath):
        self.xpath=xpath
    def read(self):
        b = xlrd.open_workbook(self.xpath)
        s = b.sheet_by_index(0)
        s1 = s.nrows
        d = []
        for i in range(s1):
            s2 = s.row_values(i)
            d.append(s2)
        return d