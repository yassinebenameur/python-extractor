import re
from typing import List
from unittest import result

pattern_test_case = "(# Begin Test Case)([\s\S]*?)(# End Test Case)"
pattern_variable_in_test_case = "(# Begin Variable)([\s\S]*?)(# End Variable)"
pattern_attributes = "(# Begin Attributes)([\s\S]*?)(# End Attributes)"
pattern_text = "(# Begin Text)([\s\S]*?)(# End Text)"
pattern_white_files = "(# Begin White Files)([\s\S]*?)(# End White Files)"
pattern_isolated_procedure = "(# Begin Isolated Procedure)([\s\S]*?)(# End Isolated Procedure)"
pattern_properties = "(# Begin Properties)([\s\S]*?)(# End Properties)"
pattern_Tc_Stub="(# Begin TC Stub)([\s\S]*?)(# End TC Stub)"




class Variable:
    pattern_NAME_variable_in_attribute = "(Name =)([\s\S]*?)(\n)"
    pattern_TYPE_variable_in_attribute = "(Decl_type =)([\s\S]*?)(\n)"
    pattern_USAGE_variable_in_attribute = "(Usage =)([\s\S]*?)(\n)"
    pattern_VALUE_variable_in_attribute = "(Value =)([\s\S]*?)(\n)"

    def __init__(self):
        self.Name = ''
        self.Type = ''
        self.Usage = ''
        self.Value = ''

    def extract_variable_attributes(self, chaine):
        name = re.findall(Variable.pattern_NAME_variable_in_attribute, str(chaine))
        type = re.findall(Variable.pattern_TYPE_variable_in_attribute, str(chaine))
        usage = re.findall(Variable.pattern_USAGE_variable_in_attribute, str(chaine))
        value = re.findall(Variable.pattern_VALUE_variable_in_attribute, str(chaine))
        input_variable = Variable()
        input_variable.Name = name[0][1].strip()
        input_variable.Type = type[0][1].strip()
        input_variable.Usage = usage[0][1].strip()
        input_variable.Value = value[0][1].strip()
        return input_variable



class TC_Hit_Count:


    pattern_Hit_Count_Setting = "(Setting =)([\s\S]*?)(\n)"
    pattern_Hit_Count_specified = "(specified =)([\s\S]*?)(\n)"

    def __init__(self):
        self.Setting=''
        self.specefied=''

    def extract_TC_Hit_Count_attributes(self, chaine):
        Setting=re.findall(TC_Hit_Count.pattern_Hit_Count_Setting,str(chaine))
        specified=re.findall(TC_Hit_Count.pattern_Hit_Count_specified,str(chaine))
        new=TC_Hit_Count()
        new.Setting=Setting[0][1].strip
        new.specefied=specified[0][1].strip

        return new


class TC_Input_Parameters:

    pattern_TC_Input_Parameters_Name="(Name =)([\s\S]*?)(\n)"
    pattern_TC_Input_Parameters_Type= "(Type =)([\s\S]*?)(\n)"
    pattern_TC_Input_Parameters_value = "(value =)([\s\S]*?)(\n)"
    pattern_TC_Input_Parameters_compare = "(compare =)([\s\S]*?)(\n)"

    def __init__(self):
        self.Name=''
        self.Type=''
        self.value=''
        self.compare=''


    def extract_Input_Parameters(self,chaine):
        Name = re.findall(TC_Input_Parameters.pattern_TC_Input_Parameters_Name, str(chaine))
        type = re.findall(TC_Input_Parameters.pattern_TC_Input_Parameters_Type, str(chaine))
        Value = re.findall(TC_Input_Parameters.pattern_TC_Input_Parameters_value, str(chaine))
        compare = re.findall(TC_Input_Parameters.pattern_TC_Input_Parameters_compare, str(chaine))
        new = TC_Input_Parameters()
        new.Name = Name[0][1].strip
        new.Type = type[0][1].strip
        new.value = Value[0][1].strip
        new.compare = compare[0][1].strip
        new.Name = Name[0][1].strip


