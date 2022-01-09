class Node:
    def __init__(self,sId,sName,sCourse,sYearLevel,mathGrade,cpeGrade,englishGrade,physicsGrade,gpa):
        self.sId = sId
        self.sName = sName
        self.sCourse = sCourse
        self.sYearLevel = sYearLevel
        self.mathGrade =mathGrade
        self.cpeGrade = cpeGrade
        self.englishGrade = englishGrade
        self.physicsGrade = physicsGrade
        self.gpa = gpa  
        self.right = None 
        self.Left = None

class Doubly_Linked_List:
    def __init__(self):
        self.head = None
    def Insert_tail(self,sId,sName,sCourse,sYearLevel,mathGrade,cpeGrade,englishGrade,physicsGrade,gpa):
  
        if self.head is None:
            new_node = Node(sId,sName,sCourse,sYearLevel,mathGrade,cpeGrade,englishGrade,physicsGrade,gpa)
            new_node.left = None
            self.head = new_node
        else:
            new_node = Node(sId,sName,sCourse,sYearLevel,mathGrade,cpeGrade,englishGrade,physicsGrade,gpa)
            n = self.head
            while n.right is not None:
                n = n.right
            n.right = new_node
            new_node.left = n
            new_node.right = None

    def Delete_Record(self,x):
        if self.head is None:
            print("The list has no element to delete")
            return 
        if self.head.right is None:
            if self.head.sId == x:
                self.head = None
            else:
                print("Item not found")
            return 

        if self.head.sId == x:
            self.head = self.head.right
            self.head.left = None
            return

        n = self.head
        while n.right is not None:
            if n.sId == x:
                break;
            n = n.right
        if n.right is not None:
            n.left.right = n.right
            n.right.left = n.left
        else:
            if n.sId == x:
                n.left.right = None
            else:
                print("Element not found")
        
    def Insert_Grades(self,sId,mathGrade,cpeGrade,englishGrade,physicsGrade):
        if self.head is None:
            print("The list has no element to delete")
            return
        
        if self.head.sId == sId:
                self.head.mathGrade = mathGrade
                self.head.cpeGrade = cpeGrade
                self.head.englishGrade = englishGrade
                self.head.physicsGrade = physicsGrade
               
                return
             
        n = self.head
        while n is not None:
            print(n.sId,' == ',sId)
            if n.sId == sId:
                
                n.mathGrade = mathGrade
                n.cpeGrade = cpeGrade
                n.englishGrade = englishGrade
                n.physicsGrade = physicsGrade
                return
            n = n.right
        if n == None:
            print("Student not found")
            return
            
    def Invalid_Duplicates(self, sId):

        n = self.head
        while n is not None:
            if n.sId == sId:
                return True
            n = n.right
        
        return False
    def Compute_Gpa(self):
        n = self.head
        while n is not None:
            n.gpa = (n.mathGrade * 3 + n.cpeGrade * 4 + n.englishGrade * 3 + n.physicsGrade * 4) / (3 + 4 + 3 + 4)
            n = n.right
        print('Compute Successful')
        
                   
    def Traverse(self):
        if self.head is None:
            print('No Student Record')
            return
        n = self.head
        while n is not None:
            print('------------------------------')
            print('\nID NUMBER: ',n.sId,'\nNANE: ',n.sName,'\nCOURSE: ',n.sCourse,'\nYEAR LEVEL: ',n.sYearLevel,'\nMATH: ',n.mathGrade,'\nCPE: ',n.cpeGrade,'\nENGLISH: ',n.englishGrade,'\nPHYSICS: ',n.physicsGrade,'\nGPA: ',round(n.gpa,2),'\n')
            n = n.right
        print('------------------------------')
    def Traverse_HighestGPA(self):
        if self.head is None:
            print('No Student Record')
            return
        n = self.head
        highest = n.gpa
        while n is not None:
            if n.gpa != 0.0:
                print('------------------------------')
                print('\nID NUMBER: ',n.sId,'\nNANE: ',n.sName,'\nCOURSE: ',n.sCourse,'\nYEAR LEVEL: ',n.sYearLevel,'\nMATH: ',n.mathGrade,'\nCPE: ',n.cpeGrade,'\nENGLISH: ',n.englishGrade,'\nPHYSICS: ',n.physicsGrade,'\nGPA: ',round(n.gpa,2))
                if highest < n.gpa:
                    highest = n.gpa
                    print('Highest GPA\n')
            n = n.right
                
            
        print('------------------------------')
    
            


     
list = Doubly_Linked_List()
print('STUDENT DATABASE PROGRAM by Millborne A. Galamiton')
while True:
    print()
    choice = int(input('1.ADD STUDENT \n2.ADD GRADES \n3.COMPUTE GPA \n4.DELETE STUDENT RECORD\n5.DISPLAY STUDENT RECORD\n6.DISPLAY STUDENT RECORD(with GPA)\n7.Exit\nEnter choice: '))
    
    if choice == 1:
        print()
        while True:
            ID = input('Enter ID: ')
            c = list.Invalid_Duplicates(ID)
            if c == False:
                break
            else:
                print('Invalid Duplicate ID Number')
        Name = input('Enter Name: ')
        Course = input('Enter Course: ')
        Year = input('Enter Year: ')
        list.Insert_tail(ID,Name,Course,Course,0.00,0.00,0.00,0.00,0.00)
        

    elif choice == 2:
        print()
        ID = input('Enter ID: ')
        c = list.Invalid_Duplicates(ID)
        if c == True: 
            math = float(input('Enter Math grade: '))
            cpe = float(input('Enter CPE grade: ') )
            english = float(input('Enter English grade: ') )
            physics = float(input('Enter Physics grade: ')) 
            list.Insert_Grades(ID,math,cpe,english,physics)
        else:
            print('Student not Found')
       
        
    elif choice == 3:
        print()
        list.Compute_Gpa()
        
    elif choice == 4:
        print()
        ID = input('Enter ID Number: ')
        list.Delete_Record(ID)
        
    elif choice == 5:
        print()
        list.Traverse()
    elif choice == 6 :
        print()
        list.Traverse_HighestGPA()
    else:break
        
            
        
        
        
        
        

        
        
        
        

   
        
        