import json
import requests

def getUserData():

    while True:

        id = input("Please enter your id number: ")
        cell_number = input("Please enter your cell number: ")

        if id.isalpha():
            id = input("Please enter your valid id number: ")
        elif cell_number.isalpha():
            cell_number = input("Please enter your valid cell number: ")
        else:
            return id, cell_number


def getStatus(id, cell_number):

    url = f'https://srd.sassa.gov.za/srdweb/api/web/outcome/{id}/{cell_number}'
    fetch = requests.get(url)
    results = fetch.json()
    writeToFile(results)

    return results

def writeToFile(data):
    with open('results.json', 'w') as file:
        file.write(json.dumps(data))

def monthFormatter(date):
    months = {"JAN" : "JANUARY", "FEB" : "FEBUAURY", "MAR" : "MARCH", "APR" : "APRIL", "MAY" : "MAY", "JUN" : "JUNE", "JUL" : "JULY", "AUG" : "AUGUST", "SEP" : "SEPTEMBER", "OCT" : "OCTOBER", "NOV" : "NOVEMBER", "DEC" : "DECEMBER"}
    date = months[date[0:3]]

    return date

def getApprovedOutcome(id, cell_number):
    results = getStatus(id, cell_number)
    outcomes = results["outcomes"]

    approvedMonths = []

    for everyOutcome in outcomes:
        if everyOutcome["outcome"] == "approved":
            approvedMonths.append(monthFormatter(everyOutcome["period"]))

    print(approvedMonths)

    return approvedMonths


def getDeclinedOutcome(id, cell_number):
    results = getStatus(id, cell_number)
    outcomes = results["outcomes"]

    declinedMonths = []

    for everyOutcome in outcomes:
        if everyOutcome["outcome"] == "declined":
            declinedMonths.append(monthFormatter(everyOutcome["period"]))

    print(declinedMonths)

    return declinedMonths



id, cell_number = getUserData()
getDeclinedOutcome(id, cell_number)