class Return_Value:

    pattern_Return_Value_Name = "(Name =)([\s\S]*?)(\n)"
    pattern_TC_Input_Parameters_Type = "(Type =)([\s\S]*?)(\n)"
    pattern_TC_Input_Parameters_value = "(value =)([\s\S]*?)(\n)"

    def __init__(self):
        self.Name=''
        self.Type=''
        self.Value=''

    def extract_TC_Input_Return_Value_attributes(self, chaine):
        Name = re.findall(Return_Value.pattern_Return_Value_Name, str(chaine))
        type = re.findall(Return_Value.pattern_TC_Input_Parameters_Type, str(chaine))
        Value = re.findall(Return_Value.pattern_TC_Input_Parameters_value, str(chaine))
        compare = re.findall(TC_Input_Parameters.pattern_TC_Input_Parameters_compare, str(chaine))
        new = Return_Value()
        new.Name = Name[0][1].strip
        new.Type = type[0][1].strip
        new.value = Value[0][1].strip

        return new


class TC_Stub:

    pattern_Procedure_tcstub = "(Procedure =)([\s\S]*?)(\n)"
    pattern_Procedure_tcstub = "(Hit Order =)([\s\S]*?)(\n)"
    pattern_Overloading_tcstub = "(# Begin Overloading)([\s\S]*?)( # End Overloading)"


    def __init__(self):
        self.Procedure=''
        self.Hit_order=''
        self.Overloading=''
        self.overload=''
        self.Hit_count:List[TC_Hit_Count]
        self.Input:List[TC_Input_Parameters]
        self.Return_Value:List[Return_Value]




class TestCase:
    pattern_DESCRIPTION_in_test_case = "(Description = )([\s\S]*?)(\n)"

    def __init__(self, doc):
        self.input_variables: List[Variable] = []
        self.output_variables: List[Variable] = []
        self.TCstub: List[TC_Stub]
        self.Name = ''
        self.Documentation = ''
        self.doc = doc



    def extract_test_case(self, chaine):

        result = re.findall(pattern_test_case, chaine)
        for i, test_case in enumerate(result):
            new_test_case = TestCase(self.doc)
            test_case_result = test_case[1]
            temp = re.search(TestCase.pattern_DESCRIPTION_in_test_case, test_case_result).group(2)
            new_test_case.Name = temp.strip()

            temp2 = re.search(pattern_text, test_case_result).group(2)
            new_test_case.Documentation = temp2.strip()
            result2 = re.findall(pattern_variable_in_test_case, test_case_result)


            for j, input_variable in enumerate(result2):
                new_variable = Variable().extract_variable_attributes(input_variable[1])

                if (new_variable.Usage =='G'):
                    new_test_case.input_variables.append(new_variable)
                else:
                    new_test_case.output_variables.append(new_variable)


            self.doc.test_cases.append(new_test_case)


