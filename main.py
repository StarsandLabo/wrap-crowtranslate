import re, subprocess

def TranslateByCrowtranslate(input_text, inner=False, display=False):
    res_array = []
    for line in input_text.split("\n"):
        if len(line) == 0 or re.match(r'^\s*$',line): pass 
        else:
            output = subprocess.run(['crow', '-t',  'ja', f"{line}"], capture_output=True, text=True)
            for i, result in enumerate(output.stdout.split("\n")):
                res_array.append(f'in : {result}\n') if i == 0 else \
                res_array.append(f'out: {result}\n') if i == 4 else \
                None
            res_array.append('\n')
    return res_array
