#%%
with open('input.txt', 'r') as f:
    input = f.read().splitlines()   
#part 1
def binary2int(binary): 
    int_val, i, n = 0, 0, 0
    while(binary != 0): 
        a = binary % 10
        int_val = int_val + a * pow(2, i) 
        binary = binary//10
        i += 1
    return int_val
def getResults(input):
    '''
        Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report.
    '''
    def findCommonBits(input: list, count: list):
        '''
            Given a list of 0 or 1s find the most common bit recursely
        '''
        if input == []:
            if count[0] > count[1]:
                return '0'
            else:
                return '1'
        if input[0] == 0:
            count[0] += 1
        else:
            count[1] += 1
        return findCommonBits(input[1:], count)
    
    def splitInput(input: list):
        '''
            there are 12 bits in each input chunk
        '''
        pos1 = [int(x[0]) for x in input]
        pos2 = [int(x[1]) for x in input]
        pos3 = [int(x[2]) for x in input]
        pos4 = [int(x[3]) for x in input]
        pos5 = [int(x[4]) for x in input]
        pos6 = [int(x[5]) for x in input]
        pos7 = [int(x[6]) for x in input]
        pos8 = [int(x[7]) for x in input]
        pos9 = [int(x[8]) for x in input]
        pos10 = [int(x[9]) for x in input]
        pos11 = [int(x[10]) for x in input]
        pos12 = [int(x[11]) for x in input]
        return [pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12]
    
    def invertBits(bits: list):
        '''
            Invert the bits of a list
        '''
        inverted = []
        for b in bits:
            if b == '0':
                inverted.append('1')
            else:
                inverted.append('0')
        return inverted
            
       
    bitsByPosition = splitInput(input)
    gammaBitsList = [findCommonBits(x, [0,0]) for x in bitsByPosition]
    epsilonBitsList = invertBits(gammaBitsList)
    gammaBits = int(''.join(gammaBitsList))
    epsilonBits = int(''.join(epsilonBitsList))
    epsilonInt = binary2int(epsilonBits)
    gammaInt = binary2int(gammaBits)
    return gammaInt, epsilonInt

g, e = getResults(input)
print(f'Part 1: {g*e}')

# part 2
# def getOxyRating(input: list, position: int):
#     bitCriteria = input[0][position] #get the bit in the given position of the first number in the input
#     newInput = filter(lambda x: x[position] == bitCriteria, input) #filter the input to only include numbers with the same bit in the given position
#     return newInput

def getNumList(input: list, position: int):
    '''
        Given a list of numbers, return a list of the numbers in the given position
    '''
    return [x[position] for x in input]

def findCommonBits2(input: list, count: list):
        '''
            Given a list of 0 or 1s find the most common bit recursely
        '''
        if input == []:
            if count[0] > count[1]:
                return '0'
            else:
                return '1'
        if input[0] == '0':
            count[0] += 1
        else:
            count[1] += 1
        return findCommonBits2(input[1:], count)

def filterInput(input: list, position: int, bit: str):
    '''
        Given an input list, return a list of all the numbers with the given bit in the given position
    '''
    return [x for x in input if x[position] == bit]

def getOxyRating(input: list):
    safeInput = input[:]
    def helper(input: list, pos: int):
        if len(input) == 1:
            return input[0]
        searchSpace = getNumList(input, pos)
        mostCommonBit = findCommonBits2(searchSpace, [0,0])
        filteredInput = filterInput(input, pos, mostCommonBit)
        return helper(filteredInput, pos+1)
    return helper(safeInput, 0)

def findLeastCommonBits(input: list, count: list):
    if input == []:
        if count[1] >= count[0]:
            return '0'
        else:
            return '1'
    if input[0] == '0':
        count[0] += 1
    else:
        count[1] += 1
    return findLeastCommonBits(input[1:], count)

def getCO2Rating(input: list):
    safeInput = input[:]
    def helper(input: list, pos: int):
        if len(input) == 1:
            return input[0]
        searchSpace = getNumList(input, pos)
        leastCommonBit = findLeastCommonBits(searchSpace, [0,0])
        filteredInput = filterInput(input, pos, leastCommonBit)
        return helper(filteredInput, pos+1)
    return helper(safeInput, 0)
    
test = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010'
]    

def getResults2(input):
    '''
    '''
    oxy, co2 = getOxyRating(input), getCO2Rating(input)
    return binary2int(int(oxy)), binary2int(int(co2))

o, c = getResults2(input)
print(f'Part 2: {o*c}')


    
    
# %%
