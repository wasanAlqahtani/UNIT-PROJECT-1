# UNIT-PROJECT-1

## Based on what you’ve learned until now , create a project of your choosing (impress us with your imagination) . This project must at least satisfy the following minimum requirements :

- Must be interactive on CLI.
- Use your coding skills in Python accurately.
- Organize Your Code into modules & (or packages)
- Use git & Github to track changes in your code.

## Project :  Quiz System :

#### Overview : A Python-based quiz system that uses OpenAI to generate quiz questions, assigns to users  unique codes, and allows the Teachers to create and track quizzes statistics. And Students to take quizzes, get scores, and receive improvement tips. 

### Features & User Stories
#### As a Teacher  I should be able to do the following :
- Login / register (store new teacher in teacher.json). 
- Generate questions using OpenAI, the teacher can only type the subject and the number of questions. 
- Assign a code to each quiz. 
- View student performance:
  - who take the quiz 
  - display each student and the score .
  - who failed, successed in each question. 
- store the questions in question.json. 

#### As a Student  I should be able to do the following :
- Login / register (store new student in student.json). 
- Take quiz by entering quiz code 
- Answer the questions 
- Earn scores 
- Get some helful tips from OpenAI depends on your weekness (Answers)
- After Answering , the score will updates in student.json
- display total score 


#### Usage :
#### Method and usage: 

 - #### Fisrt the program will display menue to choose if you student or teacher --> type 1 if you teacher / type 2 if you student : 
    
   - #### Teacher : 
       then the program will display login page 
     - type 1 to Login by entering email and password. 
     - type 2 to register by entering (name,Id email,password,subject)
       
       After that the program wil display teacher menu
     - type 1 to Generate question by entering the subject and number of questionas. : 
            this will generate unique code and generate questions using OpenAI 
     - type 2 to Show student in details : 
           this will display name of students and thier scores on specific quiz code. 
     - type 3 to Show Statistics:
           this will display each question who sucessed and who failed in specific quiz code
     - type 4 to exit from teacher menue

   - #### Student : 
       then the program will display login page 
     - type 1 to Login by entering email and password. 
     - type 2 to register by entering (name,Id email,password)
      
       After that the program wil display student menu
     - type 1 to Take quiz : 
       this will let the student take the exam depends on the code and after that if the student failed on something , OpenAi will generate helful tips to improve. 
    - type 2 to Show total score : 
           this will display total student score. 
    - type 3 to exit from student menu 

