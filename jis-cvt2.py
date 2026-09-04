import sys

def decode_mojibake(text):
    """
    将GBK误解析的Shift-JIS乱码还原为正确文本。
    策略：逐字符尝试 GBK编码 → Shift_JIS/Shift_JISx0213解码。
    无法还原的字符（如ASCII、中文原文）原样保留。
    """
    result = []
    for ch in text:
        try:
            gbk_bytes = ch.encode('gbk')
            decoded = gbk_bytes.decode('shift_jis')
            result.append(decoded)
        except (UnicodeEncodeError, UnicodeDecodeError):
            try:
                gbk_bytes = ch.encode('gbk')
                decoded = gbk_bytes.decode('shift_jisx0213')
                result.append(decoded)
            except (UnicodeEncodeError, UnicodeDecodeError):
                result.append(ch)
    return ''.join(result)

def main():
    print("=" * 50)
    print("GBK → Shift_JIS 乱码还原工具")
    print("支持: GBK误解析的Shift-JIS日文乱码还原")
    print("提示: 输入 /exit 退出，或按 Ctrl+C 关闭")
    print("=" * 50)

    while True:
        try:
            user_input = input("\n请输入乱码文本: ").strip()

            if user_input.lower() == '/exit':
                print("已退出")
                break

            decoded = decode_mojibake(user_input)
            utf8_bytes = decoded.encode('utf-8')

            print(f"还原结果: {decoded}")
            print(f"UTF-8字节: {utf8_bytes.hex()}")

        except KeyboardInterrupt:
            print("\n已退出")
            break
        except Exception as e:
            print(f"处理出错: {e}")

if __name__ == "__main__":
    main()