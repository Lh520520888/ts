#!/usr/bin/env python3
import subprocess
import sys

def main():
    so_path = '/workspace/extracted/caaaaaa/lib/armeabi/libcocos2dcpp.so'
    cmd = ['arm-linux-gnueabi-objdump', '-T', so_path]
    try:
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
        # 提取所有相关函数
        keywords = ['Card', 'Show', 'Show', 'show', 'card', 'SSS', 'ZJH', 'NN']
        lines = result.split('\n')
        card_lines = []
        sss_lines = []
        for line in lines:
            if any(k in line for k in keywords):
                if 'SSS' in line:
                    sss_lines.append(line)
                card_lines.append(line)
        print("=== 拼三张(SSS)所有相关函数 ===")
        for line in sorted(sss_lines):
            print(line)
        print("\n=== 所有与牌相关函数（前100个）===")
        for line in sorted(card_lines)[:100]:
            print(line)
    except Exception as e:
        print("Error:", e)
        
if __name__ == '__main__':
    main()
