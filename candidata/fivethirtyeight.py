import requests

# correct discrepencies betwwen APIs
candidateMap = {
    "hillary-clinton": "D",
    "donald-trump": "R",
    "gary-johnson": "L"
}

def getPollNum(candidateString):

    # set up API call
    r = requests.get("http://projects.fivethirtyeight.com/2016-election-forecast/US.json")
    r = r.json()

    # get current polling average
    currentPollNum = int(r["forecasts"]["latest"][candidateMap[candidateString]]["models"]["polls"]["forecast"])

    print(currentPollNum)
    return currentPollNum
