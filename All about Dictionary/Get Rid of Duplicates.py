# First, create a dictionary that consists of id, name, grade and subject integration of students. Then, write a program to retrieve unique entries and eliminate the rest

student_data = {

'001':{'name': ['joyce'], 'grade': [5],'subjects' : ['english, math, science'] },


'002':{'name': ['john'], 'grade': [5],'subjects' : ['english, math, science'] },


'003':{'name': ['james'], 'grade': [5],'subjects' : ['english, math, science']},


'004':{'name': ['jack'], 'grade': [5],'subjects' : ['english, math, science'] }


}

result = {}

for key,value in student_data.items():

    if value not in result.values():

        result[key] = value

print(result)