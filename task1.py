

def function1():
    fp = open("data_set.txt", "r")
    print(fp.name)
    cortana = 0
    siri = 0
    # METHOD 1
    buffer = fp.readlines();
    for line in buffer:
        if "cortana" in line:
            cortana = cortana + 1
        elif "siri" in line:
            siri = siri + 1
    print(cortana)
    print(siri)

    # METHOD 2
    # buffer = fp.read();
    # buffer = buffer.split("\n")
    # print(buffer)
    # for line in buffer:
    #     if "cortana" in line:
    #         cortana = cortana + 1
    #     elif "siri" in line:
    #         siri = siri + 1
    # print(cortana)
    # print(siri)


    fp.close()

function1()
