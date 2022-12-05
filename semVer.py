import argparse

def getMajor(currentVer):
    #Remove v and split the version nummber
    myVersion = currentVer.replace("v","").split(".")
    #Increment the major by 1
    incrementmajor = int(myVersion[0]) + 1
    #Reconstruct and return semver with incremented major
    print("version is major")
    returnedVer = "v" + str(incrementmajor) + ".0.0"
    print(returnedVer)
    return returnedVer

def getMinor(currentVer):
    #Split the version nummber
    myVersion = currentVer.split(".")
    #Increment the minor by 1
    incrementMinor = int(myVersion[1]) + 1
    #Reconstruct and return semver with incremented minor
    returnedVer = str(myVersion[0]) + "." + str(incrementMinor) + ".0"
    print(returnedVer)
    return returnedVer

def getHotfix(baseVersion):
    if len(str(baseVersion)) > 4:
        #Split the base version nummber
        myVersion = baseVersion.split(".")
        #Increment the hotfix by 1
        incrementHotfix = int(myVersion[2]) + 1
        #Reconstruct and return semver with incremented hotfix
        returnedVer = str(myVersion[0]) + "." + str(myVersion[1])  + "." +  str(incrementHotfix)
        print(returnedVer)
        return returnedVer
    else:
        return "No base version found. please re-run with the base version populated"
        

def generateSemVer(currentVer, versionType, baseVersion = None):
    #Handle scenerio where no tag is found
    if (len(currentVer) > 4):
        #Handle scenerio where no version tag is found
        if (currentVer.startswith("v")):
            #Increment major version if versiontype == major
            if versionType == "major":
                return getMajor(currentVer)
            #Increment major version if versiontype == minor
            elif(versionType == "minor"):
                return getMinor(currentVer)
            #Increment major version if versiontype == hotfix
            elif(versionType == "hotfix"):
                return getHotfix(baseVersion)
        else:
            print ("incompatible version found")
            return "v1.0.0"
    else:
        print ("No tag found found")
        return "v1.0.0"


parser = argparse.ArgumentParser()
parser.add_argument('--currentVersion', type=str, required=True)
parser.add_argument('--versionType', type=str, required=True)
parser.add_argument('--baseVersion', type=str, required=False)
args = parser.parse_args()

if __name__ == "__main__":
    generateSemVer(str(args.currentVersion).lower(), str(args.versionType).lower(), str(args.baseVersion).lower())