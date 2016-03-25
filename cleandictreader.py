import csv

class CleanDictReader(csv.DictReader):
    def clean(self, val):
        val = val.replace('~', '')
        val = val.replace('?', '')
        return val

    @property
    def fieldnames(self):
        return [self.clean(field) for field in csv.DictReader.fieldnames.fget(self)]

    def next(self):
        d = csv.DictReader.next(self)
        return {self.clean(key) : self.clean(d[key]) for key in d.keys()}