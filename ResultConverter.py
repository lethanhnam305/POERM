class ResultConverter :
    # 	 This method converts a result file by converting item IDs to strings according to a provided mapping.
    # 	 @param mapItemIDtoStringValue  a mapping between item ID (key) and attribute value (value).
    # 	 @param outputFile the path of an output file to be converted
    # 	 @param outputFileConverted the path of the result file to be written to disk 
    # 	 @param Charset charset  the charset to be used for converting the file (e.g. UTF-8) or null if the default charset should be used.
    # 	 @throws IOException  an exception is thrown if there is an error reading/writing files
    def subconvert(self, mapItemIDtoStringValue,  outputFile,  outputFileConverted) :
        # SECOND STEP:  READ THE RESULT FILE AND CONVERT IT BY USING THE MAP
        # AND AT THE SAME TIME WRITE THE OUTPUT FILE.
        #finResult =  java.io.FileInputStream( java.io.File(outputFile))
        #myInputResult =  java.io.BufferedReader( java.io.InputStreamReader(finResult))
        writer = open(outputFileConverted,"w", encoding="UTF-8")
        #// we create an object for writing the output file
        #writer =  java.io.BufferedWriter( java.io.OutputStreamWriter( java.io.FileOutputStream(outputFileConverted), charset))
        # we read the file line by line until the end of the file
        with open(outputFile, "r", encoding="UTF-8") as myInputResult:
            lines = myInputResult.readlines()
            firstLine = True
            for line in lines:
                noItemsLeft = False
                if line != "":
                    if firstLine:
                        firstLine = False
                    else:
                        writer.write("\n")
                    split = line.split(" ")
                    for i in range(len(split)):
                        token = split[i]
                        if token.startswith("#") or noItemsLeft:
                            noItemsLeft = True
                            writer.write(token.rstrip('\n'))
                        else:
                            itemID = self.isInteger(token)
                            if itemID == None:
                                if token.find(",") >= 0:
                                    parts = token.split(",")
                                    for m in range(len(parts)):
                                        item = int(parts[m])
                                        stringRepresentation = mapItemIDtoStringValue.get(item)
                                        writer.write(stringRepresentation.rstrip('\n'))
                                        if m < len(parts) - 1:
                                            writer.write(",".rstrip('\n'))
                                else:
                                    writer.write(token.rstrip('\n'))
                            else:
                                name = mapItemIDtoStringValue.get(itemID)
                                if name == None:
                                    writer.write(str(itemID).rstrip('\n'))
                                else:
                                    writer.write(mapItemIDtoStringValue.get(itemID).rstrip('\n'))
                        if i != len(split) - 1:
                            writer.write(" ")
        # we close the output file
        writer.close()
    # *
    # 	 * This method converts a result file by converting item IDs to strings according to 
    # 	 * a provided mapping.
    # 	 * @param inputDB an input file providing the mapping between item ID (key) and attribute value (value)
    # 	 * as metadata.
    # 	 * @param outputFile the path of an output file to be converted
    # 	 * @param outputFileConverted the path of the result file to be written to disk 
    # 	 * @param Charset charset  the charset to be used for converting the file (e.g. UTF-8) or null if
    # 	 *         the default charset should be used.
    # 	 * @throws IOException  an exception is thrown if there is an error reading/writing files
    def convert(self, inputDB,  outputFile,  outputFileConverted):
        # WE FIRST READ THE DATABASE FILE TO READ THE METADATA INDICATING
        # THE MAPPING BETWEEN ITEM TO ATTRIBUTE VALUE.
        # For example, a line: @ITEM=16=weight=red
        # indicate that the item 16 correspond to the string "weight=red"
        # Objects to read the file
        #fin =  java.io.FileInputStream( java.io.File(inputDB))
        #myInputDB =  java.io.BufferedReader( java.io.InputStreamReader(fin, charset))
        # A map that
        # An entry in the map is :
        #   key  =  String (attribute value)
        #   value = Integer (item id)
        mapItemIDtoStringValue =  dict()
        # variable to read a line
        # we read the file line by line until the end of the file
        with open(inputDB, "r", encoding="UTF-8") as myInputDB:
            lines = myInputDB.readlines()
            for line in lines:
                if line.startswith("@ITEM"):
                    line = line[6:]
                    index = line.index("=")
                    itemID = int(line[0:index])
                    stringValue= line[index+1:]
                    mapItemIDtoStringValue[itemID] = stringValue
        self.subconvert(mapItemIDtoStringValue, outputFile, outputFileConverted)

    # *
    # 	 * Get the integer representation of a string or null if the string is not an integer.
    # 	 * @param string a string
    # 	 * @return an integer or null if the string is not an integer.
    def  isInteger(self, string) :
        result = None
        try :
            result = int(string)
        except :
            return None
        # only got here if we didn't return false
        return result