# user="ppyyythhh"
# i=0
# dic={}
# count=1
# while i<len(user):
#     if user[i] in dic:
#         count=1
#         dic.update({user[i]:count})
#     else:
#         count+=1
#         dic.update({user[i]:count})
#     i+=1
# print(dic)
user="ppyyttooponnnnnn"
i=0
dic={}
while i<len(user):
    if user[i] not  in dic:
        store=user.count(user[i])
        dic.update({user[i]:store})
    i+=1
print(dic)