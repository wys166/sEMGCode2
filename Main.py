from Function1 import *
from Function2 import *
from Function3 import *
from Function4 import *
from Function5 import *
from Function6 import *
from Function7 import *
from Function8 import *
from Function9 import *

'''
Run the main, and reproduce the results in the paper.
mode=1, 2, 3, 4, 5, 6, 7, 8, 9
mode: 1, Show Fig. 2.
mode: 2, Show Fig. 3.
mode: 3, Show Fig. 4 and Fig. 5.
mode: 4, Show Fig. 6 and Fig. 7.
mode: 5, Show Fig. 8 and Fig. 9. 
mode: 6, Show Fig. 10. 
mode: 7, Show Fig. 11.
mode: 8, Show Fig. 12.
mode: 9, Show Fig. 14 and Fig. 15. 
'''
def Main(mode=1):
    if mode == 1:
        main1(r'D:/Data/Denoise/Signal.csv', r'D:/Data/Denoise/Reference.csv')
    elif mode == 2:
        main2(r'D:/Data/Denoise/Signal.csv') 
    elif mode == 3:
        main3('D:/Data/FeatureSelection/FeatureComparison.csv') 
    elif mode == 4:
        main4('D:/Data/FeatureSelection')
    elif mode == 5:
        main5('D:/Data/IsometricSegmentation/Feature.csv')
    elif mode == 6:
        main6('D:/Data')  
    elif mode == 7:
        main7('D:/Data/P Value/P_Value.csv')
    elif mode == 8:
        main8('D:/Data/RMSE R2/RMSE_R2.csv')
    elif mode == 9:
        main9('D:/Data/ForceEstimation')
    else:
        print('Run error!')
        print("The mode is out of range! Please note: mode=1, 2, 3, 4, 5, 6, 7, 8, 9")

'''
Run!
'''        
Main(mode=2)

