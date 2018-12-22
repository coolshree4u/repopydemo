from ConfigParser import ConfigParser
obj= ConfigParser()
obj.read('testing.cnf')
print(obj.get('section1','firstvariable'))