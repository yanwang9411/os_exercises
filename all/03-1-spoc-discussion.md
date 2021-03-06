# lec5 SPOC思考题


NOTICE
- 有"w3l1"标记的题是助教要提交到学堂在线上的。
- 有"w3l1"和"spoc"标记的题是要求拿清华学分的同学要在实体课上完成，并按时提交到学生对应的git repo上。
- 有"hard"标记的题有一定难度，鼓励实现。
- 有"easy"标记的题很容易实现，鼓励实现。
- 有"midd"标记的题是一般水平，鼓励实现。


## 个人思考题
---

请简要分析最优匹配，最差匹配，最先匹配，buddy systemm分配算法的优势和劣势，并尝试提出一种更有效的连续内存分配算法 (w3l1)
```
  + 采分点：说明四种算法的优点和缺点
  - 答案没有涉及如下3点；（0分）
  - 正确描述了二种分配算法的优势和劣势（1分）
  - 正确描述了四种分配算法的优势和劣势（2分）
  - 除上述两点外，进一步描述了一种更有效的分配算法（3分）
 ```
- [x]  
- 


> 最差匹配： 
>
> 中等大小的分配较多时，效果最好，避免出现太多的小碎片； 
>

> 缺点：释放分区较慢，外部碎片，容易破坏大的空闲分区，因此后续难以分配大的分区
>
> 最先匹配：简单 ， 在高地址空间有大块内存；   
>
> 缺点 ： 外部碎片，分配大块时较慢
> 
> 最优匹配：
> 
> 大部分分配的尺寸较小时，效果很好， · 可避免大的空闲分区被拆分，· 可减小外部碎片的大小 · 相对简单
>
> 缺点： 外部碎片，释放分区较慢，容易产生很多无用的小碎片

>
> buddysystem: 
>
>优点： 释放分区快，简单，分配内存整齐
>
> 缺点：合并条件严格会产生较多碎片

>  

## 小组思考题

请参考ucore lab2代码，采用`struct pmm_manager` 根据你的`学号 mod 4`的结果值，选择四种（0:最优匹配，1:最差匹配，2:最先匹配，3:buddy systemm）分配算法中的一种，在应用程序层面来实现，并给出测试用例。 (spoc)

>

>

class pmm_manager:
    def __init__(self):
        self.list_ = [ (0,1024), ]
    
    def alloc_size(self, size):
        for i in self.list_:
            if i[1] >= size:
                index = self.list_.index(i)

                if i[1] == size:
                    self.list_.remove(i)
                else:
                    self.list_[index] = (i[0]+size, i[1]-size)

                print self.list_
                return i[0]
            
        return -1

    def free_size(self, addr, size):
        if  len(self.list_) < 1: 
            self.list_.append((addr,size))
            return
        pre = -1
        post = len(self.list_)

        after = 1025
        before = -1

        end = addr+size
        
        for ele in self.list_:
            if  ele[0] >= end :
                after = ele[0]
                post = self.list_.index(ele)
                break

        pre = post - 1
        if pre >= 0:
            before = self.list_[pre][0]+self.list_[pre][1]

        if before < addr and after > end:
            self.list_.insert(post, (addr, size))
            print self.list_
            return

        if before == addr and after > end:
            self.list_[pre] = ( self.list_[pre][0], self.list_[pre][1]+size )
            print self.list_
            return

        if before < addr and after == end:
            self.list_[post] = ( addr, size + self.list_[post][1] )
            print self.list_
            return

        if  before == addr and after == end :
            self.list_[post] = (self.list_[pre][0], self.list_[post][1]+size+self.list_[pre][1])
            del self.list_[pre]
            print self.list_
            return

        return 




pm = pmm_manager()
print pm.alloc_size(1)
print pm.alloc_size(1)
pm.free_size(0,1)
print pm.alloc_size(2)
pm.free_size(1,1)
print pm.alloc_size(2)



--- 

## 扩展思考题

阅读[slab分配算法](http://en.wikipedia.org/wiki/Slab_allocation)，尝试在应用程序中实现slab分配算法，给出设计方案和测试用例。


## “连续内存分配”与视频相关的课堂练习

### 5.1 计算机体系结构和内存层次
MMU的工作机理？

- [x]  

>  http://en.wikipedia.org/wiki/Memory_management_unit

L1和L2高速缓存有什么区别？

- [x]  

>  http://superuser.com/questions/196143/where-exactly-l1-l2-and-l3-caches-located-in-computer
>  Where exactly L1, L2 and L3 Caches located in computer?

>  http://en.wikipedia.org/wiki/CPU_cache
>  CPU cache

### 5.2 地址空间和地址生成
编译、链接和加载的过程了解？

- [x]  

>  

动态链接如何使用？

- [x]  

>  


### 5.3 连续内存分配
什么是内碎片、外碎片？

- [x]  

>  

为什么最先匹配会越用越慢？

- [x]  

>  

为什么最差匹配会的外碎片少？

- [x]  

>  

在几种算法中分区释放后的合并处理如何做？

- [x]  

>  

### 5.4 碎片整理
一个处于等待状态的进程被对换到外存（对换等待状态）后，等待事件出现了。操作系统需要如何响应？

- [x]  

>  

### 5.5 伙伴系统
伙伴系统的空闲块如何组织？

- [x]  

>  

伙伴系统的内存分配流程？

- [x]  

>  

伙伴系统的内存回收流程？

- [x]  

>  

struct list_entry是如何把数据元素组织成链表的？

- [x]  

>  