class DOC:
    pattern_SEQUENCE_NAME_in_attribute = "(Sequence Name =)([\s\S]*?)(\n)"
    pattern_VERSION_in_attribute = "(Language Code =)([\s\S]*?)(\n)"
    pattern_DEVELOPER_in_attribute = "(Developer :)([\s\S]*?)(\n)"
    pattern_TESTER_in_attribute = "(Tester :)([\s\S]*?)(\n)"
    pattern_FILE_in_attribute = "(File =)([\s\S]*?)(\n)"
    pattern_PROCEDURE_in_attribute = "(Procedure =)([\s\S]*?)(\n)"
    pattern_PROCEDURE_NUMBER_in_attribute = "(Procedure Number =)([\s\S]*?)(\n)"
    pattern_CREATION_DATE_in_attribute = "(Creation Date =)([\s\S]*?)(\n)"
    pattern_COVERAGE_MODE_in_attribute = "(IBox = )([\s\S]*?)(\n)"

    test_cases: List[TestCase] = []
    TC_Stubs:List[TC_Stub]= []

    def __init__(self):
        self.procedure = ''
        self.sequenceName = ''
        self.sequenceDocumentation = ''
        self.developerName = ''
        self.testerName = ''
        self.creationDate = ''
        self.procedureNumber = ''
        self.sourceFile = ''
        self.language = ''
        self.coverageMode = ''
        self.additionalFiles = ''
        self.version = ''

    def extract_doc_atrributes(self, chaine):
        attributes = re.findall(pattern_attributes, str(chaine))

        attributesString = attributes[0][1]


        result2 = re.findall(DOC.pattern_SEQUENCE_NAME_in_attribute, attributesString)
        print("************************************************************************")
        print(result2)
        result3 = result2[0][1]
        print(result3)
        self.sequenceName = result3.strip()

        result2 = re.findall(DOC.pattern_VERSION_in_attribute, attributesString)
        result3 = result2[0][1]
        self.version = 'Version ' + result3

        temp = re.findall(pattern_text, str(chaine))
        temp2 = temp[0][1]
        temp3 = re.findall(DOC.pattern_DEVELOPER_in_attribute, temp2)
        temp4 = re.findall(DOC.pattern_TESTER_in_attribute, temp2)

        self.developerName = temp3[0][1].strip()
        self.testerName = temp4[0][1].strip()

        temp = re.search(pattern_test_case, chaine)
        print(temp[0])
        temp1 = temp[0]
        print(temp1)
        temp2 = re.search(DOC.pattern_CREATION_DATE_in_attribute, temp1).group(2)

        self.creationDate = temp2.strip()

        temp2 = re.search(DOC.pattern_PROCEDURE_in_attribute, temp1).group(2)
        self.procedure = temp2.strip()

        temp2 = re.search(DOC.pattern_PROCEDURE_NUMBER_in_attribute, temp1).group(2)
        self.procedureNumber = temp2.strip()

        temp2 = re.search(DOC.pattern_FILE_in_attribute, temp1).group(2)
        self.sourceFile = temp2.strip()

        temp = re.search(pattern_white_files, chaine)
        temp1 = temp[2].strip()
        self.additionalFiles = temp1.split('\n')[1]

        temp = self.sourceFile.split('.')[1].upper()
        self.language = temp.strip()
        temp = re.search(pattern_properties, chaine).group(2)
        temp2 = re.search(DOC.pattern_COVERAGE_MODE_in_attribute, temp).group(2)
        self.coverageMode = temp2.strip()

    def print_information(self):
        print('\n')
        print('XLStoTCF_ISIT    :', self.version)
        print('***** Test Sequence Attributes *****')
        print('Developer Name    :', self.developerName)
        print('Sequence Documentation    :', self.sequenceDocumentation)
        print('Tester Name    :', self.testerName)
        print('Creation Date    :', self.creationDate)
        print('Procedure    :', self.procedure)
        print('Procedure Number    :', self.procedureNumber)
        print('Source File    :', self.sourceFile)
        print('Language   :', self.language)
        print('Coverage Mode   :', self.coverageMode)
        print('Additional Files or Procedures   :', self.additionalFiles)
        print('\n')

        print('***** Test Case Attributes *****')
        for test_case in self.test_cases:
            print('Name / Description   :' + test_case.Name)
            print('Documentation   :' + test_case.Documentation)

        print('\n')
        print('*************** Test Case Data Sets *****************')

        for idx, test_case in enumerate(self.test_cases):
            print('----****** TEST CASE ' + str(idx + 1) + ' ******----')
            print('\n')

            for idx2, variable in enumerate(test_case.input_variables):
                print('\n')
                print('-- Input Variable ' + str(idx2 + 1) + ' --' + ' ( TEST CASE ' + str(idx + 1) + ' )')
                print('Name :   ', variable.Name)
                print('Type :   ', variable.Type)
                print('Usage :   ', variable.Usage)
                print('Value :   ', variable.Value)
                print('Value Retained ? :   ')
            for idx2, variable in enumerate(test_case.output_variables):
                print('\n')
                print('-- Output Variable ' + str(idx2 + 1) + ' --' + ' ( TEST CASE ' + str(idx + 1) + ' )')
                print('Name :   ', variable.Name)
                print('Type :   ', variable.Type)
                print('Usage :   ', variable.Usage)
                print('Value :   ', variable.Value)
                print('Value Retained ? :   ')

ctf_file = open("test.tcf", "r")

doc = DOC()
doc.extract_doc_atrributes(ctf_file.read())
ctf_file = open("test.tcf", "r")

#TestCase(doc).extract_test_case(ctf_file.read())
doc.print_information()