try:
    import ustruct as struct
except:
    import struct
print(struct.calcsize("<bI"))
print(struct.unpack("<bI", b"\x80\0\0\x01\0"))
print(struct.calcsize(">bI"))
print(struct.unpack(">bI", b"\x80\0\0\x01\0"))

# 32-bit little-endian specific
#print(struct.unpack("bI", b"\x80\xaa\x55\xaa\0\0\x01\0"))

print(struct.pack("<i", 1))
print(struct.pack(">i", 1))
print(struct.pack("<h", 1))
print(struct.pack(">h", 1))
print(struct.pack("<b", 1))
print(struct.pack(">b", 1))

print(struct.pack("<bI", -128, 256))
print(struct.pack(">bI", -128, 256))

print(struct.calcsize("100sI"))
print(struct.calcsize("97sI"))
print(struct.unpack("<6sH", b"foo\0\0\0\x12\x34"))
print(struct.pack("<6sH", b"foo", 10000))

s = struct.pack("BHBI", 10, 100, 200, 300)
v = struct.unpack("BHBI", s)
print(v == (10, 100, 200, 300))

# check maximum pack on 32-bit machine
print(struct.pack("<I", 2**32 - 1))
print(struct.pack("<I", 0xffffffff))

# long long ints
print(struct.pack("<Q", 2**64 - 1))
print(struct.pack("<Q", 0xffffffffffffffff))
print(struct.pack("<q", -1))
print(struct.pack("<Q", 1234567890123456789))
print(struct.pack("<q", -1234567890123456789))
print(struct.pack(">Q", 1234567890123456789))
print(struct.pack(">q", -1234567890123456789))
print(struct.unpack("<Q", b"\x12\x34\x56\x78\x90\x12\x34\x56"))
print(struct.unpack(">Q", b"\x12\x34\x56\x78\x90\x12\x34\x56"))
print(struct.unpack("<q", b"\x12\x34\x56\x78\x90\x12\x34\xf6"))
print(struct.unpack(">q", b"\xf2\x34\x56\x78\x90\x12\x34\x56"))

# check maximum unpack
print(struct.unpack("<I", b"\xff\xff\xff\xff"))
print(struct.unpack("<Q", b"\xff\xff\xff\xff\xff\xff\xff\xff"))

# network byte order
print(struct.pack('!i', 123))