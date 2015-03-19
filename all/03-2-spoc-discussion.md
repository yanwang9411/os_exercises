# lec6 SPOC思考题


NOTICE
- 有"w3l2"标记的题是助教要提交到学堂在线上的。
- 有"w3l2"和"spoc"标记的题是要求拿清华学分的同学要在实体课上完成，并按时提交到学生对应的git repo上。
- 有"hard"标记的题有一定难度，鼓励实现。
- 有"easy"标记的题很容易实现，鼓励实现。
- 有"midd"标记的题是一般水平，鼓励实现。


## 个人思考题
---

（1） (w3l2) 请简要分析64bit CPU体系结构下的分页机制是如何实现的
```
  + 采分点：说明64bit CPU架构的分页机制的大致特点和页表执行过程
  - 答案没有涉及如下3点；（0分）
  - 正确描述了64bit CPU支持的物理内存大小限制（1分）
  - 正确描述了64bit CPU下的多级页表的级数和多级页表的结构或反置页表的结构（2分）
  - 除上述两点外，进一步描述了在多级页表或反置页表下的虚拟地址-->物理地址的映射过程（3分）
 ```
- [x]  

>  
> 64bit物理内存为2^64 byte
> 每个页的大小为1024 byte，采用多级页表或反置页表
> 多级页表，即将原页号切分，变成多级页表树，此时若某级页表有不存在表项，则可以节省下一级页表的存储空间
> 反置页表：和物理地址对应，页寄存器对应物理页帧，对逻辑地址进行hash映射，利用快表查找，解决冲突 

## 小组思考题
---

（1）(spoc) 某系统使用请求分页存储管理，若页在内存中，满足一个内存请求需要150ns。若缺页率是10%，为使有效访问时间达到0.5ms,求不在内存的页面的平均访问时间。请给出计算步骤。 

- [x]  

> 500=0.9\*150+0.1\*x
> x = 3650 ns

（2）(spoc) 有一台假想的计算机，页大小（page size）为32 Bytes，支持32KB的虚拟地址空间（virtual address space）,有4KB的物理内存空间（physical memory），采用二级页表，一个页目录项（page directory entry ，PDE）大小为1 Byte,一个页表项（page-table entries
PTEs）大小为1 Byte，1个页目录表大小为32 Bytes，1个页表大小为32 Bytes。页目录基址寄存器（page directory base register，PDBR）保存了页目录表的物理地址（按页对齐）。

PTE格式（8 bit） :
```
  VALID | PFN6 ... PFN0
```
PDE格式（8 bit） :
```
  VALID | PT6 ... PT0
```
其
```
VALID==1表示，表示映射存在；VALID==0表示，表示映射不存在。
PFN6..0:页帧号
PT6..0:页表的物理基址>>5
```
在[物理内存模拟数据文件](./03-2-spoc-testdata.md)中，给出了4KB物理内存空间的值，请回答下列虚地址是否有合法对应的物理内存，请给出对应的pde index, pde contents, pte index, pte contents。
```
Virtual Address 6c74
Virtual Address 6b22
Virtual Address 03df
Virtual Address 69dc
Virtual Address 317a
Virtual Address 4546
Virtual Address 2c03
Virtual Address 7fd7
Virtual Address 390e
Virtual Address 748b
```

比如答案可以如下表示：
```
Virtual Address 7570:
  --> pde index:0x1d  pde contents:(valid 1, pfn 0x33)
    --> pte index:0xb  pte contents:(valid 0, pfn 0x7f)
      --> Fault (page table entry not valid)
      
Virtual Address 21e1:
  --> pde index:0x8  pde contents:(valid 0, pfn 0x7f)
      --> Fault (page directory entry not valid)

Virtual Address 7268:
  --> pde index:0x1c  pde contents:(valid 1, pfn 0x5e)
    --> pte index:0x13  pte contents:(valid 1, pfn 0x65)
      --> Translates to Physical Address 0xca8 --> Value: 16
```

