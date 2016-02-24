#####               BIA 660 - Week 01 Assignment

#-------------------------PART A -----------------------------
#CALCULATING THE AVERAGE SCORES

Students = [
    ['Sarah K.',10,9,7,9,10,20,19,19,45,92],
['John M.',9,9,8,9,8,20,20,18,43,95],
['David R.',8,7,7,9,6,18,17,17,40,83],
['Joan A.',9,10,10,10,10,20,19,20,47,99],
['Nick J.',9,7,10,10,10,20,20,19,46,98],
['Vicki T.',7,7,8,9,9,17,18,19,44,88]
    ]

#------------------------------------------------------------------
#To calclate the average scores for homeworks and store in a dictionary

Homework1_list=[]
Homeworks =[]

a=1
b=0
i=0
S=0
Average = 0
while i<5:
   while b<6:
      while a<6:
        
         Homework1_list.append(Students[b][a])
         S = S + Students[b][a]
         break
      b=b+1
   Average = round(S/6,2)
   Homeworks.insert(b,Average)
   a=a+1
   i=i+1
   S=0
   b=0

Output_list = {'1.Homework#1':Homeworks[0],
               '2.Homework#2':Homeworks[1],
               '3.Homework#3':Homeworks[2],
               '4.Homework#4':Homeworks[3],
               '5.Homework5':Homeworks[4]}
#print (Output_list)

#------------------------------------------------------------------
#To calclate the average scores for Quizes and store in a dictionary

Quiz1_list=[]
Quizes =[]

a=6
b=0
i=5
Sum = []
S=0
Average = 0
while i<8:
   while b<6:
      while a<9:
        
         Quiz1_list.append(Students[b][a])
         S = S + Students[b][a]
         break
      b=b+1
   Average = round(S/6,2)
   Quizes.insert(b,Average)
   a=a+1
   i=i+1
   S=0
   b=0

Output_list2 = {'6.Quiz#1':Quizes[0],
               '7.Quiz#2':Quizes[1],
               '8.Quiz#3':Quizes[2],
               }
#print (Output_list2)


#------------------------------------------------------------------
#To calclate the average scores for Midterms and store in a dictionary

Midterm_list=[]
a=9
b=0
S=0
Average = 0
while b<6:       
   Midterm_list.append(Students[b][a])
   S = S + Students[b][a]
   b=b+1

Average = round(S/6,2)

Output_list3 = {'9.Midterm#1':Average}
#print (Output_list3)

#------------------------------------------------------------------
#To calclate the average scores for Finals and store in a dictionary

Finals_list=[]
a=10
b=0
S=0
Average = 0
while b<6:       
   Finals_list.append(Students[b][a])
   S = S + Students[b][a]
   b=b+1

Average = round(S/6,2)
Output_list4 = {'Finals#1':Average}

#------------------------------------------------------------------

#Appending all dictionaries together

Averages =Output_list
Averages.update(Output_list2)
Averages.update(Output_list3)
Averages.update(Output_list4)

#To sort the items in order

import operator
sorted_Averages = sorted(Averages.items(), key=operator.itemgetter(0))
print("Average scores",'\n')
import sys
import csv
csv_writer = csv.writer(sys.stdout, delimiter='\t')
csv_writer.writerows(sorted_Averages)

#Creating text file "Averages.txt" t0 store the results
fileobject = open("Averages.txt","w")
fileobject.write("Average scores")
fileobject.write("\n")
fileobject.write("\n".join(map(lambda x: str(x), sorted_Averages)))
fileobject.close()






#-------------------------------PART B---------------------------
#To find the individual scores


criteria = [
    ['Homework',5,10,10],
    ['Quiz',3,20,20],
    ['Midterm',1,50,30],
    ['Final',1,100,40]
    ]


###-------------------------------------------------------------###
#To find the scores on homeworks and store in a list

Stu_Homework=[]
Stu_List=[]

a=0
b=1
i=0
Sum = []
S=0
Percentage = 0
while i<6:
   while b<6:
      while a<6:
         Stu_Homework.append(Students[a][b])
         S = S + Students[a][b]
         
         break
      b=b+1
   Percentage = round(((S/50*0.1)*100),2)
   
   Stu_List.insert(a,Percentage)
   #print(Stu_List)
   a=a+1
   i=i+1
   S=0
   b=1

###----------------------------------------------------------------------###
# To calculate the scores on quizes and store in a list

Stu_Quiz=[]

a=0
b=6
i=0
Sum = []
S=0

while i<6:
   while b<9:
      while a<6:
         Stu_Quiz.append(Students[a][b])
         S = S + Students[a][b]
         
         break
      b=b+1
   Percentage = round(((S/60*0.2)*100),2)
   
   Stu_List.insert(a,Percentage)

   #print(Stu_List)
   a=a+1
   i=i+1
   S=0
   b=6

###-------------------------------------------------------------------------
# To calculate the scores on Midterms and store in the list

Stu_Midterm=[]

a=0
b=9
S=0

while a<6:
   Midterm_list.append(Students[a][b])
   S = S + Students[a][b]
   Percentage = round(((S/50*0.3)*100),2)
   Stu_List.insert(a,Percentage)
   a=a+1
   S=0
  
###-------------------------------------------------------------------------
# To calculate the scores on Finals and store in the list

Stu_Finals=[]

a=0
b=10
S=0

while a<6:

   Midterm_list.append(Students[a][b])
   S = S + Students[a][b]
   Percentage = round(((S/100*0.4)*100),2)
   Stu_List.insert(a,Percentage)
   a=a+1
   S=0

###----------------------------------------------------------------------------
# To calculate the Final score per student and store in a list


i=0
Final=[]
S=0
while i<6:
   S=Stu_List[i]+Stu_List[i+6]+Stu_List[i+12]+Stu_List[i+18]
   Final.insert(i,S)
   i+=1

Output_list = [['Sarah K.',Final[0]],
                ['John M.',Final[1]],
                ['David R.',Final[2]],
                ['Joan A.',Final[3]],
                ['Nick J.',Final[4]],
                ['Vicki T.',Final[5]]
               ]

print('\n',"Finals scores",'\n')
import sys
import csv
csv_writer = csv.writer(sys.stdout, delimiter='\t') #To display the output in table frmat
csv_writer.writerows(Output_list)  #To display the output in table format

#Creating text file "FinalScores.txt" tp store the results
fileobject = open("FinalScores.txt","w")
fileobject.write("Finals scores")
fileobject.write("\n")
fileobject.write("\n".join(map(lambda x: str(x), Output_list)))

#To sort by name
Output_list.sort(key=lambda x:x[0][0])
print('\n',"sorted alphabetically",'\n')
csv_writer = csv.writer(sys.stdout, delimiter='\t')
csv_writer.writerows(Output_list)


fileobject.write("\n")
fileobject.write("\n")
fileobject.write("sorted alphabetically")
fileobject.write("\n")
fileobject.write("\n".join(map(lambda x: str(x), Output_list)))


#To sort by Scores
Output_list.sort(key=lambda x:x[0][2])
print('\n',"sorted by scores",'\n')
csv_writer = csv.writer(sys.stdout, delimiter='\t')
csv_writer.writerows(Output_list)

fileobject.write("\n")
fileobject.write("\n")
fileobject.write("sorted by scores")
fileobject.write("\n")
fileobject.write("\n".join(map(lambda x: str(x), Output_list)))
fileobject.close()

