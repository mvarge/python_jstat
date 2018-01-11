import os

JDK_PATH=r"/cygdrive/c/Program Files/Java/jdk1.8.0_91/"

def jstat_finder(folder):
    for f in os.listdir(folder):
        f = os.path.join(folder, f)
        if os.path.isfile(f):
            if "jstat" in f:
                print f
                return f
        elif os.path.isdir(f):
            jstat_finder(f)

f = jstat_finder(JDK_PATH)

print f
