//Original data
#if 0			//不需要这个原始的数据
void *sub_800A240__(int id)
{
	int	*old = (int*)0x202B6AC;
	char  *text_buf = (char*)0x202A6AC;
	char	**text_list = (char**)0x815D48C;
	if(*old == id)
		return (void*)text_buf;
	sub_8002BA4(text_list[id],text_buf);			//在rom内跳转，但是现在不需要
	sub_800A1C8(text_buf);							//应该是显示文本
	*old = id;												//已经有了
	return (void*)text_buf;
}
#endif

const
char* new_text_list[0x10] = {};


void *sub_800A240_hack(int id)
{
	int	*old = (int*)0x202B6AC;
	char  *text_buf = (char*)0x202A6AC;
	char	**text_list = (char**)0x815D48C;		// = new_text_list
	if(*old == id)
		return (void*)text_buf;
	/*
	必须使用长跳转    
	sub_8002BA4(text_list[id],text_buf);			//在rom内跳转，但是现在不需要
	sub_800A1C8(text_buf);							//应该是显示文本
	*/
	
	void*	(*f)() = (void*)0x8002BA4 + 1;	// +1  thumb mode
	
	if(((int)text_list[id])&0x80000000)		//0x88xxxxxx
	{
		char *ptr = (void*)((int)text_list[id] & 0x0FFFFFFF);
		char	*dst = text_buf;
		while((*dst++=*ptr++))
		{
		};
	}
	else
	{
		f(text_list[id],text_buf);			//0x08xxxxxx
	};
	
	f	=	(void*)0x800A1C8 + 1;					// +1 thumb mode
	f(text_buf);
	
	*old = id;												//已经有了
	return (void*)text_buf;
}



#define call_1(arg1,f)	({void*l=f;goto *l;0;})			//并不是很合格的函数，外部还需要一个NORETURN
//会生成汇编   ldr r3,=func           bx r3

#define NORETURN		__attribute__((noreturn))

__attribute__ ((aligned (4)))
__attribute__ ((section(".0800A240")))
NORETURN						//这里是为了优化代码 __attribute__((noreturn))
void *sub_800A240(int id)
{
	call_1(id,sub_800A240_hack);
}

