SECTIONS{
	. = 0x0800A240;
	.0800A240 : 
	{
		*.o(.0800A240)
	}
	/* . = ALIGN(10); */	 /*这不是必须的*/
}
INCLUDE segment.ld  		/*如果没有这个文件，数据会被初始化在 .0800A240 + sizeof(sub_0800A240)  地址后面 */
