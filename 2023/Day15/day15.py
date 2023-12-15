from Helpers.DataHelper import DataHelper

data = DataHelper(2023, 15).get_data()[0]
# data = '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''
data = data.split(",")

#------------------ Part 1 ------------------#

def hash(step):
    val = 0
    for char in step:
        val += ord(char)
        val *= 17
        val %= 256
    return val

res = list(map(hash, data))
solution = sum(res)
print("Solution 1: ", solution)

#------------------ Part 2 ------------------#

def configure(data):
    boxes = {}
    for step in data:
        if '=' in step:
            key, val = step.split("=")
            label = hash(key)
            if not label in boxes:
                boxes[label] = {key: int(val)}
            else:
                if not key in boxes[label]:
                    boxes[label][key] = int(val)
                else:
                    boxes[label][key] = int(val)
        else:
            key = step[:-1]
            label = hash(key)
            if not label in boxes:
                continue    
            else:
                if not key in boxes[label]:
                    continue    
                else:
                    boxes[label].pop(key)
                    
    strength = 0
    for i, box in boxes.items():
        for j, val in enumerate(box.values()):
            strength += (i + 1) * (j + 1) * val
    return strength

print("Solution 2: ", configure(data))