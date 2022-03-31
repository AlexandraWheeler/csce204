friends = ["Chloe","Andrew","Morgan","Bailey","Jaci"]
with open("examples/march29/friends.txt", "w") as file:
    for friend in friends:
        file.write(f"{friend}\n")