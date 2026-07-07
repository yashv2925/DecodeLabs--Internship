# ============================
# TO-DO LIST PROJECT
# DecodeLabs - Project 1
# ============================

tasks = []

while True:
    print("\n==============================")
    print("      TO-DO LIST MENU")
    print("==============================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        task = input("Enter your task: ")

        if task.strip() == "":
            print("❌ Task cannot be empty!")
        else:
            tasks.append(task)
            print("✅ Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("\n📌 No tasks available.")
        else:
            print("\n📋 Your Tasks:")
            count = 1
            for task in tasks:
                print(f"{count}. {task}")
                count += 1

    elif choice == "3":
        print("\n🙏 Thank you for using the To-Do List!")
        break

    else:
        print("❌ Invalid choice! Please enter 1, 2, or 3.")