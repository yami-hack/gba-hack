# gba-hack
  因为GBA的游戏机能,所以可以把GBA游戏机当成是简单的嵌入式设备。所以，利用标准C的特点，可以实现用纯C来达成修改目的
##下面介绍修改所需的工具
  * devkitpro
    *这个软件包可以在sourceforge.net找到,有window和linux版本,软件包已经包含了(gcc,make,as),只要设置好系统环境就可以使用
  * (*)python
    * 这个是可选的,只是为了更简单的用脚本生成.c源码和导出rom里面的数据
  基本上,一个工具就能解决了
##生成GBA游戏里面所需的修改数据步骤如下
  * 找出数据
    * 先通过逆向找出游戏的数据,可以是NO$GBA,也可以是其他逆向工具。或者别人提供的数据
  * 数据结构体
    * 然后在更具数据的结构定义C结构体,再利用工具(或py脚本),有规律的导出C结构体数据
      例如, [1] = {10,20,30}, [2] = {50,60,21}, //...     GNU C编译器的初始化可用索引初始化,当想修改某项时,直接[索引]          ={初始化列表}
      注意,必须是const struct n[] = {}...     ,这是.rodata数据段,对应gba ROM地址 0x08000000 .. 0x09FFFFFF
  * 生成数据
    * 得到file.c源码后,使用下列生成file.o文件
      arm-none-eabi-gcc -nostdlib -c -O2 file.c
    * 导出二进制数据
      arm-none-eabi-objcopy -O binary -j.rodata file.o file.bin
      * -O binary:输出二进制数据
      * -j:只输出.rodata
    然后向ROM指定地址导入二进制数据
    
##生成GBA游戏里面的程序
  * 找出程序首地址
  * 使用链接脚本修正符号地址
  * sub_<addr>.c 生成单一过程的源码
  * 分析函数的二进制接口,一般gcc命令参数添加  -mabi=apcs-gnu
  * 分析函数的cpu模式
    * 如果每条指令是2字节或者函数地址是单数,那么就是thumb模式,
    * 如果是双数或者指令字节是4字节,那么就是arm模式
    根据函数CPU模式添加gcc命令  -mthumb
  * 最大化优化-O2
  * 需要学出个ld脚本,link.ld
  * 生成二进制数据
    arm-none-eabi-gcc -nostdlib -c -O2 -mabi-apcs-gnu -mcpu=arm7tdmi -mthumb -Tlink.ld file.c 
      * -nostdlib  表示不使用标准库,直接.c源码一对一生成程序
      * -c         生成静态文件
      * -O2        最大化优化
      * -mabi-apcs-gnu   普遍的游戏二进制接口
      * -mcpu=arm7tdmi   GBA CPU
      * -mthumb    CPU执行模式
      * -Tlink.ld  使用link.ld作为链接脚本
    arm-none-eabi-objcopy -O binary -j.text file.o file.bin
  * 对于ld脚本的编写,参考"/ld"目录


##更多内容待添加
