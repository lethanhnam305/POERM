from AlgoPOERMAll import AlgoPOERMAll
from Interval import Interval
class MainTestPOERM :
    def main( args) :
        # the min support of POERM algorithm
        minSupport = 5000
        # the XSpan of POERM algorithm
        xSpan = 5
        # the YSpan of POERM algorithm
        ySpan = 5
        # the min confidence of POERM algorithm
        minConfidence = 0.5
        # the XYSpan of POERM algorithm
        xySpan = 5
        # Input file 
        inputFile ="fruithut.txt"
        # If the input file does not contain timestamps, then set this variable to true
        # to automatically assign timestamps as 1,2,3...
        selfIncrement = True
        # Output file 
        outputFile = "output.txt"
        poerm = AlgoPOERMAll()
        poerm.runAlgorithm(inputFile,minSupport,xSpan, ySpan,minConfidence,xySpan, selfIncrement)
        poerm.printRule()
        poerm.writeRule2File(outputFile)
        poerm.printStats()
if __name__=="__main__":
    MainTestPOERM.main([])
           
           