
# %%

class Solution:

    # szótárba felvesszük a vizsgálandó zárójelek
    # nyitó és záró verzióját
    braces = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

            
    def isValid(self, s: str) -> bool:

        if not isinstance(s,str): raise ValueError

        length = len(s)


        # zárójelpár kereséshez 
        #   openpos: az aktuális nyitó zárójel pozíciója
        #   closepos: az openpos-hoz tartozó záró zárójel helye
        #   braces: a nyitó zárójeltól számolva keressük a kifejezés végét
        #       egy nyitó: +1
        #       egy záró:  -1
        #       ha lemegy nullára, akkor megvan

        openpos = 0
        while openpos < length:
            # ha záró zárójellel találkozunk, akkor az biztos rossz 
            if s[openpos] in list(self.braces.values()): return False
            
            # ha nyitó zárójellel találkozunk, akkor megkeressük a záró párját
            if s[openpos] in list(self.braces.keys()):

                # ha a string végén vagyunk és épp kinyitottunk egy zárójelet, akkor az mindenképp rossz
                if openpos >= length -1: return False

                # kikeressük a használandó nyitó és záró zárójelet
                # ez inkább csak az olvashatóság miatt van
                bropen = s[openpos]
                brclose = self.braces[bropen]

                # megkeressük az adott nyitó zárójel záró párját
                closepos = openpos
                braces = 0
                for closepos in range(openpos,length):
                    if s[closepos] == bropen:  braces += 1 # nyitó: +1
                    if s[closepos] == brclose: braces -= 1 # záró:  -1

                    if braces == 0: 
                        # amikor a braces = 0, akkor megvan a kinyitott zárójel párja
                        # a kettő közti szöveget rekurzívan megvizsgáljuk

                        # ha a megtalált zárójelben lévő szöveg érvénytelen,
                        # akkor nyilván a teljes kifejezés érvénytelen
                        if not self.isValid(s[openpos+1:closepos]): return False

                        # ha érvényes volt a kifejezés, akkor 
                        # megszakítjuk a for ciklust és a záró után 
                        # folytatjuk a keresést a köv. zárójelpárra
                        openpos = closepos + 1
                        break
                    
            # ha nem volt zárójel, akkor csak megyünk egyet előre az
            # openpos változóval       
            else:
            
                openpos += 1

        # a ciklusban feldolgoztunk mindent es nem jött vissza hiba
        # akkor jók vagyunk
        return True

                






testcases = [
    '])}',
    ']',
    '(])',
    '[](',
    '',
    '[(aa){bb}]{ww(qq)}ee',
    '()',
    '([])',
    'ee(()(aa))(eee)',
    '()[]{}',
    '(])',
    '{}'
]

s = Solution()

for case in testcases:
    if s.isValid(case):
        print("\"{c}\" rendben van.".format(c=case))
    else:
        print("\"{c}\" kifejezés hibás.".format(c=case))

# %%