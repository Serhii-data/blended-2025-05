'''

This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.

'''

# def accum(string: str) -> str:
#     result = ""
#     for index in range(len(string)):
#         result += (string[index]*(index + 1)).capitalize() + "-"
#     return result[:-1]

def accum(string: str) -> str:
    return "-".join([(symbol * (index + 1)).capitalize() for index, symbol in enumerate(string)])

assert accum("abcd") == "A-Bb-Ccc-Dddd"
assert accum("RqaEzty") == "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
assert accum("cwAt") == "C-Ww-Aaa-Tttt"