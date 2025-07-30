import isEnglish, math

def decryptMessage(key, message):
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    output = [''] * numOfColumns

    col = 0
    row = 0
    for i in message:
        output[col] += i
        col += 1
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(output)

def hackTransposition(message):
    for key in range(1, len(message)):
        decryptedText = decryptMessage(key, message)

        if isEnglish.isEnglish(decryptedText):
            print('Key %s: %s' % (key, decryptedText))

    return None



hackTransposition("Pwc hloiilFiewetarmo rhse.ntr sn  hea cHhi'nhheassxe. d; i  c  wocPaphauoiraeysuers   lriswladreeaen eddsddb      eshtettlhihnhioosetrmno  ioigkrArud. ereg  hsblhfTioay ahslt sce u aie htmbdsFeiose,raoro  ednersan   btncawterdhnihde  dta eFf hnitrowi nselenf  nln owtcothuhohw ira meom ttednsh hn .eole h lua wiIfryPimn s ot  i bvhwanpea in rfratoteosnhtevrk  hrieoaaero yisrouh rt rsia os lmnnniay,doidn   tsedoaf h  nnromsh dofetah m nrsiw ttetsath ee sheit,w e n  atrc alyoeit i r thskfttyeeeruo in or brtsmetu io dhtenmt-e yeeh  oelteacfs h sh  siD utctnotrhhagrhcein ooh eddgs cfiroeoalnem fmygaia p  dlrS,bbfoet eeuv .wcsl w aai shNludauoiksenb cie duohn a rbogP absl igl taieritisnreeon  ren aoten ttnh, the e coelt ua  yhmnihK eilsiru dismenAdko,mdrlen lebe  fira asonttolhr,a,flo, k   u aewtttan hhhefdaeeedt  r   ewtesoaraa ttt sshrh t keeehhn  erieotht m whasR,p ad.u rst  sbei lBsuvtiooititsnta oi ghnouni  snsgmbt l  pehwyniofeh inso owg srR hhaieuget b san'vldsz seeeiet r cadheyfin ex odsa pgre tsel da hrot ntoiohtdhuemeh etnymat  c  thFwefn era,rot es athFn hm ercteeb ehh  edn rwocecweafaehias ud tt ms lheaieso nfn hofirdookena fueagii ldrldnid  y  t aa oasstnrf  h de rdoP ploiuiceoyfleuasafdrrtili rien cbeodgsue s  tl wiaiutditntdyotyd.y nh,   be  hBiu.speunt ua t  Trih tbhpdehheer aeec inr  agsodwKuae  arst.atseee th m sBtenlo ee oifosnctn fitl ,i diid tmeocegsosnksi s   tvithtoiin iofnncos  egof ttd m hhh dpteeeteahim otteg.m ai h abibhtAnrlio t'ielua sndisnt g tedhm ays euhn  s sidwwtgks ieoae etruttmxhete oa  n aoctleosdthosf   ecs hsoik,oearre n fd daereen n alraadhiystn os udtuetar hsdosetee   sh  iht-esttio  th s bsrrd myhaeide unedeattg  sshteFPtuee riir rmeenefsonrase rcrt auoheitrpsm oo .eeun o  nn.bfTl,d e ho eA weowrnte khsdaas ot kkto aeeerfwnvnne ede iesr nintuet mgsf hhm  feaaeaaextddtnrp  i dilhhat naeethlgi  eea nhnl niiaoydenndt es g  tc h tboiwisoe seso eeir mpnxvefea te atshi dchsinmeei ngos nodumeagneiern  rsntdttehte ohd  dw e ta.hs bhn oooyedTlmt   heehafse  enio fRryr aiu teligssh,orusii s ridntiweaegona,n   gs soop  t fnrhfhw  eiuehttvsl ohhe lR eens ud  teosisw lfsdtalf i ryo-sane,oemnoe tsostthitk  .ineesu sge tnH ,maadei .nre naderhtn dseedt tan haarttetndio  d o sP nnrmito eeehtcalrehoslrmius e,nluo  gdrfbs  e etan bconotuapdthrup  ensesn iedaoin  wwngtP  h.hinha eeoabNyrtvio rhetwcei a o nbnauagetnls esddkon.  if  tnn cBhogwauet hrtn iar  mftiPha  eiekhwde eee rm  noreodtuetui t  tdo,dR  n iutn fdsooao s trrniw o oahkuNtnanna stodpk  w on")