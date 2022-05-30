import numpy as np

dictionary = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,
              'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20}

string = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'



answer = map(lambda x,y,z: (x*y, y+z) , sorted(set([dictionary[key] for key in string.split()])), sorted(set([dictionary[key] for key in string.lower().split()]))[1:], sorted(set([dictionary[key] for key in string.split()]))[2:])


print(list(answer))
	
#using numpy
print(list(zip(np.array((sorted(set([{'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
                                    'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20}
                                    ['five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split()[key]] 
                                    for key in range(len('five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.lower().split()))])))[:-2]) * 
    								np.array((sorted(set([{'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
                                    'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20}
                                    ['five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split()[key]] 
                                    for key in range(len('five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.lower().split()))])))[1:-1]), 
            						np.array((sorted(set([{'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
                                    'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20}
                                    ['five thirteen two eleven seventeen two one thirteen ten four eight five nineteen '.split()[key]] 
                                    for key in range(len('five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.lower().split()))])))[1:-1]) + 
                                    np.array((sorted(set([{'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,
                                    'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20}
                                    ['five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split()[key]] for key in range(len('five thirteen two eleven seventeen two one thirteen ten four eight five nineteen '.lower().split()))])))[2:]))))		

	

#implementation without libraries
		 
for key in range(len(sorted(set([{'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
                                'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,
                                'eighteen':18,'nineteen':19,'twenty':20}['five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split()[key]] 
                                for key in range(len('five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.lower().split()))]))[2:])):
	print((sorted(set([{'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
    'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20}
	['five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split()[key]] 
 	for key in range(len('five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.lower().split()))]))[:-2][key] * 
	sorted(set([{'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
    'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20}
	['five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split()[key]] 
    for key in range(len('five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.lower().split()))]))[1:-1][key],
	sorted(set([{'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
    'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20}
	['five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split()[key]] 
    for key in range(len('five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.lower().split()))]))[1:-1][key] + 
    sorted(set([{'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20}
	['five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split()[key]] 
 	for key in range(len('five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.lower().split()))]))[2:][key]))
		 
