#creating array
import array as arr
a = arr.array('i', [1,2,3])
print("newly created array: ", end=" ")
for i in range (0,3):
    print(a[i], end=" ")
print()
b = arr.array('d', [2.5, 3.2, 3.3])
print("newly created array: ", end=" ")
for i in range(0,3):
    print(b[i], end=" ")
print()

#inserting in array
import array as arr
a = arr.array('i', [1,2,3])
print("newly created array: ", end=" ")
for i in range (0,3):
    print(a[i], end=" ")
print()
a.insert(1,4)
print("Array after insertion: ", end=" ")
for i in range (0,4):
    print(a[i], end=" ")

#methods of array
import array as arr

a = arr.array('i', [1, 2, 3])
print("Original array: ", end="")
for x in a:
    print(x, end=" ")
print()

a.append(4)
print("After append(4): ", end="")
for x in a:
    print(x, end=" ")
print()

a.insert(1, 5)
print("After insert(1, 5): ", end="")
for x in a:
    print(x, end=" ")
print()

a.extend([6, 7, 8])
print("After extend([6, 7, 8]): ", end="")
for x in a:
    print(x, end=" ")
print()

a.fromlist([9, 10])
print("After fromlist([9, 10]): ", end="")
for x in a:
    print(x, end=" ")
print()

print("Element at index 2:", a[2])
print("Index of value 5:", a.index(5))
print("Count of value 3:", a.count(3))
print()

a[0] = 99
print("After updating index 0 to 99: ", end="")
for x in a:
    print(x, end=" ")
print()

popped_val = a.pop(2)
print("Popped value at index 2:", popped_val)
print("After pop(2): ", end="")
for x in a:
    print(x, end=" ")
print()

a.remove(99)
print("After remove(99): ", end="")
for x in a:
    print(x, end=" ")
print()

a.reverse()
print("After reverse(): ", end="")
for x in a:
    print(x, end=" ")
print()

py_list = a.tolist()
print("Converted to list:", py_list)
print()

print("Typecode:", a.typecode)
print()
print("Item size in bytes:", a.itemsize)
print()
print("Buffer info (address, length):", a.buffer_info())
print()

b = arr.array('i')
b.frombytes(a.tobytes())
print("Recreated array from bytes: ", end="")
for x in b:
    print(x, end=" ")
print()

del b[:]
print("Length of b after clearing with del b[:]:", len(b))