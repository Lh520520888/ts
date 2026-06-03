#!/usr/bin/env python3

def calculate_thumb_b(addr_from, addr_to):
    # 计算 Thumb-16 位 B 指令
    offset = (addr_to - (addr_from + 4)) // 2
    # 指令格式：0b1101cccccccccccc（条件为EQ时是0xdxxx）
    # 无条件 B 指令：0b11100xxxxxxxxx → 0xe0xx
    imm = offset & 0xff
    print(f"从 0x{addr_from:x} 跳转到 0x{addr_to:x}")
    print(f"偏移量 (÷2): 0x{imm:x} = {imm}")
    instruction = 0xe000 | imm
    # 小端序存储
    byte1 = (instruction >> 0) & 0xff
    byte2 = (instruction >> 8) & 0xff
    print(f"指令机器码: 0x{instruction:04x} → 小端序: 0x{byte1:02x} 0x{byte2:02x}")
    return (byte1, byte2)

print("=== 位置1: setHandCard13 (0x27a238) ===")
print("目标: 不管条件，直接去 showAllCard13 (0x27a244)")
b1a, b1b = calculate_thumb_b(0x27a238, 0x27a244)
print()

print("=== 位置2: setHandCard (0x27ac5e) ===")
print("目标: 不管条件，直接去 showAllCard (0x27ac62)")
b2a, b2b = calculate_thumb_b(0x27ac5e, 0x27ac62)
