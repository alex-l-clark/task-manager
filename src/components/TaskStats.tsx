import React from 'react';
import { Task } from '../types';
import { CheckCircle, Clock, AlertCircle, XCircle } from 'lucide-react';

interface TaskStatsProps {
  tasks: Task[];
}

export function TaskStats({ tasks }: TaskStatsProps) {
  const stats = {
    total: tasks.length,
    pending: tasks.filter(t => t.status === 'pending').length,
    completed: tasks.filter(t => t.status === 'completed').length,
    inProgress: tasks.filter(t => t.status === 'in_progress').length,
    cancelled: tasks.filter(t => t.status === 'cancelled').length,
  };

  const completionRate = stats.total > 0 ? Math.round((stats.completed / stats.total) * 100) : 0;

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      <div className="card">
        <div className="flex items-center">
          <div className="p-2 bg-primary-100 rounded-lg">
            <CheckCircle className="w-6 h-6 text-primary-600" />
          </div>
          <div className="ml-4">
            <p className="text-sm font-medium text-gray-600">Total Tasks</p>
            <p className="text-2xl font-bold text-gray-900">{stats.total}</p>
          </div>
        </div>
      </div>

      <div className="card">
        <div className="flex items-center">
          <div className="p-2 bg-success-100 rounded-lg">
            <CheckCircle className="w-6 h-6 text-success-600" />
          </div>
          <div className="ml-4">
            <p className="text-sm font-medium text-gray-600">Completed</p>
            <p className="text-2xl font-bold text-gray-900">{stats.completed}</p>
          </div>
        </div>
      </div>

      <div className="card">
        <div className="flex items-center">
          <div className="p-2 bg-warning-100 rounded-lg">
            <Clock className="w-6 h-6 text-warning-600" />
          </div>
          <div className="ml-4">
            <p className="text-sm font-medium text-gray-600">Pending</p>
            <p className="text-2xl font-bold text-gray-900">{stats.pending}</p>
          </div>
        </div>
      </div>

      <div className="card">
        <div className="flex items-center">
          <div className="p-2 bg-primary-100 rounded-lg">
            <AlertCircle className="w-6 h-6 text-primary-600" />
          </div>
          <div className="ml-4">
            <p className="text-sm font-medium text-gray-600">Completion Rate</p>
            <p className="text-2xl font-bold text-gray-900">{completionRate}%</p>
          </div>
        </div>
      </div>
    </div>
  );
}