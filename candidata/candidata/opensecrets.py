import requests

candidateToIDMap = {
    "hillary-clinton": "N00000019",
    "donald-trump": "N00023864",
    "gary-johnson": "N00033226"
}

issueToIndustryMap = {
    "Health Care": ["H01, H02, H03, H04"],
    "Economy": ["F03", "F06", "F07", "F10"],
    "Terrorism": ["D01", "D02", "D03"],
    "Environment": ["E01", "E10"]
}

def getContributionsByIssue(candidateString, issueString):

    # Get a list of industries that correspond to the issueString
    industries = issueToIndustryMap [issueString]

    # A list of dictionaries in the form {industryTitle: value, contribution: value}
    contributionsByIndustry = []
    industryEntry = {}

    # Loop through all industries that are tied to the given issue
    for industryString in industries:
        args = {
            "method": "CandIndByInd",
            "apikey": "0a742eb9c1549ea59ebb9a25bb440de8",
            "cid": candidateToIDMap [candidateString],
            "ind": industryString,
            "cycle": "2016",
            "output": "json"
        }
        r = requests.get("http://www.opensecrets.org/api/", args)
        r = r.json()

        # Get the title of the industry and their contribution to the candidate campaign
        industryEntry = {}
        industryTitle = r ["response"] ["candIndus"] ["@attributes"] ["industry"]
        contribution = r ["response"] ["candIndus"] ["@attributes"] ["total"]

        contributionsByIndustry.append(
            {
                "industryTitle": industryTitle,
                "contribution": int(contribution)
            }
        );

    return contributionsByIndustry

# Test
#getContributionsByIssue("hillary-clinton", "Terrorism")
