users = {"alice", "bob", "carol", "carol"}
print(users)

users.add("dave")
users.add("alice")  # duplicate value
print(users)

users.remove("bob")
print(users)

print("Number of users:", len(users))

if "alice" in users:
    print("Alice exists in the set")
