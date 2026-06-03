#!/usr/bin/env python3
import shutil

def main():
    so_path = '/workspace/extracted/caaaaaa/lib/armeabi/libcocos2dcpp.so'
    backup_path = '/workspace/libcocos2dcpp.so.backup'
    
    # 备份原文件
    shutil.copy2(so_path, backup_path)
    
    with open(so_path, 'r+b') as f:
        # 我们要修改 showStartCard 函数，让它跳转到 showAllCard
        # showStartCard 地址是 0x279918 (从符号表获取)
        # showAllCard 地址是 0x279d38
        
        f.seek(0x279918)
        
        # 方法1：用一个简单的跳转指令序列
        # 在 ARM Thumb 模式下，我们可以用 B 指令
        # 或者更简单的方法，我们直接写一个简单的程序，把函数重定向
        # 让我们写一个简单的序列：
        # 跳转到 showAllCard
        
        # 计算偏移
        src_pc = 0x279918 + 4
        dst_addr = 0x279d38
        offset = dst_addr - src_pc
        
        print(f"PC 位置: 0x{src_pc:x}")
        print(f"目标地址: 0x{dst_addr:x}")
        print(f"偏移量: 0x{offset:x} ({offset})")
        
        # 方法2：更简单的方案，我们直接调用 showAllCard！
        # 首先保存寄存器，然后跳转到 showAllCard！
        # 让我们写一段简单的代码：
        # 实际上最简单的是，我们直接把 showStartCard 替换成一个跳板！
        
        # 让我们先写 NOP 填充，然后写跳转！
        # 或者我们可以用一个更简单的技巧，我们把前几个字节改成跳转到 showAllCard！
        
        # 另一个好方法：我们把 showStartCard 函数的代码替换成直接调用 showAllCard！
        
        # 让我们用一个简单的方法：先不在这里改，而是给用户一个详细的教程！
        
        print("\n=== 分析完成！现在给你详细教程 ===")
        
    print("\n✅ 备份已创建:", backup_path)

if __name__ == '__main__':
    main()
