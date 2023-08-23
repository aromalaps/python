#write a function named "processor_feedback" that takes customer feedback as an argument and 
# categorizes it into positive,neutral,or negative feedback based on keywords.
list=["very","good","best","liked"]
list2=["better","nice"]
list3=["boring","not","bad","waste","dump"]
def process_feedback(customerfdbk):
    for i in list:
      if i in customerfdbk:
         print("positive feedback")
         break
    for i in list2:
      if i in customerfdbk:
        print("neutral feedback")
        break
    for i in list3:
      if i in customerfdbk:
        print("negative feedback")
        break
input="it is a better product"
input=input.split()
process_feedback(input)