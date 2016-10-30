import requests

# correct discrepencies betwwen APIs
candidateMap = {
    "hillary-clinton": "hillary-clinton",
    "donald-trump": "donald-trump",
    "gary-johnson": "gary-johnson"
}
issueMap = {
    "Health Care": "health-care",
    "Economy": "economy",
    "Terrorism": "terrorism",
    "Environment": "environment"
}

def getRecentStatementRulings(candidateString, issueString):

    # object for storing statements and rulings
    statementsAndRulings = {}

    # set up API call
    args = {
        "order_by": "ruling_date",
        "speaker__name_slug": candidateString,
        "subject__subject_slug": issueMap[issueString],
        "limit": 5,
        "format": "json"
    }
    r = requests.get("http://www.politifact.com/api/v/2/statement/", args)
    r = r.json()

    # loop through the 5 statements/rulings we want to use
    for i in range(len(r["objects"])):

        # get the statements and rulings...
        statement = r ["objects"] [i] ["statement"]
        ruling = r ["objects"] [i] ["ruling"] ["ruling"]

        # ...and put them in the object
        statementsAndRulings [i] = [statement, ruling]

    print(statementsAndRulings)
    return statementsAndRulings

def getRecentStatements(candidateString):

    # object for storing statements and rulings
    statementsAndRulings = {}

    # set up API call
    args = {
        "order_by": "ruling_date",
        "speaker__name_slug": candidateString,
        "limit": 5,
        "format": "json"
    }
    r = requests.get("http://www.politifact.com/api/v/2/statement/", args)
    r = r.json()

    # loop through the 5 statements/rulings we want to use
    for i in range(len(r["objects"])):

        # get the statements and rulings...
        statement = r ["objects"] [i] ["statement"]
        ruling = r ["objects"] [i] ["ruling"] ["ruling"]

        # ...and put them in the object
        statementsAndRulings [i] = [statement, ruling]

    return statementsAndRulings

#getRecentStatements("hillary-clinton")
