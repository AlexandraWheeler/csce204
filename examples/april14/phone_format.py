# original phone format (770)-776-8538
# new phone format 770.776.8538

def updatePhone(phone):
    answer = ""
    for num in phone:
        if num == "(" or num == ")":
            continue
        elif num == "-":
            answer += "."
        else:
            answer += num
    return answer


phone = updatePhone("(770)-776-8538")
print(phone)