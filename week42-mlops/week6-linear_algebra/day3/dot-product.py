#The dot product combines two vectors and produces one number.
import numpy as np
A = [2, 3, 4]
B = [5, 6, 7]

print(np.dot(A , B))


import numpy as np

A = np.array([2, 3, 4]) # type: ignore
B = np.array([5, 6, 7]) # type: ignore

result = np.dot(A, B)

print(result)
result = A @ B

print(result)


#features → model → prediction

import numpy as np

A = np.array([ # type: ignore
    [1, 2],
    [3, 4]
])

B = np.array([ # type: ignore
    [5, 6],
    [7, 8]
])

C = A @ B

print(C)

#Matrix multiplication is not just math for AI. It is one of the fundamental operations used inside neural networks.


















