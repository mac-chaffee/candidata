import json
import os


def read_recent_statements(candidateString, issueString):
    current_dir = os.path.dirname(__file__)
    file = os.path.join(current_dir, "data", "pf-%s-%s.json" % (candidateString, issueString))
    with open(file, mode="r") as jsonfile:
        return json.load(jsonfile)

def read_recent_statements_front(candidateString):
    current_dir = os.path.dirname(__file__)
    file = os.path.join(current_dir, "data", "pf-recent-%s.json" %(candidateString))
    with open(file, mode="r") as jsonfile:
        return json.load(jsonfile)
