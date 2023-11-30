with open("fille.txt", "r")as f:
    print(type(f))
    f.seek(10) # it will strat reading after 10 index
    print(f.tell()) # it will tell how many letters we will seek
    data = f.read(5) # read next five bytes

    print(data)
with open("main.txt", "w")as f:

    f.write("Hello world")
    f.truncate(5) # it reduce the file size to only 5 bytes or character
with open("main.txt", "r")as f:
    print(f.read())
