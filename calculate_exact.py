#!/usr/bin/env python3

def calculate_b_instruction(src_addr, dst_addr):
    # 计算 B.W (32-bit Thumb) 跳转指令
    offset = dst_addr - (src_addr + 4)
    print(f"源地址: 0x{src_addr:08x}")
    print(f"目标地址: 0x{dst_addr:08x}")
    print(f"偏移 (PC相对): 0x{offset:x} = {offset} 字节")
    
    # 编码32位Thumb B.W指令
    imm = offset >> 1
    print(f"立即数(左移前): 0x{imm:x}")
    
    # 分解 imm
    S = (imm >> 23) & 1
    J1 = ((imm >> 22) & 1) ^ (1 - S)
    J2 = ((imm >> 21) & 1) ^ (1 - S)
    imm10 = (imm >> 11) & 0x3ff
    imm11 = imm & 0x7ff
    
    # 构造第一halfword (0b11110xxx...)
    hw1 = 0xf000
    hw1 |= (S << 10)
    hw1 |= imm10
    
    # 构造第二halfword (0b1011xxxx...)
    hw2 = 0xb000
    hw2 |= ((J1 & 1) << 13)
    hw2 |= ((J2 & 1) << 11)
    hw2 |= imm11
    
    # 转换成字节（小端序）
    bytes1 = hw1.to_bytes(2, 'little')
    bytes2 = hw2.to_bytes(2, 'little')
    full_instruction = bytes1 + bytes2
    
    print(f"\n✅ 要修改的前4字节（小端序）：{full_instruction.hex()}")
    print(f"即：位置 0x{src_addr:x} 写入：{full_instruction.hex(' ', 2)}")
    
    return full_instruction

if __name__ == '__main__':
    # 关键地址
    src = 0x279918   # showStartCard 开头
    dst = 0x279d38   # showAllCard 开头
    calculate_b_instruction(src, dst)
