import hashlib

from hashlib_data import lorem

h = hashlib.md5()

h.update(lorem.encode('utf-8'))

all_at_ounce = h.hexdigest()

def chunkize(size, text):
    start = 0
    while start < len(text):
        chunk = text[start:start + size]
        yield chunk
        start += size
    return

h = hashlib.md5()
for chunk in chunkize(64, lorem.encode('utf-8')):
    h.update(chunk)
line_by_line = h.hexdigest()

print('All at once  :', all_at_ounce)
print('Line by line :', line_by_line)
print("Same         :", (all_at_ounce == line_by_line))