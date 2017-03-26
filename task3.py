
import redis
redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
def function1():
    fp = open("data_set.txt", "r")
    # print(fp.name)
    cortana = []
    siri = []
    task = 0
    taskListForCortana=[]
    statementListForCortana=[]
    statement = 0


    buffer = fp.read();
    buffer = buffer.split("\n")
    # print(buffer)
    for line in buffer:
        if "cortana" in line:
            cortana.append(line)
        elif "siri" in line:
            siri.append(line)
    # print(cortana)
    # print(siri)

    # print("\n")

    for line in cortana:
        if "what" in line or "how" in line or "when" in line or "why" in line:
            # print(line)
            taskListForCortana.append(line);
            task=task+1
        else:
            statementListForCortana.append(line)
            statement=statement+1

    # print("TASKS FOR CORTANA")
    # print(taskListForCortana)
    # print("TOTAL = ",task)
    # print("STATEMENTS FOR CORTANA")
    # print(statementListForCortana)
    # print("TOTAL = ", statement)
    # print("\n")

    task=0
    statement=0
    taskListForSiri=[]
    statementListForSiri=[]

    for line in siri:
        if "what" in line or "how" in line or "when" in line or "why" in line:
            # print(line)
            taskListForSiri.append(line)
            task=task+1
        else:
            statementListForSiri.append(line)
            statement=statement+1

    # print("TASKS FOR SIRI")
    # print(taskListForSiri)
    # print("TOTAL = ", task)
    # print("STATEMENTS FOR SIRI")
    # print(statementListForSiri)
    # print("TOTAL = ", statement)
    fp.close()
    redis_db.hmset("pythonDict", taskListForCortana)
    redis_db.hgetall("pythonDict")
    redis_db.hmset("pythonDict1", taskListForSiri)
    redis_db.hgetall("pythonDict1")

function1()