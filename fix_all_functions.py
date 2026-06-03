#!/usr/bin/env python3

def calculate_b_instruction(src_addr, dst_addr):
    offset = dst_addr - (src_addr + 4)
    imm = offset >> 1
    S = (imm >> 23) & 1
    J1 = ((imm >> 22) & 1) ^ (1 - S)
    J2 = ((imm >> 21) & 1) ^ (1 - S)
    imm10 = (imm >> 11) & 0x3ff
    imm11 = imm & 0x7ff
    
    hw1 = 0xf000
    hw1 |= (S << 10)
    hw1 |= imm10
    
    hw2 = 0xb000
    hw2 |= ((J1 & 1) << 13)
    hw2 |= ((J2 & 1) << 11)
    hw2 |= imm11
    
    bytes1 = hw1.to_bytes(2, 'little')
    bytes2 = hw2.to_bytes(2, 'little')
    return bytes1 + bytes2

def main():
    # 目标函数 showAllCard 地址
    show_all_card_addr = 0x279d38
    
    # 所有要修改的显示背面牌的函数
    functions = [
        ("showStartCard", 0x279918),
        ("showBackCard", 0x27ac94),
        ("showBackCard13", 0x2787e8),
        ("showALLBackCard", 0x278a60),
        ("showALLBackCard13", 0x278bac),
        ("showSmallBackCard", 0x278cf8),
    ]
    
    print("=" * 60)
    print("📋 拼三张游戏 - 需要修改的所有位置")
    print("=" * 60)
    print("目标：所有显示背面牌的函数都跳转到显示正面 (showAllCard)")
    print(f"showAllCard 地址: 0x{show_all_card_addr:08x}")
    print()
    
    for name, addr in functions:
        instruction = calculate_b_instruction(addr, show_all_card_addr)
        print(f"📍 {name}")
        print(f"   位置: 0x{addr:08x}")
        print(f"   改为: {instruction.hex(' ', 2)}")
        print()
    
    print("=" * 60)
    print("📝 MT管理器操作步骤：")
    print("1. 对于上面列出的每一个地址")
    print("2. 跳到该位置，把前4个字节改成上面写的十六进制值")
    print("3. 保存，重新打包签名安装")
    print("=" * 60)

if __name__ == '__main__':
    main()
