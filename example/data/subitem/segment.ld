
/*
段布局
*/


SECTIONS
{
	. = 0x09000000;
	.hackinfo : 
	{
		KEEP (*(.hackinfo))
	}
	
	. = 0x09000400;
	.text : 
	{
		*(.text);
	} 
	

	
	.rodata :
	{
		KEEP (*(EXCLUDE_FILE (data_*.o) .rodata))
		KEEP (*(.rodata))
		. = ALIGN(4);
	} 
	
	/*
	.ewram : 
	{
		. = 0x3FFFF;
	} >ewram
	
	.iwram : 
	{
		. = 0x7FFF;
	} >iwram
	
	
	.ioram : 
	{
		INCLUDE "gbaio.ld"
		. = 0x400;
	} >ioram

	
	.palram : 
	{
		. = 0x400;
	} >palram
	

	.vram : 
	{
		. = 0x17fff;
	} >vram
	

	.oam : 
	{
		. = 0x400;
	} >OAMram
	*/
}
