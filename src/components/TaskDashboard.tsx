import React, { useState, useMemo } from 'react';
import { User, Task, TaskFilter } from '../types';
import { TaskList } from './TaskList';
import { TaskForm } from './TaskForm';
import { TaskStats } from './TaskStats';
import { Header } from './Header';
import { FilterBar } from './FilterBar';

interface TaskDashboardProps {
  user: User;
  tasks: Task[];
  onLogout: () => void;
  onAddTask: (title: string) => Promise<boolean>;
  onUpdateTask: (taskId: string, updates: Partial<Task>) => Promise<boolean>;
  onDeleteTask: (taskId: string) => Promise<boolean>;
}

export function TaskDashboard({
  user,
  tasks,
  onLogout,
  onAddTask,
  onUpdateTask,
  onDeleteTask,
}: TaskDashboardProps) {
  const [showTaskForm, setShowTaskForm] = useState(false);
  const [filter, setFilter] = useState<TaskFilter>({});

  const filteredTasks = useMemo(() => {
    return tasks.filter(task => {
      if (filter.status && task.status !== filter.status) {
        return false;
      }
      if (filter.search && !task.title.toLowerCase().includes(filter.search.toLowerCase())) {
        return false;
      }
      return true;
    });
  }, [tasks, filter]);

  const handleAddTask = async (title: string) => {
    const success = await onAddTask(title);
    if (success) {
      setShowTaskForm(false);
    }
    return success;
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <Header user={user} onLogout={onLogout} />
      
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            Welcome back, {user.username}!
          </h1>
          <p className="text-gray-600">
            Manage your tasks and stay productive
          </p>
        </div>

        <TaskStats tasks={tasks} />

        <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
          <div className="lg:col-span-3">
            <div className="mb-6">
              <FilterBar
                filter={filter}
                onFilterChange={setFilter}
                onAddTask={() => setShowTaskForm(true)}
              />
            </div>

            <TaskList
              tasks={filteredTasks}
              onUpdateTask={onUpdateTask}
              onDeleteTask={onDeleteTask}
            />
          </div>

          <div className="lg:col-span-1">
            {showTaskForm && (
              <div className="mb-6">
                <TaskForm
                  onSubmit={handleAddTask}
                  onCancel={() => setShowTaskForm(false)}
                />
              </div>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}