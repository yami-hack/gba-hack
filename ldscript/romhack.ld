/*
链接脚本是按顺序链接程序的,
OVERLAY  	:或者COPY,表示覆盖数据,
			:然后利用objcopy把该段的标识改为 "AX" (alloc,exec),--set-section-flags name="r,a,c"
			:覆盖数据,按段的索引顺序覆盖,(0>1>2>3...) 
如果当前段的内存布局在另一个段的段内存内,并且另一段标识是(AX),则会忽略当前段,非(AX)则不会忽略

*/

INCLUDE rom.ld
INCLUDE segment.ld