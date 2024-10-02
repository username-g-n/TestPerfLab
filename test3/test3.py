import json

def inputJson(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def resultCreating(tests, idAndValue):
    for test in tests:
        testId = test.get('id')
        if testId in idAndValue:
            test['value'] = idAndValue[testId]
        if 'values' in test:
            resultCreating(test['values'], idAndValue)

def dumpJson(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def main():
    testsFile = 'tests.json'
    valuesFile = 'values.json'
    reportFile = 'report.json'
    testsData = inputJson(testsFile)
    valuesData = inputJson(valuesFile)
    idAndValue = {result['id']: result['value'] for result in valuesData['values']}
    resultCreating(testsData['tests'], idAndValue)
    dumpJson(testsData, reportFile)

if __name__ == "__main__":
    main()
    input('Press ENTER to exit')
