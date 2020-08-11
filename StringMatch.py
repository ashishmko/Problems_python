class Finder:
    def __init__(self, list_strings):
        self.result = []
        self.strings = list_strings
        self.hashMap = dict()

    def find(self, input):
        self.result.clear()

        for item in self.strings:
             if len(input) == len(item):
                isEqual = True

                for i in  range(len(input)):
                    if item[i] not in self.hashMap:
                        self.hashMap[item[i]] = 1
                    else:
                        self.hashMap[item[i]] += 1
                    if input[i] not in self.hashMap:
                        self.hashMap[input[i]] = 1
                    else:
                        self.hashMap[input[i]] += 1

                for i in range(len(input)):
                    if (self.hashMap[input[i]]%2) != 0:
                        isEqual = False
                        break

                self.hashMap.clear()

                if isEqual == True:
                    self.result.append(item)

        return self.result




if __name__ == '__main__':

    finder = Finder(['asd', 'sads', 'dsa', 'dass', 'dassa'])

    print(finder.find('sda'))
    print(finder.find('ssad'))
