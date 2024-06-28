a=[['John', 85, 90, 88], ['Alice', 78, 85, 92], ['Bob', 92, 88, 90]]
# b=[a.sort(key=lambda m: m[1])]
# print(b)
# for i in a:
#     for j in i[1::]:
#         temp = sum(i[1::])
#         b.append(temp)
#
list1=[]
tem=[]
for i in range(len(a)):
    print(sum(a[i][1::])/len(a[i][1::]))
    tem.append(sum(a[i][1::])/len(a[i][1::]))

    # if tem<sum(a[i][1::])/len(a[i][1::]):
    #     list1.insert(0,a[i])
    # else:
    #     list1.append(a[i])
    # tem=()
    # print((sum(a[i][1::])/len(a[i][1::])))



#print(list1,tem)
def sort_students_by_average(scores):
    def average_score(student):
        # Calculate the average score excluding the first element (student name)
        scores = student[1:]
        return sum(scores) / len(scores)

    # Sort the list of students based on the average score in descending order
    sorted_students = sorted(scores, key=average_score, reverse=True)
    return sorted_students

# Example usage:
students = [['John', 85, 90, 88], ['Alice', 78, 85, 92], ['Bob', 92, 88, 90]]

sorted_students = sort_students_by_average(students)
print(sorted_students)
