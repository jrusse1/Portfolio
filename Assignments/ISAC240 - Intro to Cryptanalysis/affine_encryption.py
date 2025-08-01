ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def affineCipher(message,key1,key2):
    output = ''
    for m in message:



        if m.upper() not in ALPHABET:
            output += m
            continue

        index = ALPHABET.find(m.upper())
        newIndex = (index * key1 + key2) % len(ALPHABET)

        output += ALPHABET[newIndex]

    return output

message = "When the mutton and an omelet had been served and a samovar and vodka brought, with some wine which the French had taken from a Russian cellar and brought with them, Ramballe invited Pierre to share his dinner, and himself began to eat greedily and quickly like a healthy and hungry man, munching his food rapidly with his strong teeth, continually smacking his lips, and repeating- Excellent! Delicious! His face grew red and was covered with perspiration. Pierre was hungry and shared the dinner with pleasure. Morel, the orderly, brought some hot water in a saucepan and placed a bottle of claret in it. He also brought a bottle of kvass, taken from the kitchen for them to try. That beverage was already known to the French and had been given a special name. They called it limonade de cochon (pig's lemonade), and Morel spoke well of the limonade de cochon he had found in the kitchen. But as the captain had the wine they had taken while passing through Moscow, he left the kvass to Morel and applied himself to the bottle of Bordeaux. He wrapped the bottle up to its neck in a table napkin and poured out wine for himself and for Pierre. The satisfaction of his hunger and the wine rendered the captain still more lively and he chatted incessantly all through dinner"
key1 = 11
key2 = 3

print(affineCipher(message,key1,key2))



