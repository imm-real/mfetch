import re

def skip_ansi(text: str):
    match = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return match.sub('', text)

def frame(text: str, width: int):
    lines = text.split('\n')
    new_text = f" ┏━ mfetch {'━'*(width-9)}┓\n"
    for line in lines:
        new_text += f" ┃ {line}{' '*(width-(len(skip_ansi(line))+2))} ┃\n"
    new_text += f" ┗{'━'*width}┛"
    return new_text
