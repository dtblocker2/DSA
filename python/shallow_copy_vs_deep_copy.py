#shallow copy
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0][0] = 99
print(original,shallow)  # Output: [[99, 2], [3, 4]]

#deep copy
import copy
deep = copy.deepcopy(original)
deep[0][0] = 100
print(original,deep)  # Output: [[99, 2], [3, 4]]
