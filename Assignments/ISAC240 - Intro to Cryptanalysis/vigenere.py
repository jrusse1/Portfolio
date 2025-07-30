alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenere(message,key, mode):
    output = ''
    index = 0

    for m in message:

        if m.upper() not in alphabet:
            output += m
            continue

        keyIndex = alphabet.find(key[index].upper())
        if mode == 'e':
            newIndex = (alphabet.find(m.upper()) + keyIndex) % len(alphabet)
        elif mode == 'd':
            newIndex = (alphabet.find(m.upper()) - keyIndex) % len(alphabet)

        if m.isupper():
            output += alphabet[newIndex].upper()
        else:
            output += alphabet[newIndex].lower()

        index = (index + 1) % len(key)

    return output

message = "Otee aw deknjzeu mg fhv kgam Gbwdrv pse szmlunx bf fhv lsye gesoe rl tqffkw, iika zus yxsp ie aae hrgve. Hzl xmcv xpbrvlkqd jnxreibfs. Hv kwmlcr oms jnxreibfs ak mzmt dheqnk. Pzqn kaw oagmsun nxff olm szd yx oms cxxf achfq, slwvqncr zq crfw fo ybeeecy szd ixsxiqxv fhv igeikbgz hv pse ie. Bl iaj ggf tytl Yojvgi hrw tqee mswee hj fhrm lte ythby thfcuvkgds nxjq mrllqrj bf ut rgv ieix hmtihfuzzgy tid. Isunwnd ms kasf wrl af wrl fat kasf wybut tfkeqnkxv Bivkjq ak mzq mffwzt. Yx oms khjyeemwp bp mzq cfgkoifnkzejl gr hzl gin nxswnvlk. Fhv ywi gctkeej hx iiex zq hrw vdued szd kaw ooeowdsrmaan nblt tybk sofw-fmtlkwp mrg zmd uxkfrfrwp tyx eaou hx ooevwztitlqd xegam zg otita zq hrw kbeem lte ctkf fvp vmyj tfp wybut wrl wesvgluac ygd tyx wjetnluoe hx tij wweixg. Lte gbkfoc, wssgvk, szd gxseaem uaak pwde ixspy. Ethalvhf iaj mg qnkxj fhv mgin expf drr. Hueikw etzed ooelapeixv fhrm af wfndp bv t meewnd mnu pgdtyr sotzhf fo jesk tyx whicwgqr, snl zon aw recm ltak aw iolev zok wg ut. Yx vud ehl wnfp oty, snl te wxdf a whjqbfwazg kasf hv pgglu ggf crkjk olm zus zglqnkbgz. Hv llduxzdqd rzsunjm lte thfrejlaan fy zus nxswnvlk nuk waylp ywxt kasf hv vgglu ggf omxjoodx af aew ltak aae ffkeqr xegamp yjmmv hx yiew, uantxjziez nqnxxszcv, daxlzgy, mnu lwxf-jtudiwbuq, hrw tqee waepvkkqd cbcq dlll ny thffatm outy mzq fzkkf mrg zq mvm"
ciphertext = vigenere(message, 'SMART', 'd')
print(ciphertext)