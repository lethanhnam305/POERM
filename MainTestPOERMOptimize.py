from AlgoPOERMOptimize import AlgoPOERMOptimize
from Interval import Interval
import numpy as np
import time
class MainTestPOERMOptimize:
    def main( args) :
        # the min support of POERM algorithm
        # the XSpan of POERM algorithm
        xSpan = 5
        # the YSpan of POERM algorithm
        ySpan = 5
        # the min confidence of POERM algorithm
        minConfidence = 0.5
        # the XYSpan of POERM algorithm
        xySpan = 5
        # Input file 
        # If the input file does not contain timestamps, then set this variable to true
        # to automatically assign timestamps as 1,2,3...
        selfIncrement = True
        # Output file 
        outputFile = "output.txt"

        inputFile1 ="OnlineRetail.txt"
        #minsup1 = [4000, 4500, 5000, 5500, 6000]
        #minSupport = 8000
        minsup1 = [7000, 7500, 8000, 8500, 9000]
        minconf1 = [0.4, 0.5, 0.6, 0.7, 0.8]
        span1 = [2, 3, 4, 5, 6]
        inputFile2 ="fruithut.txt"
        minsup2 = [3500, 4000, 4500, 5000, 5500]
        minconf2 = [0.3, 0.4, 0.5, 0.6, 0.7]
        span2 = [4, 5, 6, 7, 8]
        inputFile3 ="BMS WebView1.txt"
        minsup3 = [150, 200, 250, 300, 350]
        minconf3 = [0.3, 0.4, 0.5, 0.6, 0.7]
        span3 = [2,3, 4, 5, 6]
        '''
        # Danh gia thuc nghiem tren 3 bo du lieu
        minSupport1 = 7000
        minSupport2 = 5000
        output1 = "./Output2/Out_OnlineRetail.txt"
        output2 = "./Output2/Out_fruithut.txt"
        output_1 = "./Output2/Output_1.txt"
        output_2 = "./Output2/Output_2.txt"
        poerm = AlgoPOERMOptimize()
        with open(output_2,"w") as file :
            poerm.runAlgorithm(inputFile2,minSupport2,xSpan, ySpan,minConfidence,xySpan, selfIncrement)
            poerm.writeRuletoFile(output2)
            file.write(str(poerm.getDeltaTime()) +" "+ str(poerm.maxMemory) +"\n")
            #poerm.runAlgorithm(inputFile2,minSupport2,xSpan, ySpan,minConfidence,xySpan, selfIncrement)
            #poerm.writeRuletoFile(output2)
            #file.write(str(poerm.getDeltaTime()) +" "+ str(poerm.maxMemory) +"\n")
        '''
        # minsup
        '''
        runtime = []
        for i in minsup1:
            poerm = AlgoPOERMOptimize()
            poerm.runAlgorithm(inputFile1,i,xSpan, ySpan,minConfidence,xySpan, selfIncrement)
            runtime.append(poerm.getDeltaTime())
        with open('1_minsup.txt', 'w') as f:
            buffer =""            
            for item in minsup1:
                buffer += str(item) + " "
            buffer = buffer[:-1]
            buffer += "\n"
            f.write(buffer)
            buffer =""            
            for item in runtime:
                buffer += str(item) + " "
            buffer = buffer[:-1]
            buffer += "\n"
            f.write(buffer)
        '''
        # minconf
        '''
        runtime = []
        for i in minconf1:
            poerm = AlgoPOERM()
            poerm.runAlgorithm(inputFile1,minSupport,xSpan, ySpan,i,xySpan, selfIncrement)
            runtime.append(poerm.getDeltaTime())
        with open('1_minconf.txt', 'w') as f:
            buffer =""            
            for item in minconf1:
                buffer += str(item) + " "
            buffer = buffer[:-1]
            buffer += "\n"
            f.write(buffer)
            buffer =""            
            for item in runtime:
                buffer += str(item) + " "
            buffer = buffer[:-1]
            buffer += "\n"
            f.write(buffer)
        '''
        #span
        '''
        runtime = []
        for i in span1:
            poerm = AlgoPOERM()
            poerm.runAlgorithm(inputFile1,6000,i,i,minConfidence,i, selfIncrement)
            runtime.append(poerm.getDeltaTime())
        with open('1_span.txt', 'w') as f:
            buffer =""            
            for item in span1:
                buffer += str(item) + " "
            buffer = buffer[:-1]
            buffer += "\n"
            f.write(buffer)
            buffer =""            
            for item in runtime:
                buffer += str(item) + " "
            buffer = buffer[:-1]
            buffer += "\n"
            f.write(buffer)
        '''
        poerm = AlgoPOERMOptimize()
        poerm.runAlgorithm(inputFile3,200,xSpan,ySpan,0.5,xySpan, selfIncrement)
        poerm.printRule()
        #poerm.writeRuletoFile(outputFile)
        #poerm.printStats()
if __name__=="__main__":
    MainTestPOERMOptimize.main([])
# So sanh 2 thuat toan
# OnelineRetail
# Fruithut
# Accidents
           