# HACK_DATA
## item_data.c
  * 这个数据文件是从ROM里面导出来的,用编译工具arm-none-eabi-gcc 生成.o文件,再与rom2asm链接,链接脚本在ldscript/romhack.ld, 汇编文件后缀名 name.rom.s   里面有关item_data都是弱符号(weak symbol).
