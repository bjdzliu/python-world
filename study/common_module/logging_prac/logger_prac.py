import logging

FORMAT='%(asctime)-15s\tThread info: %(thread)d %(threadName)s %(message)s'

FORMAT_a='%(asctime)-15s\tThread info: %(thread)d %(threadName)s %(message)s'

logging.basicConfig(format=FORMAT,level=logging.INFO)

root=logging.getLogger()
print(root.name,type(root),root.parent,id(root))

# logger_a 的 parent 是root
logger_a=logging.getLogger('a')
print(logger_a.name,type(logger_a),id(logger_a.parent),id(logger_a))
print(logger_a.getEffectiveLevel())
logger_a.info("\noutput")
logger_a.setLevel(28)
logger_a.info("output----")
