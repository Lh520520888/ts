#!/usr/bin/env python3
import struct

def read_bytes(file_path, offset, length):
    with open(file_path, 'rb') as f:
        f.seek(offset)
        return f.read(length)

def main():
    so_path = '/workspace/extracted/caaaaaa/lib/armeabi/libcocos2dcpp.so'
    
    # showStartCard 地址 0x279918
    print("=== showStartCard (0x279918) ===")
    data = read_bytes(so_path, 0x279918, 64)
    for i in range(0, len(data), 4):
        print(f"{0x279918 + i:08x}: {data[i:i+4].hex()} - {data[i:i+4]}")
    
    # showAllCard 地址 0x279d38
    print("\n=== showAllCard (0x279d38) ===")
    data = read_bytes(so_path, 0x279d38, 64)
    for i in range(0, len(data), 4):
        print(f"{0x279d38 + i:08x}: {data[i:i+4].hex()} - {data[i:i+4]}")

if __name__ == '__main__':
    main()