> 页目录表存储在 page11，
> 
> 6c74:   pde index: 1b , (valid 1, pfn a0)  pte index 03 (valid 1, pfn e1)
> 
> 6b22 : pde index: 1a, (valid 1 , pfn d2) pte index 19 ( valid 1 , pfn c7)
>
> 03df pde index : 00, ( valid 1 , pfn da ) pte index 1e ( valid 1, pfn 85) 
>
> 69dc : pde index : 1a ( valid 1, pfn d2) pte index : 0e ( valid 0, pfn 7f) fail
>
> 317a : pde index : 0c ( valid 1, pfn 98) pte index : 0b (valid 1, pfn b5)
>
> 4546: pde index : 11 ( valid 1, pfn a1 ) pte index 0a : ( valid 0, pfn 7f)  fail
>
> 2c03: pde index : 0b ( valid 1, pfn c4) pte index 00 : ( valid 1, pfn d7)
> 
> 7fd7: pde index : 1f ( valid 1, pfn 92) pte index 1e : ( valid 0, pfn 7f)  fail 
>
> 390e: pde index : 0e ( valid 0, pfn 7f) pte index 08 :                      fail
>
> 748b: pde index : 1d ( valid 1, pfn 80) pte index  04: ( valid 0, pfn 7f)    fail
>




（3）请基于你对原理课二级页表的理解，并参考Lab2建页表的过程，设计一个应用程序（可基于python, ruby, C, C++，LISP等）可模拟实现(2)题中描述的抽象OS，可正确完成二级页表转换。

>  
 \#include \<iostream\>
\#include \<cstdlib\>
\#include \<memory.h\>

using namespace std;


struct v_addr {
    unsigned offset :5;
    unsigned frame : 5;
    unsigned page_dir : 5;
};

struct p_addr {
    unsigned offset : 5;
    unsigned frame : 7;
};

struct frame_ {
    unsigned frame : 7;
};


// get the unit of requested address

class page_m {
    private:
        char** memory;
        frame_ pde_base;
        // pde_base;
    public:
        page_m(){
            memset ( &pde_base, 0, sizeof(pde_base));
            memory = new char* [128];
            for ( int i=0; i<128; i++ ) {
                memory[i] = new char[32];
                for ( int j = 0; j<32; j++ ){
                    memory[i][j] = 0x0;
                }
            }
            memory[0][0] = 0x81;
            memory[1][0] = 0x82;
            memory[2][0] = 0x01;
        }

        ~page_m(){
            for ( int i=0; i<128; i++ ) {
                delete memory[i];
            }
            delete[] memory;
        }

        bool get_by_pde_index( int pde_index, int& pte_addr) {
            pte_addr = (int)memory[pde_base.frame][pde_index];
            if ( !(pte_addr & 0x80) )
                return false;
            pte_addr = 0x7f & memory[pde_base.frame][pde_index];
            return true;
        }

        bool get_by_pte_index( int pte_addr, int pg_index, int& pg_addr) {
            pg_addr = (int)memory[pte_addr][pg_index];
            if ( !(pg_addr & 0x80) )
                return false;
            pg_addr = memory[pte_addr][pg_index] & 0x7f;
            return true;
        }
        
        char get_by_addr ( v_addr addr) {
            int pde_index = addr.page_dir;
            int pg_index = addr.frame;
            int pte_addr = 0;
            if ( !get_by_pde_index(pde_index, pte_addr) ) {
                cout << "fail" << endl;
                return ' ';
            }
            
            int pg_addr = 0;
            if ( !get_by_pte_index(pte_addr, pg_index, pg_addr) ) {
                cout << "fail" << endl;
                return ' ';
            }

            // print the result
            
            cout << "physical address :"  << endl; 
            cout << " number of frame ---" << pg_addr  << endl;
            cout << " offset --- " << addr.offset << endl;
            cout << "content: " << (int)memory[pg_addr][addr.offset] << endl;
            return memory[pg_addr][addr.offset];

                
           return memory[0][0]; 
        }
};

        
int main()
{
    v_addr addr;
    addr.page_dir = 0;
    addr.frame = 0;
    addr.offset = 0;
    page_m pm;
    pm.get_by_addr(addr);
    return 0;
}


（4）假设你有一台支持[反置页表](http://en.wikipedia.org/wiki/Page_table#Inverted_page_table)的机器，请问你如何设计操作系统支持这种类型计算机？请给出设计方案。

>  搜索逻辑地址对应的页帧，使用hash表查询，在快表中查询相应的页表项，有冲突时查找冲突链，查找失败产生异常
>  实现时，首先存储hash函数，并存储hash表的基地址，（或许可以在cpu中高速缓存hash表），查找快表（包括冲突链）找到页表基地址，访问cache，保证最佳情况0次 访存。


--- 

## 扩展思考题

阅读64bit IBM Powerpc CPU架构是如何实现[反置页表](http://en.wikipedia.org/wiki/Page_table#Inverted_page_table)，给出分析报告。

--- 
