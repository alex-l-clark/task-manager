import React, { useState, useEffect } from 'react';
import { AuthScreen } from './components/AuthScreen';
import { TaskDashboard } from './components/TaskDashboard';
import { TaskManager } from './services/TaskManager';
import { UserManager } from './services/UserManager';
import { User, Task } from './types';

function App() {
  const [currentUser, setCurrentUser] = useState<User | null>(null);
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);

  const taskManager = new TaskManager();
  const userManager = new UserManager();

  useEffect(() => {
    // Check for existing session
    const savedUser = localStorage.getItem('currentUser');
    if (savedUser) {
      const user = JSON.parse(savedUser);
      setCurrentUser(user);
      loadUserTasks(user.username);
    }
    setLoading(false);
  }, []);

  const loadUserTasks = async (username: string) => {
    try {
      const userTasks = await taskManager.getUserTasks(username);
      setTasks(userTasks);
    } catch (error) {
      console.error('Error loading tasks:', error);
    }
  };

  const handleLogin = async (username: string, password: string) => {
    try {
      const result = await userManager.login(username, password);
      if (result.success && result.user) {
        setCurrentUser(result.user);
        localStorage.setItem('currentUser', JSON.stringify(result.user));
        await loadUserTasks(username);
        return { success: true, message: result.message };
      }
      return { success: false, message: result.message };
    } catch (error) {
      return { success: false, message: 'Login failed. Please try again.' };
    }
  };

  const handleRegister = async (username: string, password: string) => {
    try {
      const result = await userManager.register(username, password);
      if (result.success && result.user) {
        setCurrentUser(result.user);
        localStorage.setItem('currentUser', JSON.stringify(result.user));
        setTasks([]);
        return { success: true, message: result.message };
      }
      return { success: false, message: result.message };
    } catch (error) {
      return { success: false, message: 'Registration failed. Please try again.' };
    }
  };

  const handleLogout = () => {
    setCurrentUser(null);
    setTasks([]);
    localStorage.removeItem('currentUser');
  };

  const handleAddTask = async (title: string) => {
    if (!currentUser) return;
    
    try {
      const newTask = await taskManager.addTask(currentUser.username, title);
      setTasks(prev => [...prev, newTask]);
      return true;
    } catch (error) {
      console.error('Error adding task:', error);
      return false;
    }
  };

  const handleUpdateTask = async (taskId: string, updates: Partial<Task>) => {
    if (!currentUser) return;

    try {
      const updatedTask = await taskManager.updateTask(taskId, currentUser.username, updates);
      if (updatedTask) {
        setTasks(prev => prev.map(task => 
          task.id === taskId ? updatedTask : task
        ));
        return true;
      }
      return false;
    } catch (error) {
      console.error('Error updating task:', error);
      return false;
    }
  };

  const handleDeleteTask = async (taskId: string) => {
    if (!currentUser) return;

    try {
      const success = await taskManager.deleteTask(taskId, currentUser.username);
      if (success) {
        setTasks(prev => prev.filter(task => task.id !== taskId));
        return true;
      }
      return false;
    } catch (error) {
      console.error('Error deleting task:', error);
      return false;
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  if (!currentUser) {
    return (
      <AuthScreen 
        onLogin={handleLogin}
        onRegister={handleRegister}
      />
    );
  }

  return (
    <TaskDashboard
      user={currentUser}
      tasks={tasks}
      onLogout={handleLogout}
      onAddTask={handleAddTask}
      onUpdateTask={handleUpdateTask}
      onDeleteTask={handleDeleteTask}
    />
  );
}

export default App;