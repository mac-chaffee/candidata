import os
import json
import requests

candidateToIDMap = {
    "hillary-clinton": "N00000019",
    "donald-trump": "N00023864",
    "gary-johnson": "N00033226"
}

issueToIndustryMap = {
    "Health Care": ["H01", "H02", "H03", "H04"],
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
            "apikey": "f917920880a3cb2dde278f3565c3defe",
            "cid": candidateToIDMap [candidateString],
            "ind": industryString,
            "cycle": "2016",
            "output": "json"
        }
        r = requests.get("http://www.opensecrets.org/api/", args)
        if r.status_code == 404:
            continue
        r = r.json()

        # Get the title of the industry and their contribution to the candidate campaign
        industryTitle = r ["response"] ["candIndus"] ["@attributes"] ["industry"]
        contribution = r ["response"] ["candIndus"] ["@attributes"] ["total"]

        contributionsByIndustry.append(
            {
                "industryTitle": industryTitle,
                "contribution": int(contribution)
            }
        );

    current_dir = os.path.dirname(__file__)
    file = os.path.join(current_dir, "data", "os-%s-%s.json" % (candidateString, issueString))
    with open(file, mode="w") as jsonfile:
        json.dump(contributionsByIndustry, jsonfile)

def getTopContributors(candidateString):

    # A list of dictionaries in the form {industryTitle: value, contribution: value}
    contributionsByIndustry = []

    args = {
        "method": "candIndustry",
        "apikey": "f917920880a3cb2dde278f3565c3defe",
        "cid": candidateToIDMap [candidateString],
        "cycle": "2016",
        "output": "json"
    }
    r = requests.get("http://www.opensecrets.org/api/", args)
    print(r)
    if r.status_code == 404:
        return []
    r = r.json()

    # Get the industries
    industries = r ["response"] ["industries"] ["industry"]
    for industry in industries:
        industryTitle = industry ["@attributes"] ["industry_name"]
        contribution = industry ["@attributes"] ["total"]

        contributionsByIndustry.append(
            {
                "industryTitle": industryTitle,
                "contribution": int(contribution)
            }
        );

    current_dir = os.path.dirname(__file__)
    file = os.path.join(current_dir, "data", "ostop-%s.json" % (candidateString))
    with open(file, mode="w") as jsonfile:
        json.dump(contributionsByIndustry, jsonfile)

current_dir = os.path.dirname(__file__)

for name in candidateToIDMap:
    getTopContributors(name)
    for key, val in issueToIndustryMap.items():
        getContributionsByIssue(name, key)
