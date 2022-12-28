
"""
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
    lines = f.read().split("\n")

monkeys = {i[0]:i[1] for i in (line.split(": ") for line in lines)}

def get_monkey_value(name: str) -> int:
    monkey = monkeys[name]
    if any(i in monkey for i in ("*", "+", "-", "/")):
        operator = monkey.split(" ")[1]
        left, right = monkey.split(f" {operator} ")
        left, right = get_monkey_value(left), get_monkey_value(right)
        if operator == "*":
            return left * right
        elif operator == "+":
            return left + right
        elif operator == "-":
            return left - right
        elif operator == "/":
            return left // right
    return int(monkey)


print(monkeys["root"])
print(get_monkey_value("root"))