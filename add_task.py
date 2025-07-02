import uuid

def generate_task_id():
    return str(uuid.uuid4())

def save_task(task_id, task_title, task_status):
    try:
        with open("tasks.txt", "a") as file:
            file.write(f"{task_id}|{task_title}|{task_status}\n")
            print("Task added successfully!")
            return True
    except Exception as e:
        print(f"Error saving task: {e}")    
        return False


def add_task():
    task_title = input("Enter a task: ")
    task_id = generate_task_id()
    task_status = "pending"
    if save_task(task_id, task_title, task_status):
        return True
    else:
        print("Failed to add task.")
        return False

add_task()