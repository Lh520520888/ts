#!/usr/bin/env python3

# 目标：在 0x279918 (showStartCard) 写一个跳转到 0x279d38 (showAllCard) 的指令
# 这是 ARM Thumb-2 指令集
# B 指令格式：0b11100xxxxxxxxx... 或者用 32-bit Thumb B.W 指令

def main():
    src_addr = 0x279918
    dst_addr = 0x279d38
    
    print(f"从 0x{src_addr:x} 跳转到 0x{dst_addr:x}")
    
    # 计算相对偏移（注意：PC 是当前地址 + 4 对于 Thumb）
    offset = dst_addr - (src_addr + 4)
    print(f"偏移量: 0x{offset:x} = {offset} 字节")
    
    # 计算 32-bit Thumb B.W 指令
    # B.W 的编码：0b11110xxxxxxxxx0 10xJ2x11xxxxxxxxx
    # 对于正偏移，我们可以计算一下
    if offset >= 0:
        # 24-bit 有符号偏移 (右移 1 位)
        imm = offset >> 1
        print(f"24-bit 立即数: 0x{imm:x}")
        
        # 构造指令：0xF0xx 0xBxxx
        # 更简单的方法是，我们直接用汇编来算，但这里我们有个更简单的方案：
        print("\n更简单的方案：我们直接用 B 指令跳转到目标地址！")
        print("或者我们直接把 showStartCard 的第一条指令替换成跳转到 showAllCard！")
        print("我们可以用一个简单的技巧：")
        print("直接把 showStartCard 的开头替换成跳转到 showAllCard！")

if __name__ == '__main__':
    main()
