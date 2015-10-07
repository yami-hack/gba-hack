
/*
游戏数据,链接库,的位置

*/


SECTIONS
{
	
	. = 0x08000000;
	.rom (COPY):
	{
		KEEP (*rom*.o(.text))
	}
	
}
