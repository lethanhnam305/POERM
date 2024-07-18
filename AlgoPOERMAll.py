import math
from POERParas import POERParas
from MemoryLogger import MemoryLogger
from Interval import Interval
from EventSetAppear import EventSetAppear
from RuleInterval import RuleInterval
from POERRule import POERRule
from POERRuleOccur import POERRuleOccur
import time
class AlgoPOERMAll :
    # the input file 
    inputFile = None
    # the start time of program run 
    startTime = 0
    # the end time of program run 
    endTime = 0
    # the runtime of program run 
    deltaTime = 0
    def  getDeltaTime(self) :
        return self.deltaTime
     # a datastructure to record parameter of the algorithm 
    parameter = None
    # a sequence that eliminates all events having less than minsup occurrences
    # from the input dataset
    XFreS = None
    # a sequence that eliminates all events having less than minsup*minconf
    # occurrences from the input dataset
    YFreS = None
    # a map to record item and its appear time interval 
    thisAppear = None
    # a list to record xEventSet 
    XFreAppear = None
    # a list to record yEventSet 
    YFreAppear = None
    # a list to record vaild poerm rule 
    ruleAppear = None
    # Maximum memory used during the last execution 
    maxMemory = 0.0
    def  getMaxMemory(self) :
        return self.maxMemory
    instance = MemoryLogger(0)
    def  runAlgorithm(self, inputFile,  minSupport,  xSpan,  ySpan,  minConfidence,  xySpan,  selfIncrement) :
        # * Initialize data structures
        self.XFreS =  dict()
        self.YFreS =  dict()
        self.thisAppear =  dict()
        self.XFreAppear =  []
        self.YFreAppear =  []
        self.ruleAppear =  []
        # save input file path and parameters
        self.inputFile = inputFile
        self.parameter = POERParas(minSupport, xSpan, ySpan, minConfidence, xySpan, selfIncrement)
        self.instance.reset()
        self.startTime = round(time.time() * 1000)
        self.preProcess(self.inputFile)
        self.miningXEventSet2()
        self.miningYEventSet()
        # System.out.println("x: " + this.XFreAppear.size() + " y: " + this.YFreAppear.size());
        self.findRule()
        self.instance.checkMemory()
        self.maxMemory = self.instance.getMaxMemory()
        self.endTime = round(time.time() * 1000)
        self.deltaTime = self.endTime - self.startTime
    #  Find all XEventSet that maybe the anti episode of a Partially-Ordered Episode Rule
    def miningXEventSet2(self) :
            index = 0
            end = len(self.XFreAppear)
            while index < end:
                self.thisAppear.clear()
                episodeAppear = self.XFreAppear[index]
                index += 1
                # Frequent-i item
                episode = episodeAppear.getEventSet()
                compareKey = episode[len(episode) - 1]
                appear = episodeAppear.getIntervals()
                for interval in appear :
                    intStart = interval.start
                    intEnd = interval.end
                    # for a frequent-i itemset and its time intervals[interval.start,
                    # interval.end),
                    # Search the time intervals [interval.end - XSpan + 1, interval.start) to add
                    # each event setFile}
                    # such that e > frequent-i itemset's lastItemand and its occurrences in the map
                    # fresMap;
                    for j in range (intEnd - self.parameter.getXSpan() + 1,intStart):
                        if j not in self.XFreS.keys():
                            continue
                        eventSet = self.XFreS.get(j)
                        for eventItem in eventSet :
                            # add each event setFile}
                            # such that e > frequent-i itemset's lastItemand and its occurrences in the map
                            # fresMap;
                            if eventItem > compareKey:
                                if eventItem in self.thisAppear.keys():
                                    self.thisAppear[eventItem].append(Interval(j, intEnd))
                                else :
                                    appearTime =  []
                                    appearTime.append(Interval(j, intEnd))
                                    self.thisAppear[eventItem] = appearTime
                    # Search the time intervals [interval.end + 1, interval.start + XSpan)
                    for j in range(intEnd+1,intStart + self.parameter.getXSpan()):
                        if j not in self.XFreS.keys():
                            continue
                        eventSet = self.XFreS.get(j)
                        for eventItem in eventSet :
                            if eventItem > compareKey:
                                if eventItem in self.thisAppear.keys():
                                    self.thisAppear[eventItem].append(Interval(intStart, j))
                                else :
                                    appearTime =  []
                                    appearTime.append(Interval(intStart, j))
                                    self.thisAppear[eventItem] = appearTime
                    # Search the time intervals [intStart, intEnd]
                    for j in range(intStart, intEnd+1):
                        if j not in self.XFreS.keys():
                            continue
                        eventSet = self.XFreS.get(j)
                        for eventItem in eventSet :
                            if eventItem > compareKey:
                                if eventItem in self.thisAppear.keys():
                                    self.thisAppear[eventItem].append(Interval(intStart, intEnd))
                                else :
                                    appearTime =  []
                                    appearTime.append(Interval(intStart, intEnd))
                                    self.thisAppear[eventItem] = appearTime
                # Add each pair of fresMap such that |value|minsup into XFreAppear;
                for key, value in self.thisAppear.items() :
                    # System.out.println("Finded ");
                    value = sorted(sorted(value, key = lambda x : x.start), key = lambda x : x.end)
                    newValue =  []
                    for i in range (0,len(value)):
                        if i == 0 or value[i].equal(newValue[len(newValue)-1])== False:
                            newValue.append(value[i])
                    if (len(newValue) >= self.parameter.getMinSupport()) :
                        newKey = list(episode)
                        newKey.append(key)
                        self.XFreAppear.append(EventSetAppear(newKey, newValue))
                end = len(self.XFreAppear)
                self.instance.checkMemory()
            print("end: " + str(end))
    # *
    # 	 * a Comparator to sort interval by its end.
    '''
    class myComparator(java.util.Comparator) :
        def  compare(self, a,  b) :
            if (a.end_special == b.end_special) :
                return a.start - b.start
            return a.end_special - b.end_special
    '''
    # class myComparator2 implements Comparator<Interval> {
    # 		public int compare(Interval a, Interval b) {
    # 			if (a.start == b.start) {
    # 				return a.end - b.end;
    # 			}
    # 			return a.start - b.start;
    # 		}
    # 	}
    # *
    # 	 * Read the dataset Convert the item in the dataset into numbers and build a map
    # 	 * for it. record each item occur time eliminates all events having less than
    # 	 * minsup occurrences from the input dataset to obtain a sequence XFres and less
    # 	 * than minsup * minconf occurrences to obtain a sequence YFres filter out
    # 	 * frequent-1 item in XFreAppear and YFreAppear
    def preProcess(self, input) :
            eventSet =  dict()
            line = None
            timestamp = 1
            num = None
            preTimestamp = -1
            # if self increment mode
            if (self.parameter.isSelfIncrement() == True) :
                with open(input, "r", encoding="UTF-8") as file:
                    lines = file.readlines()
                    # if the line is a comment, is empty or is a
                    # kind of metadata
                    for line in lines:
                        if line =="" or line[0] == '#' or line[0] == '%' or line[0] == '@':
                            timestamp += 1
                            continue
                    # System.out.println(timestamp+" " + line);
                        array = line.split(" ")
                        eSet =  []
                        eSet2 =  []
                        for event in array :
                        # Convert the item in the dataset into numbers and build a map for it.
                            num = int(event)
                            support = eventSet.get(num)
                            if (support != None) :
                                eventSet[num] = support + 1
                                self.thisAppear[num].append(Interval(timestamp, timestamp))
                            else :
                                eventSet[num] = 1
                                interval =  []
                                interval.append(Interval(timestamp, timestamp))
                                self.thisAppear[num] = interval
                        # use list save the data in this timestamp
                            eSet.append(num)
                            eSet2.append(num)
                        if (len(eSet) > 0) :
                        # use hashMap save the data in this timestamp
                            self.XFreS[timestamp] = eSet2
                        timestamp += 1
            else :
                with open(input, "r", encoding="UTF-8") as file:
                    lines = file.readlines()
                    # if the line is a comment, is empty or is a
                    # kind of metadata
                    for line in lines:
                        if line == "" or line[0] == '#' or line[0] == '%' or line[0] == '@':
                            continue
                        lineSplited = line.split("|")
                        timestamp = int(lineSplited[1])
                        array = lineSplited[0].split(" ")
                        eSet =  []
                        eSet2 =  []
                        for event in array :
                        # Convert the item in the dataset into numbers and build a map for it.
                            num = int(event)
                            support = eventSet.get(num)
                            if (support != None) :
                                eventSet[num] = support + 1
                                self.thisAppear[num].append(Interval(timestamp, timestamp))
                            else :
                                eventSet[num] = 1
                                interval =  []
                                interval.append(Interval(timestamp, timestamp))
                                self.thisAppear[num] = interval
                        # use list save the data in this timestamp
                            eSet.append(num)
                            eSet2.append(num)
                        if (len(eSet) > 0) :
                        # use hashMap save the data in this timestamp
                            self.XFreS[timestamp] = eSet2
            self.instance.checkMemory()
            # eliminates all events having less than minsup occurrences from the input
            # dataset to obtain a sequence XFres
            # and less than minsup * minconf occurrences to obtain a sequence YFres
            self.loadFrequent(eventSet)
    # 	 * eliminates all events having less than minsup occurrences from the input
    # 	 * dataset to obtain a sequence XFres and less than minsup * minconf occurrences
    # 	 * to obtain a sequence YFres filter out frequent-1 item in XFreAppear and
    # 	 * YFreAppear
    def loadFrequent(self, eventSet) :
        # TODO Auto-generated method stub
        for key, eSet in self.XFreS.items():
            XnewList =  []
            YnewList =  []
            for e in eSet :
                support = eventSet.get(e)
                if (support >= self.parameter.getMinSupport() * self.parameter.getMinConfidence()) :
                    YnewList.append(e)
                    if (support >= self.parameter.getMinSupport()) :
                        XnewList.append(e)
            self.XFreS[key] = XnewList
            self.YFreS[key] = YnewList
        for key,val in eventSet.items():
            numKey =  []
            numKey.append(key)
            if (float(val) >= float(self.parameter.getMinSupport()) * self.parameter.getMinConfidence()) :
                # YFreAppear.put(numKey, XFreAppear.get(numKey));
                value = self.thisAppear.get(key)
                # System.out.println("key: " + key);
                self.YFreAppear.append(EventSetAppear(numKey, value))
                if (val >= self.parameter.getMinSupport()) :
                    self.XFreAppear.append(EventSetAppear(numKey, value))
        self.instance.checkMemory()
    # *
    # 	 * Find all XEventSet that maybe the anti episode of a Partially-Ordered Episode
    # 	 * Rule
    def miningXEventSet(self) :
            index = 0
            end = len(self.XFreAppear)
            while index < end:
                self.thisAppear.clear()
                episodeAppear = self.XFreAppear[index]
                index += 1
                # Frequent-i item
                episode = episodeAppear.getEventSet()
                compareKey = episode[len(episode) - 1]
                appear = episodeAppear.getIntervals()
                for interval in appear :
                    intStart = interval.start
                    intEnd = interval.end
                    # for a frequent-i itemset and its time intervals[interval.start,
                    # interval.end),
                    # Search the time intervals [interval.end - XSpan + 1, interval.start) to add
                    # each event setF??e}
                    # such that e > frequent-i itemset's lastItemand and its occurrences in the map
                    # fresMap;
                    for j in range (intEnd - self.parameter.getXSpan() + 1,intStart):
                        if j not in self.XFreS.keys():
                            continue
                        eventSet = self.XFreS.get(j)
                        for eventItem in eventSet :
                            # add each event setF??e}
                            # such that e > frequent-i itemset's lastItemand and its occurrences in the map
                            # fresMap;
                            if eventItem > compareKey:
                                if eventItem in self.thisAppear.keys():
                                    self.thisAppear[eventItem].append(Interval(j, intEnd))
                                else :
                                    appearTime =  []
                                    appearTime.append(Interval(j, intEnd))
                                    self.thisAppear[eventItem] = appearTime
                    # Search the time intervals [interval.end + 1, interval.start + XSpan)
                    for j in range(intEnd+1,intStart + self.parameter.getXSpan()):
                        if j not in self.XFreS.keys():
                            continue
                        eventSet = self.XFreS.get(j)
                        for eventItem in eventSet :
                            if eventItem > compareKey:
                                if eventItem in self.thisAppear.keys():
                                    self.thisAppear[eventItem].append(Interval(intStart, j))
                                else :
                                    appearTime =  []
                                    appearTime.append(Interval(intStart, j))
                                    self.thisAppear[eventItem] = appearTime
                    # Search the time intervals [intStart, intEnd]
                    for j in range(intStart, intEnd+1):
                        if j not in self.XFreS.keys():
                            continue
                        eventSet = self.XFreS.get(j)
                        for eventItem in eventSet :
                            if eventItem > compareKey:
                                if eventItem in self.thisAppear.keys():
                                    self.thisAppear[eventItem].append(Interval(intStart, intEnd))
                                else :
                                    appearTime =  []
                                    appearTime.append(Interval(intStart, intEnd))
                                    self.thisAppear[eventItem] = appearTime
                # Add each pair of fresMap such that |value|??insup into XFreAppear;
                for key, value in self.thisAppear.items():
                    # System.out.println("Finded ??");
                    value = sorted(sorted(value, key = lambda x : x.start), key = lambda x : x.end)
                    newValue =  []
                    for i in range (0,len(value)):
                        if i == 0 or value[i].equal(newValue[len(newValue)-1])== False:
                            newValue.append(value[i])
                    if (len(newValue) >= self.parameter.getMinSupport()) :
                        newKey = list(episode)
                        newKey.append(key)
                        self.XFreAppear.append(EventSetAppear(newKey, newValue))
                end = len(self.XFreAppear)
                self.instance.checkMemory()
    # *
    # 	 * Find all YEventSet that maybe the anti episode of a Partially-Ordered Episode
    # 	 * Rule, similar to miningXEventSet
    def miningYEventSet(self) :
            index = 0
            end = len(self.YFreAppear)
            while (index < end) :
                self.thisAppear.clear()
                episodeAppear = self.YFreAppear[index]
                index += 1
                # Frequent-i item
                episode = episodeAppear.getEventSet()
                # System.out.println("visited " + episode);
                compareKey = episode[len(episode) - 1]
                appear = episodeAppear.getIntervals()
                for interval in appear :
                    intStart = interval.start
                    intEnd = interval.end
                    # Search the time intervals [interval.end - YSpan + 1, interval.start) to add
                    # each event setF??e}
                    # such that e > frequent-i itemset's lastItemand and its occurrences in the map
                    # fresMap;
                    for j in range (intEnd - self.parameter.getYSpan() + 1,intStart):
                        if j not in self.YFreS.keys():
                            continue
                        eventSet = self.YFreS.get(j)
                        for eventItem in eventSet :
                            if (eventItem > compareKey) :
                                if eventItem in self.thisAppear.keys():
                                    self.thisAppear[eventItem].append(Interval(j, intEnd))
                                else :
                                    appearTime =  []
                                    appearTime.append(Interval(j, intEnd))
                                    self.thisAppear[eventItem] = appearTime
                    # Search the time intervals [interval.end + 1, interval.start + YSpan)
                    for j in range(intEnd+1,intStart + self.parameter.getYSpan()):
                        if j not in self.YFreS.keys():
                            continue
                        eventSet = self.YFreS.get(j)
                        for eventItem in eventSet :
                            if (eventItem > compareKey) :
                                if eventItem in self.thisAppear.keys():
                                    self.thisAppear[eventItem].append(Interval(intStart,j))
                                else :
                                    appearTime =  []
                                    appearTime.append(Interval(intStart, j))
                                    self.thisAppear[eventItem] = appearTime
                    # Search the time intervals [intStart, intEnd]
                    for j in range(intStart, intEnd+1):
                        if j not in self.YFreS.keys():
                            continue
                        eventSet = self.YFreS.get(j)
                        for eventItem in eventSet :
                            if (eventItem > compareKey) :
                                if ((eventItem in self.thisAppear.keys())) :
                                    self.thisAppear[eventItem].append(Interval(intStart, intEnd))
                                else :
                                    appearTime =  []
                                    appearTime.append(Interval(intStart, intEnd))
                                    self.thisAppear[eventItem] = appearTime
                # Add each pair of fresMap such that |value|??insup * minconf into XFreAppear;
                for key, value in self.thisAppear.items():
                    # System.out.println("Finded ??");
                    value = sorted(sorted(value, key = lambda x : x.start), key = lambda x : x.end)
                    newValue =  []
                    for i in range (0,len(value)):
                        if i == 0 or value[i].equal(newValue[len(newValue)-1])== False:
                            newValue.append(value[i])
                    if (len(newValue) >= self.parameter.getMinSupport() * self.parameter.getMinConfidence()) :
                        newKey = list(episode)
                        newKey.append(key)
                        self.YFreAppear.append(EventSetAppear(newKey, newValue))
                end = len(self.YFreAppear)
                self.instance.checkMemory()
    # *
    # 	 * try to combine all xEventSet and yEventSet to generate rules
    def findRule(self) :
        print("XFreAppear: " + str(len(self.XFreAppear)) + " ")
        print("YFreAppear: " + str(len(self.YFreAppear)) + " ")
        # Integer anotherInteger = 225;
        for anitemset in self.XFreAppear :
            anitKey = anitemset.getEventSet()
            # 			if (anitKey.size() == 1 && anitKey.get(0).compareTo(anotherInteger) == 0) {
            # 				System.out.println(anitKey.get(0));
            # 			}else {
            # 				continue;
            # 			}
            anitValues = anitemset.getIntervals()
            # 		    System.out.println("scan X " + anitKey);
            anitStart = 0
            anitCount = 0
            for anitValue in anitValues :
                if anitValue.start <= anitStart:
                    continue
                anitCount += 1
                anitStart = anitValue.end
            if anitCount < self.parameter.getMinSupport():
                continue
            for conseset in self.YFreAppear :
                start = 0
                j = 0
                conseKey = conseset.getEventSet()
                # 				if (anitKey.size() == 1 && anitKey.get(0).compareTo(anotherInteger) == 0 && conseKey.size() == 1 && conseKey.get(0).compareTo(anotherInteger) == 0) {
                # 					System.out.println(anitKey.get(0));
                # 				}else {
                # 					continue;
                # 				}
                #if (len(anitKey) > 1 and conseKey[0] == 3) :
                    #print(" aaa ")
                conseValue = conseset.getIntervals()
                # 				if (anitKey.equals(conseKey)) {
                # 					continue;
                # 				}
                intervalList =  []
                #anitIndex = 0
                for anitValue in anitValues :
                    if (anitValue.start <= start) :
                        continue
                    while (j < len(conseValue) and conseValue[j].end <= anitValue.end) :
                        j += 1
                    for k in range(j,len(conseValue)):
                        if (conseValue[k].end - self.parameter.getYSpan() + 1 - self.parameter.getXYSpan() > anitValue.end) :
                            break
                        if (conseValue[k].start <= anitValue.end or conseValue[k].start > anitValue.end + self.parameter.getXYSpan()) :
                            continue
                        # 			    		count++;
                        intervalList.append(anitValue)
                        intervalList.append(conseValue[k])
                        intervalList.append(Interval(0, 0))
                        # 						if (intervalList.size() < 200) {
                        # 							System.out.println(anitValue.start + " " + conseValue.get(k).end + "end");
                        # 						}
                        start = conseValue[k].end
                        break
                confidence = int(len(intervalList) / 3)
                # 			    String.
                # 				System.out.println("key " + anitKey + "==>" + conseKey + " " + confidence + " / " + anitCount);
                self.instance.checkMemory()
                if (confidence >= anitCount * self.parameter.getMinConfidence()) :
                    # 			    	System.out.println("key " + anitKey + "==>" + conseKey + " " + confidence + " / " + anitCount);
                    self.ruleAppear.append(POERRule(anitKey, conseKey, None, anitCount, confidence))
    # *
    # 	 * write the information to file
    def printRule(self) :
        for poerrule in self.ruleAppear :
            episodeRule = ""
            antiEpisode = poerrule.getAntiEpisode()
            conseEpisode = poerrule.getConseEpisode()
            for anti in antiEpisode :
                episodeRule += str(anti) + " "
            episodeRule += "==> "
            for conse in conseEpisode :
                episodeRule += str(conse) + " "
            print("rule: " + episodeRule + "#SUP: " + str(poerrule.getAntiCount()) + " #CONF: " + str(poerrule.getRuleCount() / float(poerrule.getAntiCount())))
    # *
    # 	 * write the information to file
    def writeRule2File(self, filename) :
            self.instance.checkMemory()
            # rankRuleBySupport();
            with open(filename, "w") as file:
                for poerrule in self.ruleAppear :
                    buffer = ""
                    for anti in poerrule.getAntiEpisode() :
                        buffer += str(anti)
                        buffer += " "
                    buffer += "==> "
                    for conse in poerrule.getConseEpisode() :
                        buffer += str(conse)
                        buffer += " "
                    buffer += "#SUP: "
                    buffer += str(poerrule.getAntiCount())
                    buffer += " #CONF: "
                    buffer += str(poerrule.getRuleCount() / float(poerrule.getAntiCount()))
                    buffer += "\n"
                    file.write(str(buffer))
    # *
    # 	 * Print statistics about the algorithm execution to System.out.
    def printStats(self) :
        print("=============  POERM-ALL v.2.45 - STATS =============")
        print(" Rule count : " + str(len(self.ruleAppear)))
        print(" Maximum memory usage : " + str(self.maxMemory) + " mb")
        print(" Total time ~ : " + str(self.deltaTime) + " ms")
        print("===================================================")
    