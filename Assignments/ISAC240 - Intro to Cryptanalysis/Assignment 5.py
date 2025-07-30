letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ETAOIN = 'ETAOINVKJXQZ'
def singlefrequency(message):
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for m in message.upper():
        if m in letters:
            letterCount[m] += 1

    return letterCount

def getItemsAtIndexZero(items):
    return items[0]

def getFreqOrder(message):
    letterToFreq = singlefrequency(message)
    freqToLetter = {}
    for m in letters:
        if letterToFreq[m] not in freqToLetter:
            freqToLetter[letterToFreq[m]] = [m]
        else:
            freqToLetter[letterToFreq[m]].append(m)

    for m in freqToLetter:
        freqToLetter[m].sort(key=ETAOIN.find, reverse=True)
        freqToLetter[m]= ''.join(freqToLetter[m])

    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=getItemsAtIndexZero, reverse=True)
    freqOrder = []
    for m in freqPairs:
        freqOrder.append(m[1])

    return ''.join(freqOrder)

def englishFreqMatchScore(message):
    freqOrder = getFreqOrder(message)
    matchScore = 0
    for m in ETAOIN:
        if m in freqOrder:
            matchScore += 1
    return matchScore


print(englishFreqMatchScore('''When the mutton and an omelet had been served and a samovar and vodka brought, with some wine which the French had taken from a Russian cellar and brought with them, Ramballe invited Pierre to share his dinner, and himself began to eat greedily and quickly like a healthy and hungry man, munching his food rapidly with his strong teeth, continually smacking his lips, and repeating- "Excellent! Delicious!" His face grew red and was covered with perspiration. Pierre was hungry and shared the dinner with pleasure. Morel, the orderly, brought some hot water in a saucepan and placed a bottle of claret in it. He also brought a bottle of kvass, taken from the kitchen for them to try. That beverage was already known to the French and had been given a special name. They called it limonade de cochon (pig's lemonade), and Morel spoke well of the limonade de cochon he had found in the kitchen. But as the captain had the wine they had taken while passing through Moscow, he left the kvass to Morel and applied himself to the bottle of Bordeaux. He wrapped the bottle up to its neck in a table napkin and poured out wine for himself and for Pierre. The satisfaction of his hunger and the wine rendered the captain still more lively and he chatted incessantly all through dinner.'''))