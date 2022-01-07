first of all in info.txt file some students have 3 names, a first name, a middle name and a last name, i will be taking only first name and middle name or may be last name or someone's gender ? do i care ? no !

What we have rn
line sl no., registrtion. no, branch roll no. ,section roll no, name, gender and category

the list we want
registrtion. no, branch roll no. ,section roll no, name,

lets code !

Now i want second sem marks along with registration no and section roll no. sooo....

list we have have
Unordered serial no, Reg. no, Section Rollno, Name, first sem marks, second sem marks, passed/supply/left some exm

list we want
Reg. no, Section Rollno, Name, first sem marks, second sem marks,

lets code !


Learnt a lot of things rn btw, you cant use nested loops on files you have to close the file with every iteration of the loop which will only make my problem more complex so i decided to make Pyhton Objects  which will have serialised serial no as their key and will contain data 

So i did this for the info and marks file , and now i had infoMap and marksMap, now it was time to loop over them and concatenate them,

i matched the Unique Id i.e registration no. and appended it to resultsMap which has 2nd sem's marks s the key, and contains the following data registration no, section roll no, name and second sem marks, now there are some places where you will find names of some subjects and thats okay, because its of those students who have not given their exams correctly and they dont have their 2nd sem marks so i will have to ignore those cases in the final list which will be ready in next commit, you may think im giving an excuse, but that's not the case, im just telling that i cant be done because i dont have their second sem marks ! (Our Lovely Institute gives us the result in PDF format which you cant sort by any means and that is the reason why im writing some code here!)