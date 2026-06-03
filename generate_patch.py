#!/usr/bin/env python#!/usr/bin/env python3

# 计算正确的跳转字节序列
# Thumb-2 B.W 指令

def encode_bw(src, dst):
    # src: 源地址
    # dst: 目标地址
    # 返回4#!/usr/bin/env python3

# 计算正确的跳转字节序列
# Thumb-2 B.W 指令

def encode_bw(src, dst):
    # src: 源地址
    # dst: 目标地址
    # 返回4字节的机器码
    
    offset = dst - (src + 4)
    print(f"源: 0x{src:x}")
    print(f"目标: 0#!/usr/bin/env python3

# 计算正确的跳转字节序列
# Thumb-2 B.W 指令

def encode_bw(src, dst):
    # src: 源地址
    # dst: 目标地址
    # 返回4字节的机器码
    
    offset = dst - (src + 4)
    print(f"源: 0x{src:x}")
    print(f"目标: 0x{dst:x}")
    print(f"偏移: 0x{offset:x}")
    
    imm = offset >> 1
    print(f"立即数: 0x{imm:x}")
    
    # 分解#!/usr/bin/env python3

# 计算正确的跳转字节序列
# Thumb-2 B.W 指令

def encode_bw(src, dst):
    # src: 源地址
    # dst: 目标地址
    # 返回4字节的机器码
    
    offset = dst - (src + 4)
    print(f"源: 0x{src:x}")
    print(f"目标: 0x{dst:x}")
    print(f"偏移: 0x{offset:x}")
    
    imm = offset >> 1
    print(f"立即数: 0x{imm:x}")
    
    # 分解立即数
    S = (imm >> 23) & 1
    J1 = 1 - (((imm >> 22) & 1) ^ S)
    J2 = 1 - (((imm >>#!/usr/bin/env python3

# 计算正确的跳转字节序列
# Thumb-2 B.W 指令

def encode_bw(src, dst):
    # src: 源地址
    # dst: 目标地址
    # 返回4字节的机器码
    
    offset = dst - (src + 4)
    print(f"源: 0x{src:x}")
    print(f"目标: 0x{dst:x}")
    print(f"偏移: 0x{offset:x}")
    
    imm = offset >> 1
    print(f"立即数: 0x{imm:x}")
    
    # 分解立即数
    S = (imm >> 23) & 1
    J1 = 1 - (((imm >> 22) & 1) ^ S)
    J2 = 1 - (((imm >> 21) & 1) ^ S)
    imm10 = (imm >> 11) & 0x3ff
    imm11 = imm & 0x#!/usr/bin/env python3

# 计算正确的跳转字节序列
# Thumb-2 B.W 指令

def encode_bw(src, dst):
    # src: 源地址
    # dst: 目标地址
    # 返回4字节的机器码
    
    offset = dst - (src + 4)
    print(f"源: 0x{src:x}")
    print(f"目标: 0x{dst:x}")
    print(f"偏移: 0x{offset:x}")
    
    imm = offset >> 1
    print(f"立即数: 0x{imm:x}")
    
    # 分解立即数
    S = (imm >> 23) & 1
    J1 = 1 - (((imm >> 22) & 1) ^ S)
    J2 = 1 - (((imm >> 21) & 1) ^ S)
    imm10 = (imm >> 11) & 0x3ff
    imm11 = imm & 0x7ff
    
    print(f"S={S}, J1={J1}, J2={J2}")
    print(f"imm10=0x{imm10:x}, imm11=0x{imm11