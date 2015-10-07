#-*- coding: utf-8 -*-  
#coding=utf-8
import struct
import sys
#execfile("bin.py");

def outASM(ifile,out,address,size):
    ifile.seek(address);
    offset    =    0;
    while offset + 0x10 <= size :
        data0    = '0x%08x'%struct.unpack("I",ifile.read(4));
        data1    = '0x%08x'%struct.unpack("I",ifile.read(4));
        data2    = '0x%08x'%struct.unpack("I",ifile.read(4));
        data3    = '0x%08x'%struct.unpack("I",ifile.read(4));
        off        = '0x%08x'%(offset + address)
        datastr    =    "    .int  %s,%s ,%s,%s       @%s"%(data0,data1,data2,data3,off)
        if out == None:
            print datastr
        else:
            datastr +=  '\n';
            out.writelines(datastr);
        offset    +=    0x10;
    while offset < size:
        data0    = '0x%02x'%struct.unpack("B",ifile.read(1));
        off        = '0x%08x'%(offset + address)
        datastr    =    "    .byte %s                                               @%s" %(data0,off);
        if out == None:
            print datastr;
        else:
            datastr +=  '\n';
            out.writelines(datastr);
        offset    +=    1;
    return offset;

class Chunk:
    def __init__(self,addr,size,ttype,filename,info):
        self.addr    =    addr;
        self.size    =    size;
        self.type    =    ttype;
        self.file    =    filename;
        self.info    =    info;

chunks    =    [];

def add_chunk_file(addr,size,ttype,filename,info):
    chunks.append(Chunk(addr,size,ttype,filename,info));
    
def add_chunk(addr,size,ttype,info):
    chunks.append(Chunk(addr,size,ttype,"",info));
    

    
class FileOut:
    def __init__(self,ifile,size,chunk):
        self.file    =    ifile;
        self.size    =    size;
        self.offset    =    0;
        self.chunks    =    chunk;
        self.chunkindex    =    0;
    def outASM(self,out):
        osize    =    self.size;
        self.out(out,osize);
    def out(self,out,size):
        endoffset    =    self.offset + size;
        while self.offset < endoffset:
            cchunk      =   None;
            if self.chunkindex < len(self.chunks):
                cchunk    =    self.chunks[self.chunkindex];
            #非空chunk
            if cchunk != None:
                #如果大于当前的偏移和小于输出结束地址
                #   先输出中间空白的嵌套函数输出中间空白的内容,可能包括其他chunk
                #   然后判断是否存在文件名,如果存在,则创建文件,信息输出到文件里,然后汇编输出到文档中
                #   判断块的类型,如果是只是添加信息,则是0,如果是替换,则是1,  替换时,不会包括其他块
                #       添加信息时,紧接着输出数据
                #       替换时,是直接跳过那些数据
                if cchunk.addr >= self.offset and cchunk.addr < endoffset:
                    outsize    =    cchunk.addr - self.offset;
                    self.offset        +=    outASM(self.file,out,self.offset,outsize);
                    infostr            =    cchunk.info;
                    outsize            =    cchunk.size;
                    ofile            =    None;
                    if cchunk.file !='' and cchunk.file != None:
                        ofile        =    open(cchunk.file,'w+');
                    self.chunkindex    +=    1;
                    if ofile == None:
                        print infostr;
                    else:
                        infostr +=  '\n';
                        ofile.writelines(infostr);

                    if cchunk.type == 1:
                        #这是Memory,或引用的,替换的
                        self.offset +=  outsize;
                    else:
                        self.out(ofile,outsize);
                    #判断如果是输出到文件,那么添加.include 汇编质量
                    if ofile         != None:
                        ofile.close();
                        incfile     =   cchunk.file;
                        if out != None:
                            out.writelines('    .include \"%s\"\n'%incfile);
                        else:
                            print '    .include \"%s\"\n'%incfile;
                            
                    #end------
                elif cchunk.addr < self.offset:
                    #当这个cchunk地址 小于当前偏移,则索引自加1
                    self.chunkindex    +=    1;
                else:
                    #当前chunk不属于该chunk,那么就直接输出数据
                    outsize    =        endoffset - self.offset;
                    self.offset        +=    outASM(self.file,out,self.offset,outsize);
                    break;
                #end-------
            else:
                #
                outsize        =    endoffset    -    self.offset;
                self.offset    +=    outASM(self.file,out,self.offset,outsize);
		
        endstr  =   "@end chunk  0x%08X\n\n"%endoffset;
        if out ==None:
            print endstr;
        else:
            out.writelines(endstr);
        
        
            
            
        
    

