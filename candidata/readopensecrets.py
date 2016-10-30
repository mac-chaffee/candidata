import json
import os


def read_contributions(candidateString, issueString):
    current_dir = os.path.dirname(__file__)
    file = os.path.join(current_dir, "data", "os-%s-%s.json" % (candidateString, issueString))
    with open(file, mode="r") as jsonfile:
        return json.load(jsonfile)

def read_contributors(candidateString):
    current_dir = os.path.dirname(__file__)
    file = os.path.join(current_dir, "data", "ostop-%s.json" % (candidateString))
    with open(file, mode="r") as jsonfile:
        return json.load(jsonfile)
