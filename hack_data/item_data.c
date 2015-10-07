
typedef unsigned char 	u8;
typedef unsigned short 	u16;
typedef unsigned int 	u32;

typedef signed char  	s8;
typedef signed short 	s16;
typedef signed int 		s32;


typedef struct{
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

#define DEF_ITEM_1_BASE(name,desc,desc2,code)		(name),(desc),(desc2),(code)
#define DEF_ITEM_2_(type,ability,bonuses,effect)	(type),(ability),(bonuses),(effect)
#define DEF_ITEM_3_(durability,power,hit,weight,critical,range)	(durability),(power),(hit),(weight),(critical),(range)
#define DEF_ITEM_4_(cost,rank,icon)				(cost),(rank),(icon)
#define DEF_ITEM_5_(s_u_effect,weaponeffect,weaponexp)		(s_u_effect),(weaponeffect),(weaponexp)


#define HACK_ITEM_BASE		0x20
//#define HACK_ITEM_BASE   	0x30
#define HACK_ITEM_ID(id)	(HACK_ITEM_BASE	+(id))

//命名必须是rom2asm/Ext.py,的符号命名, 或者item_data[0xff]
const Item item_data[] = {
	    [0x0000] =    {0x0000,         0x0000,         0x0000,         0x00,         0x00,         0x00000000,         0x00000000,         0x00000000,         0x00,         0x00,         0x00,         0x00,         0x00,         0x00,         0x0000,         0x00,         0x00,         0x00,         0x00,         0x00,         0x00,         0x00,         0x00},
	    [0x0001] =    {0x02DB,         0x038B,         0x0000,         0x01,         0x00,         0x00000001,         0x00000000,         0x00000000,         0x2E,         0x05,         0x5A,         0x05,         0x00,         0x11,         0x000A,         0x01,         0x00,         0x00,         0x00,         0x01,         0x00,         0x00,         0x00},
	    [0x0002] =    {0x02DC,         0x038C,         0x0000,         0x02,         0x00,         0x00000001,         0x00000000,         0x00000000,         0x1E,         0x03,         0x64,         0x02,         0x05,         0x11,         0x0010,         0x01,         0x01,         0x00,         0x00,         0x01,         0x00,         0x00,         0x00},
		//....
		//or
		[0x3] = {0x02DC,         0x038C,         0x0000,         0x02,         0x00,         0x00000001,         0x00000000,         0x00000000,         0x1E,         0x03,         0x64,         0x02,         0x05,         0x11,         0x0010,         0x01,         0x01,         0x00,         0x00,         0x01,         0x00,         0x00,         0x00
				,
				.u15_	=	14,
				.u14_	=	15,
	    },
		//or
		[0x4]	=	{
			DEF_ITEM_1_BASE(0x2de,0x38e,0x0,0x4),
			DEF_ITEM_2_(0,0x1,0,0),
			DEF_ITEM_3_(0x14,0xd,0x50,0x8,0,0x11),
			DEF_ITEM_4_(0x4B,0xB5,0x3),
			DEF_ITEM_5_(0,0,1),
		},

		//or
		[HACK_ITEM_ID(0)] = {
				//.............
		},

		//or
		//...
		//[0x5]={}
		//[0x6] = {}
		//...........
};



