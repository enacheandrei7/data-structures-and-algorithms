"""
Implementation of Array data structure in Python
"""
# import array


class Array():
    """Class used to create a new array"""

    def __init__(self) -> None:
        """Class constructor"""
        self.length = 0
        self.data = {}

    def __str__(self) -> str:
        """String representation of the class"""
        return str(self.__dict__)

    def get(self, index):
        """Gets the element on the position with the value of index"""
        return self.data[index]

    def push(self, item):
        """Adds an element to the end of the array"""
        self.data[self.length] = item
        self.length+=1

    def pop(self):
        """Removes and returns the last element of the array"""
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length-=1
        return last_item

    def delete(self, index):
        """Deletes the elemend on the position with the value of index"""
        deleted_item = self.data[index]

        if index == self.length - 1:
            del self.data[self.length - 1]
            self.length -= 1
        else:
            for i in range(index, self.length-1):
                self.data[i] = self.data[i + 1]

        del self.data[self.length - 1]
        self.length-=1
        return deleted_item


first_arr = Array()
first_arr.push('hi')
first_arr.push('this')
first_arr.push('is')
first_arr.push('a')
first_arr.push('delete this!')
first_arr.push('story')
first_arr.push('about')
first_arr.push('how')
print(first_arr)
print('Deleted element: ', first_arr.delete(4))
print(first_arr)
x = first_arr.pop()
print('Popped item: ', x)
print(first_arr)


# Python built-in module
# new_array = array.array('i', [10, 20, 30])
# print("Array with built-in module: ", new_array)
# print("Length: ", len(new_array))
