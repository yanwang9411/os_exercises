#lec9 虚存置换算法spoc练习

1. 置换算法的功能？

--x

> > 页缺失时需要置换出内存中的页面，加载新的页面

2. 全局和局部置换算法的不同？
--x

> > 局部置换在当前进程固定数目的页面中进行置换
> > 全局置换，进程的页面数目可变

3. 最优算法、先进先出算法和LRU算法的思路？
--x

> > 最优算法，对未来最远使用的页面进行替换
> > 先进先出： 最先载入的页面最先被替换
> > LRU： 最近最少使用的被替换

4. 时钟置换算法的思路？

--x
> > 对使用过的页面进行标记，循环查询，选取未被使用的页面替换， 和LRU思路类似

5. LFU算法的思路？

--x
> > LFU是最近最不常用页面置换算法,也就是淘汰一定时期内被访问次数最少的页

6. 什么是Belady现象？

--x 
> > 进程页面数增多，缺页率上升

7. 几种局部置换算法的相关性：什么地方是相似的？什么地方是不同的？为什么有这种相似或不同？

--x 
> > 局部置换算法有： FIFO， LRU， LFU，clock
> > 相似点，都是为了近似找出最优置换页面，fifo实现简单，但被替换的往往不符合程序运行特征，LRU 性能较好，不会出现belady，硬件支持要求高；clock是LRU的一个简单实现；LFU从使用次数的角度，选取最优页面


8. 什么是工作集？

--x 
> > 当前时刻t，向前长度为T的窗口中使用的页面集合

9. 什么是常驻集？

--x 
> > 当前时刻中内存中驻留的页

10. 工作集算法的思路？

--x 
> > 监视工作集，只有工作集中的页面才能留在内存

11. 缺页率算法的思路？

--x
> > 用两次缺页相隔的时间来衡量缺页率，缺页率高时，增加常驻集，相反减少

12. 什么是虚拟内存管理的抖动现象？

--x
> > 并发度升高到一定程度，CPU的利用效率反而下降

13. 操作系统负载控制的最佳状态是什么状态？

--x
> > 负载过高，对cpu资源的竞争激烈，对硬件有所损伤
> > 在一定范围，提高系统负载，理想负荷为1



## 小组思考题目

----
(1)（spoc）请证明为何LRU算法不会出现belady现象

--x
> > 见piazza


(2)（spoc）根据你的`学号 mod 4`的结果值，确定选择四种替换算法（0：LRU置换算法，1:改进的clock 页置换算法，2：工作集页置换算法，3：缺页率置换算法）中的一种来设计一个应用程序（可基于python, ruby, C, C++，LISP等）模拟实现，并给出测试。请参考附件代码或独自实现。

--x
> >

2号

addrlist = [0,1,2,3,0,2,3,6,2,1,4,2,3,1,2]
t = 4

window = []
workset = set([])

print "visit sequence :   "
print addrlist
print "window size :"
print t
print "Memory resident: "
for i in addrlist:
    if i in workset:
        print "HIT"
    else:
        print "MISS"
    if ( len(window) < t  ):
        window.append(i)
        workset.add(i)
        print workset

    else:
        del window[0]
        window.append(i)
        workset = set([])
        for k in range(0, t):
            workset.add(window[k])
        print workset
    print ' '




## 扩展思考题
（1）了解LIRS页置换算法的设计思路，尝试用高级语言实现其基本思路。此算法是江松博士（导师：张晓东博士）设计完成的，非常不错！

参考信息：

 - [LIRS conf paper](http://www.ece.eng.wayne.edu/~sjiang/pubs/papers/jiang02_LIRS.pdf)
 - [LIRS journal paper](http://www.ece.eng.wayne.edu/~sjiang/pubs/papers/jiang05_LIRS.pdf)
 - [LIRS-replacement ppt1](http://dragonstar.ict.ac.cn/course_09/XD_Zhang/(6)-LIRS-replacement.pdf)
 - [LIRS-replacement ppt2](http://www.ece.eng.wayne.edu/~sjiang/Projects/LIRS/sig02.ppt)
