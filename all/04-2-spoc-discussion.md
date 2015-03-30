#lec9 虚存置换算法spoc练习

## 小组思考题目

----
(1)（spoc）请证明为何LRU算法不会出现belady现象


(2)（spoc）根据你的`学号 mod 4`的结果值，确定选择四种替换算法（0：LRU置换算法，1:改进的clock 页置换算法，2：工作集页置换算法，3：缺页率置换算法）中的一种来设计一个应用程序（可基于python, ruby, C, C++，LISP等）模拟实现，并给出测试。请参考附件代码或独自实现。


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
