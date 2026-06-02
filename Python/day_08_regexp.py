import re

text = "this is only the text to try"


match = re.search(r"only", text, re.IGNORECASE)


if match:
    print("Match found!")
    print("start index:", match.start())
    print("end index:", match.end())







