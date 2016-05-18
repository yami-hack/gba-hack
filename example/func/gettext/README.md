
这个例子是修改突刺剑的攻击力，具体的看源码item.c

1,首先把FE8(US).gba放到目录

2,打开控制台执行
	bash
	all.sh

3,等待几分钟(时间主要消耗在rom2asm.py上)

4,得到elf，可以用vba-m打开elf文件

5,改动的文件有 
	sub_800A240.c 
	link.ld
	未改动的
	segment.ld
	rom.ld
	romhack.ld
	需要文件
	FE8(US).gba

一,	在所有.sh文件中，都要注释，执行什么命令
	命令基本都是从gnu c doc 中来的
	
二，rom的汇编文件可以用  .incbin "xxx.gba"
	我没有做过类似的例子，所以不知道正确性
	
三，这个例子同样适用指针
	__attribute__ ((section(".08000000")))
	const void*	xx_ptr = &data;		//int data[];  [0x08000000] = &data;
	
四，同样使用于函数修改
	__attribute__ ((section(".08000000")))
	sub_xxxx(){};					//address = 08000000
	但是，该函数替换rom中的函数时，必须小于原始函数，所以一般用
	__attribute__ ((section(".08000000")))
	sub_xxxx(){  asm_call(sub_xxxx_hack);};			//#define asm_call(func)  {asm("bx %1":"r"(func));} 应该有错误，我不擅长记一些东西，具体的看gnu arm 汇编
	sub_xxxx_hack(){...};			//address > 0x9000000  不用设置地址，因为自动适应ROM地址
