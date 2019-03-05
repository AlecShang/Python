

import sys

print('aaa')
class StudentPython():
    student_number = '001'
    student_age = '18'
    student_major = 'computer'

    def DoHomework(self):
        print('please do homework!')
        print('then you can play!')
        
        return None


shang = StudentPython()
print(shang.student_age)
print(shang.DoHomework())
print(StudentPython.__dict__)

