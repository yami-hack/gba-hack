
#define PACKED __attribute__ ((packed))
#define SECTION(name) 	__attribute__ ((section(name)))

typedef unsigned char 	u8;
typedef unsigned short 	u16;
typedef unsigned int 	u32;

typedef signed char  	s8;
typedef signed short 	s16;
typedef signed int 		s32;


typedef struct 
__attribute__ ((packed))   //gnu c扩展，使用最小二进制存储
{
	u16	 u00_;		//道具名称
	u16	 u02_;		//道具描述
	u16	 u04_;		//道具说明
	u8	 u06_;		//核心代码
	u8	 u07_;		//道具类型
	u32	 u08_;		//特殊属性
	u32	 u0C_;		//附加能力指针
	u32	 u10_;		//职业特效指针
	u8	 u14_;		//耐久
	u8	 u15_;		//攻击
	u8	 u16_;		//命中
	u8	 u17_;		//重量
	u8	 u18_;		//必杀
	u8	 u19_;		//射程
	u16	 u1A_;		//单价
	u8	 u1C_;		//等级需求
	u8	 u1D_;		//道具图标
	u8	 u1E_;		//杖／物品效果
	u8	 u1F_;		//武器效果
	u8	 u20_;		//熟练度获得
	u8	 u21_;		//未知
	u8	 u22_;		//未知
	u8	 u23_;		//未知
}Item;


//修改item[0x9] 突刺剑的数据
//???? + (sizeof(Item)*0x9)   =0x809C54;

__attribute__ ((section(".08809C54")))			//gnu c扩展，程序段名  (.address)  必须要在link.ld文件中添加该数据段
const			//常量数据,使用的空间地址是在0x08000000-0x09FFFFFF
Item				//道具类型
hack_item = {
  /*copy form "hack_data/item_data.c "*/	     0x02E3,         0x0393,         0x0000,         0x09,         0x00,         0x00040011,         0x00000000,         0x08902452,         0x28,         0x07,         0x5F,         0x05,         0x0A,         0x11,         0x0096,         0x00,         0x08,         0x00,         0x00,         0x02,         0x00,         0x00,         0x00,
	.u15_ = 60,		//攻击修改(att hack)
};



