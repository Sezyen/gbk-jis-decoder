# gbk-jis-decoder


# Shift-JIS → GBK 乱码还原工具

将因编码误读（Shift-JIS 误解析 GBK ）产生的乱码还原为正确文本。

## 功能

- 逐字符尝试 GBK 编码 → Shift_JIS / Shift_JISx0213 解码
- 无法还原的字符原样保留
- 输出还原后的文本及其 UTF-8 字节序列

## 使用方法

```bash
python jis-cvt2.py
