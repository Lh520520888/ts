#!/usr/bin/env python3

def read_bytes(file_path, offset, length):
    with open(file_path, 'rb') as f:
        f.seek(offset)
        return f.read(length)

def main():
    so_path = '/workspace/extracted/caaaaaa/lib/armeabi/libcocos2dcpp.so'
    
    print("=== 查看 OnSubSendCard (0x270818) 中的关键调用 ===")
    data = read_bytes(so_path, 0x270818, 500)
    
    # 我们找一下 bl 指令（调用函数）
    # BL 指令在 Thumb-2 中是 0b11110xxxxxxxxx0 11xJ2x11xxxxxxxxx
    
    print("\n关键符号地址:")
    print(f"showStartCard: 0x279918")
    print(f"showAllCard: 0x279d38") 
    print(f"setHandCard13: 0x27a220")
    print(f"showAllCard13: 0x27a020")
    print(f"showBackCard13: 0x27??? (让我们找一下)")
    
    # 让我们先列出所有 SSS 相关的符号！
    print("\n让我们找一下更多 SSS 相关函数！")
    
if __name__ == '__main__':
    main()
