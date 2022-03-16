class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:

        rec = []
        res = {}
        
        for file in names :
            if file in res :
                n = res[file]
                tmp = file+'('+ str(n) +')'
                while tmp in res :
                    n += 1
                    tmp = file+'('+ str(n) +')'
                rec.append(tmp)
                res[tmp] = 1
                res[file] += 1
            else :
                res[file] = 1
                rec.append(file)
                    
        return rec
