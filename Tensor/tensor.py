class Tensor():
    def __init__(self, data, shape):
        self.data = data
        self.shape = shape

    def addValue(self):
        data = self.data
        shape = self.shape
        if shape:
            dataCount = 1
            for i in shape:
                dataCount *= i
            if len(data) < dataCount:
                data += [0]*(dataCount-len(data))
            elif len(data) > dataCount:
                data = data[0:dataCount]
        return data

    def shape_data(self):
        data = self.addValue()
        shape = self.shape
        if shape:
            for i in reversed(shape[1:]):
                count = 0
                arrPtr = []
                listPtr = []
                for j in range (0, len(data)):
                    arrPtr.append(data[j])
                    count += 1
                    if count >= i:
                        listPtr.append(arrPtr)
                        arrPtr = []
                        count = 0
                data = listPtr
            return data
        else:
            return []

def main():
    arrNew = [item for item in input("Enter the list items: ").split()]
    arr = []
    for entry in arrNew:
        for convert in [int, float]:
            try:
                entry = convert(entry)
                arr.append(entry)
            except ValueError:
                continue
            break
    shape = [int(item) for item in input("Enter the shape items: ").split()]
    for i in shape:
        if i < 0:
            print("Shape must bigger than 0!")
            shape = [int(item) for item in input("Enter the shape items: ").split()]
    tensor = Tensor(arr, shape)
    print(tensor.shape_data())

if __name__ == "__main__":
    main()

