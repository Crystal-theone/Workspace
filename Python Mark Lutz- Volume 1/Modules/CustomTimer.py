import time,sys
timer=time.clock if sys.platform[:3]=="win" else time.time
def totalTime(reps,func,*args):
    repetition=range(reps)
    startTime=timer()
    for i in repetition:
        func(*args)
    resultTime=timer()-startTime
    return (resultTime,"Total Time")

def bestOf(reps,func,*argument):
    repetitions=range(reps)
    minTime=2**32
    for i in repetitions:
        startTime=timer()
        ret=func(*argument)
        totalTime=timer()-startTime
        minTime=totalTime if totalTime<minTime else minTime
    return (minTime,ret)
