from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools
from requests import HTTPError
import json
import time

from service_builder import ServiceBuilder

FORM_IDS = ["1u6EXUqfPgb3KvjrwkI-o-oL_EGB1FWmru7VVnsXgolk",
               "17DgT-8UA0xgf9OhDQ15uVNrrqsLedPolg3Ep7DYoUms"]

def main():
    service = ServiceBuilder().service
    
    maxIter = 100
    for i in range(maxIter):
        answerDict = getAnswers(service, FORM_IDS)
        answerList = []

        for formKey in answerDict:
            processedAnswers = processAnswer(answerDict[formKey])

            answerList.append(processedAnswers)

        print(f"Final answer list: {answerList}")

        print(f"Completed action {i+1}/{maxIter}")
        if i != maxIter-1:
            print("Sleeping for 1 min")
            time.sleep(60)

def gatherData() -> list:
    service = ServiceBuilder().service
    
    answerDict = getAnswers(service, FORM_IDS)
    answerList = []

    for formKey in answerDict:
        processedAnswers = processAnswer(answerDict[formKey])

        answerList.append(processedAnswers)
        
    return answerList

def processAnswer(ansList) -> dict:
    res = {}
    for ans in ansList:
        if not ans in res:
            res[ans] = 1
        else:
            res[ans] += 1


    return res


def getAnswers(service, formIDs) -> dict:

    finalAnswerList = {}

    try:
        for form_id in formIDs:
            formAnsList = []
            result = service.forms().responses().list(formId=form_id).execute()
            for response in result['responses']:
                ansObjList = list(response['answers'].values())
                answer = list(
                    map(lambda objList: objList['textAnswers']['answers'][0]['value'], ansObjList))[0]
                formAnsList.append(answer)
            finalAnswerList[form_id] = formAnsList

    except HTTPError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')

    return finalAnswerList


if __name__ == '__main__':
    main()
