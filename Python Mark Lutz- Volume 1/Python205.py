import Modules.Pybench as profiler,sys
pythons=[(1,"python"),(0,"python34")]
stmt=[(0,0,"[x**2 for x in range(1000)]")]
traceCMD='-t' in sys.argv
pythons=pythons if '-a' in sys.argv else None
profiler.runner(stmt,pythons,traceCMD)
