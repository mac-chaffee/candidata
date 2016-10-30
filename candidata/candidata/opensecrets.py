import requests

def getContributionsByIssue(candidateString, issueString):

    # Pretend the issueString leads to this array of industry codes
    industries = ["H01", "W06", "H02"]

    contributionsByIndustry = {}

    # Loop through all industries that are tied to the given issue
    for industryString in industries:
        args = {
            "method": "CandIndByInd",
            "apikey": "aa677ff4c6fe947883bcfa3e844df599",
            "cid": candidateString,
            "ind": industryString,
            "cycle": "2016",
            "output": "json"
        }
        r = requests.get("http://www.opensecrets.org/api/", args)
        r = r.json()

        # Get the title of the industry and their contribution to the candidate campaign
        industryTitle = r ["response"] ["candIndus"] ["@attributes"] ["industry"]
        contribution = r ["response"] ["candIndus"] ["@attributes"] ["total"]
        contributionsByIndustry [industryTitle] = int(contribution)

    print(contributionsByIndustry)
    return contributionsByIndustry

# Test
getContributionsByIssue("N00000019", None)
