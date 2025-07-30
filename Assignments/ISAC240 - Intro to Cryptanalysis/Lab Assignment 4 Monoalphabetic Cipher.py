alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def translate(message, key, mode):
    translated = ''
    charsA = alphabet
    charsB = key
    if mode == 'decrypt':
        charsA, charsB = charsB, charsA

    for i in message:
        if i.upper() in charsA:
            index = charsA.find(i.upper())

            if i.isupper():
                translated += charsB[index].upper()
            else:
                translated += charsB[index].lower()

        else:
            translated += i

    return translated

print(translate("The glow of the first fire that began on the second of September was watched from the various roads by the fugitive Muscovites and by the retreating troops, with many different feelings. The Rostov party spent the night at Mytishchi, fourteen miles from Moscow. They had started so late on the first of September, the road had been so blocked by vehicles and troops, so many things had been forgotten for which servants were sent back, that they had decided to spend that night at a place three miles out of Moscow. The next morning they woke late and were again delayed so often that they only got as far as Great Mytishchi. At ten o'clock that evening the Rostov family and the wounded traveling with them were all distributed in the yards and huts of that large village. The Rostovs' servants and coachmen and the orderlies of the wounded officers, after attending to their masters, had supper, fed the horses, and came out into the porches. In a neighboring hut lay Raevski's adjutant with a fractured wrist. The awful pain he suffered made him moan incessantly and piteously, and his moaning sounded terrible in the darkness of the autumn night. He had spent the first night in the same yard as the Rostovs. The countess said she had been unable to close her eyes on account of his moaning, and at Mytishchi she moved into a worse hut simply to be farther away from the wounded man. In the darkness of the night one of the servants noticed, above the high body of a coach standing before the porch, the small glow of another fire. One glow had long been visible and everybody knew that it was Little Mytishchi burning- set on fire by Mamonov's Cossacks", "nmlkjihgfedcbazyxwvutsrqpo".upper(), 'encrypt'))
print(translate("Ugj hczr zi ugj ifwvu ifwj ugnu mjhna za ugj vjlzak zi Vjyujbmjw rnv rnulgjk iwzb ugj snwfztv wznkv mp ugj ithfufsj Btvlzsfujv nak mp ugj wjuwjnufah uwzzyv, rfug bnap kfiijwjau ijjcfahv. Ugj Wzvuzs ynwup vyjau ugj afhgu nu Bpufvglgf, iztwujja bfcjv iwzb Bzvlzr. Ugjp gnk vunwujk vz cnuj za ugj ifwvu zi Vjyujbmjw, ugj wznk gnk mjja vz mczldjk mp sjgflcjv nak uwzzyv, vz bnap ugfahv gnk mjja izwhzuuja izw rgflg vjwsnauv rjwj vjau mnld, ugnu ugjp gnk kjlfkjk uz vyjak ugnu afhgu nu n ycnlj ugwjj bfcjv ztu zi Bzvlzr. Ugj ajqu bzwafah ugjp rzdj cnuj nak rjwj nhnfa kjcnpjk vz ziuja ugnu ugjp zacp hzu nv inw nv Hwjnu Bpufvglgf. Nu uja z'lczld ugnu jsjafah ugj Wzvuzs inbfcp nak ugj rztakjk uwnsjcfah rfug ugjb rjwj ncc kfvuwfmtujk fa ugj pnwkv nak gtuv zi ugnu cnwhj sfccnhj. Ugj Wzvuzsv' vjwsnauv nak lznlgbja nak ugj zwkjwcfjv zi ugj rztakjk ziifljwv, niujw nuujakfah uz ugjfw bnvujwv, gnk vtyyjw, ijk ugj gzwvjv, nak lnbj ztu fauz ugj yzwlgjv. Fa n ajfhgmzwfah gtu cnp Wnjsvdf'v nketunau rfug n iwnlutwjk rwfvu. Ugj nritc ynfa gj vtiijwjk bnkj gfb bzna faljvvnaucp nak yfujztvcp, nak gfv bznafah vztakjk ujwwfmcj fa ugj knwdajvv zi ugj ntutba afhgu. Gj gnk vyjau ugj ifwvu afhgu fa ugj vnbj pnwk nv ugj Wzvuzsv. Ugj lztaujvv vnfk vgj gnk mjja tanmcj uz lczvj gjw jpjv za nllztau zi gfv bznafah, nak nu Bpufvglgf vgj bzsjk fauz n rzwvj gtu vfbycp uz mj inwugjw nrnp iwzb ugj rztakjk bna. Fa ugj knwdajvv zi ugj afhgu zaj zi ugj vjwsnauv azufljk, nmzsj ugj gfhg mzkp zi n lznlg vunakfah mjizwj ugj yzwlg, ugj vbncc hczr zi nazugjw ifwj. Zaj hczr gnk czah mjja sfvfmcj nak jsjwpmzkp dajr ugnu fu rnv Cfuucj Bpufvglgf mtwafah- vju za ifwj mp Bnbzazs'v Lzvvnldv", "nmlkjihgfedcbazyxwvutsrqpo".upper(), 'decrypt'))