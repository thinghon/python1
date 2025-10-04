text = """
20224016-박소호
Soonchunhyang University
Department of Computer Science and Engineering
"""
f=open("프로그래밍1/test.txt",'w')
f.write(text)
f.close()

f = open('Documents//프로그래밍1//test.txt')
lines = f.read()
print(lines.upper())
