#!/usr/bin/env python3
import shutil

so_path = '/workspace/extracted/caaaaaa/lib/armeabi/libcocos2dcpp.so'
backup_path = '/workspace/libcocos2dcpp.so.backup.final'

shutil.copy2(so_path, backup_path)
print(f"备份已创建: {backup_path}")

def encode_b_thumb(source_addr, target_addr):
    offset = target_addr - (source_addr + 4)
    imm = offset >> 1
    imm10 = (imm >> 11) & 0x3ff
    imm11 = imm & 0x7ff
    S = (imm >> 23) & 1
    J1 = ((imm >> 22) & 1) ^ (1 - S)
    J2 = ((imm >> 21) & 1) ^ (1 - S)
    hw1 = 0xf000 | (S << 10) | imm10
    hw2 = 0xb000 | (J1 << 13) | (J2 << 11) | imm11
    return hw1.to_bytes(2, 'little') + hw2.to_bytes(2, 'little')

# 关键目标地址
target_show_all = 0x279d38  # showAllCard

# 所有需要修改的显示背面/开始的函数
functions = [
    (0x279918, "showStartCard"),
    (0x2787e8, "showBackCard"),
    (0x278a60, "showALLBackCard"),
    (0x278bac, "showALLBackCard13"),
    (0x278cf8, "showSmallBackCard"),
    (0x279b88, "showStartLzCard"),
]

with open(so_path, 'r+b') as f:
    for addr, name in functions:
        try:
            jmp_code = encode_b_thumb(addr, target_show_all)
            f.seek(addr)
            f.write(jmp_code)
            print(f"✅ 修改成功: {name} @ 0x{addr:x} → showAllCard @ 0x{target_show_all:x}")
            print(f"   字节码: {jmp_code.hex()}")
        except Exception as e:
            print(f"❌ 修改失败: {name}: {e}")

print("\n🎉 所有修改完成！现在你可以重新打包并安装测试！")
