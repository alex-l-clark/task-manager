import { Task } from '../types';

export class TaskManager {
  private tasks: Task[] = [];

  constructor() {
    this.loadTasks();
  }

  private loadTasks() {
    const tasksData = localStorage.getItem('tasks');
    if (tasksData) {
      this.tasks = JSON.parse(tasksData).map((task: any) => ({
        ...task,
        createdAt: task.createdAt ? new Date(task.createdAt) : new Date(),
        updatedAt: task.updatedAt ? new Date(task.updatedAt) : new Date(),
      }));
    }
  }

  private saveTasks() {
    localStorage.setItem('tasks', JSON.stringify(this.tasks));
  }

  private generateId(): string {
    return Date.now().toString(36) + Math.random().toString(36).substr(2);
  }

  async getUserTasks(username: string): Promise<Task[]> {
    return this.tasks.filter(task => task.username === username);
  }

  async addTask(username: string, title: string): Promise<Task> {
    const newTask: Task = {
      id: this.generateId(),
      username,
      title: title.trim(),
      status: 'pending',
      createdAt: new Date(),
      updatedAt: new Date(),
    };

    this.tasks.push(newTask);
    this.saveTasks();
    return newTask;
  }

  async updateTask(taskId: string, username: string, updates: Partial<Task>): Promise<Task | null> {
    const taskIndex = this.tasks.findIndex(
      task => task.id === taskId && task.username === username
    );

    if (taskIndex === -1) {
      return null;
    }

    const updatedTask = {
      ...this.tasks[taskIndex],
      ...updates,
      updatedAt: new Date(),
    };

    this.tasks[taskIndex] = updatedTask;
    this.saveTasks();
    return updatedTask;
  }

  async deleteTask(taskId: string, username: string): Promise<boolean> {
    const taskIndex = this.tasks.findIndex(
      task => task.id === taskId && task.username === username
    );

    if (taskIndex === -1) {
      return false;
    }

    this.tasks.splice(taskIndex, 1);
    this.saveTasks();
    return true;
  }

  async getTaskById(taskId: string, username: string): Promise<Task | null> {
    return this.tasks.find(
      task => task.id === taskId && task.username === username
    ) || null;
  }

  async getTasksByStatus(status: Task['status'], username: string): Promise<Task[]> {
    return this.tasks.filter(
      task => task.username === username && task.status === status
    );
  }
}