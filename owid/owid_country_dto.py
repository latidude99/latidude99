class OwidCountryDTO:

    def __init__(self, name, label, flag, data, values, labels):
        self.name = name
        self.label = label
        self.flag = flag
        self.data = data
        self.values = values
        self.labels = labels


    def __str__(self):
        return self.name
