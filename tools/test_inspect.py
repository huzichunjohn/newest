import inspect

class Test(object):
    def say(self):
	print "hello world."

for name, m in inspect.getmembers(Test, inspect.ismethod):
    print name, m

t = Test()
for name, m in inspect.getmembers(t, inspect.ismethod):
    print name, m
