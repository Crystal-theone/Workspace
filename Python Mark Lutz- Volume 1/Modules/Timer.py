"""
Contains the collection of functions used for checking the running efficiency of the functions.
"""
import time,sys
timer=time.clock if sys.platform[:3]=="win" else time.time
def total(reps,func,*args,**kwargs):
    """Returns total times required to run the function. Returns(Total Time,Last Result)"""
    repsList=list(range(reps))
    startTime=timer()
    for i in repsList:
        ret=func(*args,**kwargs)
    totalTime=timer()-startTime
    return (totalTime,ret)
def bestof(reps,func,*args,**kwargs):
    """Quickest function among reps runs.
       Returns(best time,last result)"""
    best=2**32
    for i in range(reps):
        startTime=timer()
        ret=func(*args,**kwargs)
        elaspedTime=timer()-startTime
        if elaspedTime<best:best=elaspedTime
    return (best,ret)
def bestoftotal(reps1,reps2,func,*args,**kwargs):
    """Best of total runs"""
    return bestof(reps1,total,reps2,func,*args,**kwargs)


