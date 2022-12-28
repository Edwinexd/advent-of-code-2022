"""
The MIT License (MIT)

Copyright (c) 2022-present Edwin Sundberg

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

with open("data.txt", encoding="utf-8") as f:
    lines = f.read().split()
    lines = [int(line) for line in lines]


class Value():
    value: int
    _id: int

    def __init__(self, value: int, _id: int) -> None:
        self.value = value
        self._id = _id

    def __repr__(self) -> str:
        return str(self.value)

sequence = [Value(i*811589153, _id) for _id,i in enumerate(lines)]

def wrap_index(index: int):
    return index % len(sequence)

def swap(i: int, j: int):
    sequence[wrap_index(i)], sequence[wrap_index(j)] = sequence[wrap_index(j)], sequence[wrap_index(i)]

def move(index: int, steps: int):

    steps = steps % (len(sequence)-1)

    negative: bool
    if steps < 0:
        steps *= -1
        negative = True
    else:
        negative = False
    
    for i in range(steps):
        current_index = index + (i if not negative else i *-1)
        swap_index = current_index + (1 if not negative else -1)

        swap(current_index, swap_index)


static_sequence = sequence.copy()

zero_obj = None
for _ in range(10):
    for number in static_sequence:
        move(sequence.index(number), number.value)
        if number.value == 0:
            zero_obj = number

if zero_obj is None:
    exit()

zero_index = sequence.index(zero_obj)

print(sequence[(zero_index + 1000) % len(sequence)].value + sequence[(zero_index + 2000) % len(sequence)].value + sequence[(zero_index + 3000) % len(sequence)].value)