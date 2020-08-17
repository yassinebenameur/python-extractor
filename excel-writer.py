from openpyxl import Workbook

from main import DOC, TestCase

wb = Workbook()

ctf_file = open("test.tcf", "r")
doc = DOC()
doc.extract_doc_atrributes(ctf_file.read())
ctf_file = open("test.tcf", "r")
TestCase(doc).extract_test_case(ctf_file.read())
doc.print_information()

# grab the active worksheet
ws = wb.active

ws['B2'] = 'XLStoTCF_ISIT'
ws['C2'] = doc.version

ws.merge_cells('B4:F4')
ws['B4'] = 'Test Sequence Attributes'

ws['B5'] = 'Sequence Name'
ws['C5'] = doc.sequenceName

ws['B6'] = 'Sequence Documentation'
ws['C6'] = doc.sequenceDocumentation

ws['B7'] = 'Developer Name'
ws['C7'] = doc.developerName

ws['B8'] = 'Tester Name'
ws['C8'] = doc.testerName

ws['B9'] = 'Creation Date'
ws['C9'] = doc.creationDate

ws['B10'] = 'Procedure'
ws['C10'] = doc.procedure

ws['B11'] = 'Procedure Number'
ws['C11'] = doc.procedureNumber

ws['B12'] = 'Source File'
ws['C12'] = doc.sourceFile

ws['B13'] = 'Language'
ws['C13'] = doc.language

ws['B14'] = 'Coverage Mode'
ws['C14'] = doc.coverageMode

ws['B15'] = 'Additional Files or Procedures'
ws['C15'] = doc.additionalFiles

ws['B55'] = 'Test Case Data Sets'


print(len(doc.test_cases[0].input_variables))
current = 56
for idx, variable in enumerate(doc.test_cases[0].input_variables):
    row = 56 + idx * 6
    pos = 'B' + str(row)
    ws[str(pos)] = 'Input Variable ' + str(idx + 1)

    pos = 'C' + str(row + 1)
    ws[str(pos)] = 'Name '

    pos = 'C' + str(row + 2)
    ws[str(pos)] = 'Type '

    pos = 'C' + str(row + 3)
    ws[str(pos)] = 'Usage '

    pos = 'C' + str(row + 4)
    ws[str(pos)] = 'Value '

    pos = 'C' + str(row + 5)
    ws[str(pos)] = 'Value Retained ? '

    current = row

for idx, variable in enumerate(doc.test_cases[0].output_variables):
    row = current + (idx+1) * 7
    pos = 'B' + str(row)
    ws[str(pos)] = 'Output Variable' + str(idx + 1)

    pos = 'C' + str(row + 1)
    ws[str(pos)] = 'Name '

    pos = 'C' + str(row + 2)
    ws[str(pos)] = 'Type '

    pos = 'C' + str(row + 3)
    ws[str(pos)] = 'Usage '

    pos = 'C' + str(row + 4)
    ws[str(pos)] = 'Value '

    pos = 'C' + str(row + 5)
    ws[str(pos)] = 'Comparison '

    pos = 'C' + str(row + 6)
    ws[str(pos)] = 'TBrun Analysis'

col = 'D'
# for test_case in doc.test_cases:
#     row = 57
#
#     for input_variable in test_case.input_variables:
#         ws[col + str(row)] = input_variable.Name
#         ws[col + str(row + 1)] = input_variable.Type
#         ws[col + str(row + 2)] = input_variable.Usage
#         ws[col + str(row + 3)] = input_variable.Value
#         row = row + 6
#     row = current+1
#     for output_variable in test_case.output_variables:
#         ws[col + str(row)] = output_variable.Name
#         ws[col + str(row+1)] = output_variable.Type
#         ws[col + str(row+2)] = output_variable.Usage
#         ws[col + str(row+3)] = output_variable.Value
#         row = row + 7
#
#     col = chr(ord(col) + 1)

wb.save('sample.xlsx')
