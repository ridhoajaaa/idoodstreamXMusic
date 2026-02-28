# Patch Location.__init__() bug in pyrogram
import os

files = [
    '/usr/local/lib/python3.12/site-packages/pyrogram/types/inline_mode/inline_query.py',
    '/usr/local/lib/python3.12/site-packages/pyrogram/types/inline_mode/chosen_inline_result.py',
]

for f in files:
    if not os.path.exists(f):
        continue
    content = open(f).read()
    if 'client=client' in content:
        import re
        content = re.sub(r'location=types\.Location\(.*?client=client\s*\)', 
            lambda m: m.group(0).replace(',\n                client=client', '').replace(', client=client', ''),
            content, flags=re.DOTALL)
        open(f, 'w').write(content)
        print(f'[PATCH] Patched: {f}')
    else:
        print(f'[PATCH] Already clean: {f}')
