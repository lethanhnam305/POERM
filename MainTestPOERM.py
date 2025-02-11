from AlgoPOERM import AlgoPOERM
from Interval import Interval
import numpy as np
class MainTestPOERM :
    def main( args) :
        # the min support of POERM algorithm
        #minSupport = 5000
        # the XSpan of POERM algorithm
        xSpan = 2
        # the YSpan of POERM algorithm
        ySpan = 2
        # the min confidence of POERM algorithm
        minConfidence = 0.5
        # the XYSpan of POERM algorithm
        xySpan = 2
        # Input file 
        inputFile1 ="OnlineRetail.txt"
        #minsup1 = [4000, 4500, 5000, 5500, 6000]
        minsup1 = [7000, 7500, 8000, 8500, 9000]
        minconf1 = [0.4, 0.5, 0.6, 0.7, 0.8]
        span1 = [2, 3, 4, 5, 6]
        inputFile2 ="fruithut.txt"
        minsup2 = [3500, 4000, 4500, 5000, 5500]
        minconf2 = [0.4, 0.5, 0.6, 0.7, 0.8]
        span2 = [4, 5, 6, 7, 8]
        inputFile3 ="BMS WebView1.txt"
        minsup3 = [150, 200, 250, 300, 350]
        minconf3 = [0.3, 0.4, 0.5, 0.6, 0.7]
        span3 = [2,3, 4, 5, 6]
        inputFile4 = "liquor_11.txt"

        # If the input file does not contain timestamps, then set this variable to true
        # to automatically assign timestamps as 1,2,3...
        selfIncrement = True
        # Output file 
        outputFile = "output.txt"
        # minsup
        '''
        runtime = []
        for i in minsup1:
            poerm = AlgoPOERM()
            poerm.runAlgorithm(inputFile1,i,xSpan, ySpan,minConfidence,xySpan, selfIncrement)
            runtime.append(poerm.getDeltaTime())
        with open('./Normal/1_minsup.txt', 'w') as f:
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
            poerm.runAlgorithm(inputFile1,minSupport,i,i,minConfidence,i, selfIncrement)
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
        
        #poerm = AlgoPOERM()
        #poerm.runAlgorithm(inputFile1,7000,xSpan,ySpan,0.4,xySpan, selfIncrement)
        #poerm.printRule()
        #poerm.writeRuletoFile(outputFile)
        #poerm.printStats()
        
        
        # Danh gia thuc nghiem tren 3 bo du lieu
        
        minSupport1 = 7000
        minSupport2 = 5000
        minSupport3 = 200
        output1 = "./Output1/Out_OnlineRetail.txt"
        output2 = "./Output1/Out_fruithut.txt"
        output3 = "./Output1/Out_BMS1.txt"
        output4 = "./Output1/Out_Liquor.txt"
        output5 = "./Output1/Out_mushrooms.txt"
        output6 = "./Output1/Out_foodmart.txt"
        output_1 = "./Output1/Output_1.txt"
        output_2 = "./Output1/Output_2.txt"
        output_3 = "./Output1/Output_3.txt"
        output_4 = "./Output1/Output_4.txt"
        output_5 = "./Output1/Output_5.txt"
        output_6 = "./Output1/Output_6.txt" 

        inputFile5 = "chess.txt"
        inputFile6 = "retail.txt"
        poerm = AlgoPOERM()
        
            #poerm1.runAlgorithm(inputFile1,minSupport1,xSpan, ySpan,minConfidence,xySpan, selfIncrement)
            #poerm1.writeRuletoFile(output1)
            #file.write(str(poerm1.getDeltaTime()) +" "+ str(poerm1.maxMemory) +"\n")
        poerm.runAlgorithm(inputFile5, 4000, xSpan , ySpan, minConfidence, xySpan, selfIncrement)
        poerm.writeRuletoFile(outputFile)
            #file.write(str(poerm.getDeltaTime()) +" "+ str(poerm.maxMemory) +"\n")
            #poerm.runAlgorithm(inputFile5,100,xSpan, ySpan,minConfidence,xySpan, selfIncrement)
            #poerm.writeRuletoFile(output4)
        poerm.printStats()
        '''
        writer = open("Mushrooms_.txt","w")
        with open("mushrooms.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                line = line[:-2]
                writer.write(str(line)+"\n")
        writer.close()
        '''
if __name__=="__main__":
    MainTestPOERM.main([])
           
           