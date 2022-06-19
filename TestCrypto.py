import hashlib
md5hasher = hashlib.md5(b'alice')
print(md5hasher.hexdigest())