def BIN2s(ifile,out,address,size) :
    ifile.seek(0,2);
    filesize    =    ifile.tell();
    if size <= 0:
        size    =    filesize;
    #chunks.sort(lambda x,y:cmp(x.addr,y.addr));
    chunks.sort(key = lambda x:x.addr);
    oo            =    FileOut(ifile,size,chunks);
    oo.outASM(out);


def add_chunk_fileEx(addr,size,fn,sname,esize,num) :
    #info = "    " + ".weak\t\t" + sname + "\n    " + ".global\t\t" + sname +"\n    " + ".size\t\t" + sname + ",\t" + esize + " * " + num +"\n    " + ".type\t\t" + sname + ",\t" + "%object" + "\n" + sname + ":\n";
    info    =  "    .weak\t\t%s"%sname;
    info    +=  "\n    .global\t\t%s"%sname;
    info    +=  "\n    .size\t\t%s ,%d * %d"%(sname,esize,num);
    info    +=  "\n    .type\t\t%s,%s"%(sname,'%object');
    info    +=  "\n%s:"%sname;
    add_chunk_file(addr, size, 0, fn, info);
    
def add_chunkEx(addr,size,sname,esize,num):
    add_chunk_fileEx(addr, size, "", sname, esize, num)
    
def add_pointer(addr,name):
	#def add_chunk(addr,size,ttype,info):
	info	=	"\t.word\t%s"%name;
	add_chunk(addr,4,1,info);
	
def add_pointers(addr_list,name):
	info	=	"\t.word\t%s"%name;
	for addr in addr_list:
		add_chunk(addr,4,1,info);

def add_asmbl(addr,link,mode = 2):
    code  = "";
    if mode==0:
        code = "\t.code 16\n"
    elif mode==1:
	    code = "\t.code 32\n"
    info  =  "\tbl 0x%08X"%link;
    info  =  code + info;
    add_chunk(addr,4,1,info);

def add_list_asmbl(addr_list,link,mode = 2):
    code  = "";
    if mode==0:
        code = "\t.code 16\n"
    elif mode==1:
	    code = "\t.code 32\n"
    info  =  "\tbl 0x%08X"%link;
    info  =  code + info;
    for addr in addr_list:
        addr	=	addr - 0x08000000;
        add_chunk(addr,4,1,info);

funcStr = [".code 32",".code 16\n\t.thumb_func"]

def addfunction(ea,size,ctype):
    addr    =    ea - 0x08000000;
    info    =    "\t%s\tsub_%X\n"%(".global",ea);
    info    +=    "\t%s\n"%funcStr[ctype];
    info    +=    "\t%s\tsub_%X,%s\n"%(".type",ea,"%function");
    info    +=    "\t%s\tsub_%X,0x%X\n"%(".size",ea,size);
    info    +=    "sub_%X:\n"%ea;
    add_chunk(addr,size,0,info);

def Fs(fn):
    f       =   open(fn,"r");
    text    =   f.read();
    f.close();
    return text;
    
    
    
# add_chunk_file(0x20,0,0,"aa.t","4567");
# add_chunk_file(0x10,0x10,0,"bb.t","4567");
# add_chunk_file(0x40,0,0,"","4567");
# add_chunk_file(0x30,0,0,"","4567");
# chunks.sort(key = lambda x:x.addr);



# print chunks[0].addr;
# print chunks[1].addr;
# print chunks[2].addr;
# print chunks[3].addr;


#=======================================================
#数据
#add_chunk_file(0x858288,0x34*255,0,"char_data.asm",Fs("char_data.l"));
#
add_chunk(0x0, 0x0, 0, Fs("base.info"));








#结束块
#========================================================


argc    =   len(sys.argv);

if  argc< 3:
    print 'error:  binaryfile [outfile] ext.py>[outfile]'
    exit();
    

execfile(sys.argv[2]);
    
print "@out binary file:" + sys.argv[1];
ifile    =    open(sys.argv[1],"rb");
#outASM(file,None,0,0x24);
BIN2s(ifile,None,0,0);


ifile.close();


