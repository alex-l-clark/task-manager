import React, { useState } from 'react';
import { Task } from '../types';
import { 
  CheckCircle, 
  Clock, 
  AlertCircle, 
  XCircle, 
  Edit2, 
  Trash2, 
  Save, 
  X,
  MoreHorizontal
} from 'lucide-react';
import clsx from 'clsx';

interface TaskItemProps {
  task: Task;
  onUpdate: (taskId: string, updates: Partial<Task>) => Promise<boolean>;
  onDelete: (taskId: string) => Promise<boolean>;
}

export function TaskItem({ task, onUpdate, onDelete }: TaskItemProps) {
  const [isEditing, setIsEditing] = useState(false);
  const [editTitle, setEditTitle] = useState(task.title);
  const [loading, setLoading] = useState(false);
  const [showActions, setShowActions] = useState(false);

  const statusConfig = {
    pending: { icon: Clock, color: 'warning', label: 'Pending' },
    completed: { icon: CheckCircle, color: 'success', label: 'Completed' },
    in_progress: { icon: AlertCircle, color: 'primary', label: 'In Progress' },
    cancelled: { icon: XCircle, color: 'error', label: 'Cancelled' },
  };

  const config = statusConfig[task.status];
  const StatusIcon = config.icon;

  const handleStatusChange = async (newStatus: Task['status']) => {
    setLoading(true);
    await onUpdate(task.id, { status: newStatus });
    setLoading(false);
  };

  const handleSaveEdit = async () => {
    if (editTitle.trim() === task.title) {
      setIsEditing(false);
      return;
    }

    setLoading(true);
    const success = await onUpdate(task.id, { title: editTitle.trim() });
    if (success) {
      setIsEditing(false);
    } else {
      setEditTitle(task.title);
    }
    setLoading(false);
  };

  const handleCancelEdit = () => {
    setEditTitle(task.title);
    setIsEditing(false);
  };

  const handleDelete = async () => {
    if (window.confirm('Are you sure you want to delete this task?')) {
      setLoading(true);
      await onDelete(task.id);
      setLoading(false);
    }
  };

  return (
    <div className={clsx(
      'task-item',
      loading && 'opacity-50 pointer-events-none'
    )}>
      <div className="flex items-start gap-4">
        <div className="flex-shrink-0 mt-1">
          <StatusIcon className={clsx(
            'w-5 h-5',
            config.color === 'success' && 'text-success-600',
            config.color === 'warning' && 'text-warning-600',
            config.color === 'primary' && 'text-primary-600',
            config.color === 'error' && 'text-error-600'
          )} />
        </div>

        <div className="flex-1 min-w-0">
          {isEditing ? (
            <div className="flex gap-2 mb-2">
              <input
                type="text"
                value={editTitle}
                onChange={(e) => setEditTitle(e.target.value)}
                className="input flex-1"
                onKeyDown={(e) => {
                  if (e.key === 'Enter') handleSaveEdit();
                  if (e.key === 'Escape') handleCancelEdit();
                }}
                autoFocus
              />
              <button
                onClick={handleSaveEdit}
                className="btn-success"
                disabled={!editTitle.trim()}
              >
                <Save className="w-4 h-4" />
              </button>
              <button
                onClick={handleCancelEdit}
                className="btn-secondary"
              >
                <X className="w-4 h-4" />
              </button>
            </div>
          ) : (
            <h3 className={clsx(
              'text-lg font-medium mb-2',
              task.status === 'completed' && 'line-through text-gray-500'
            )}>
              {task.title}
            </h3>
          )}

          <div className="flex items-center gap-4 text-sm text-gray-500">
            <span className={clsx(
              'status-badge',
              `status-${task.status.replace('_', '-')}`
            )}>
              {config.label}
            </span>
            
            {task.createdAt && (
              <span>
                Created {new Date(task.createdAt).toLocaleDateString()}
              </span>
            )}
          </div>
        </div>

        <div className="flex-shrink-0 relative">
          <button
            onClick={() => setShowActions(!showActions)}
            className="p-2 text-gray-400 hover:text-gray-600 rounded-lg hover:bg-gray-100"
          >
            <MoreHorizontal className="w-4 h-4" />
          </button>

          {showActions && (
            <div className="absolute right-0 top-full mt-1 bg-white rounded-lg shadow-lg border border-gray-200 py-1 z-10 min-w-48">
              <div className="px-3 py-2 text-xs font-medium text-gray-500 border-b border-gray-100">
                Change Status
              </div>
              
              {Object.entries(statusConfig).map(([status, config]) => (
                <button
                  key={status}
                  onClick={() => {
                    handleStatusChange(status as Task['status']);
                    setShowActions(false);
                  }}
                  className={clsx(
                    'w-full px-3 py-2 text-left text-sm hover:bg-gray-50 flex items-center gap-2',
                    task.status === status && 'bg-gray-50 font-medium'
                  )}
                >
                  <config.icon className="w-4 h-4" />
                  {config.label}
                </button>
              ))}

              <div className="border-t border-gray-100 mt-1 pt-1">
                <button
                  onClick={() => {
                    setIsEditing(true);
                    setShowActions(false);
                  }}
                  className="w-full px-3 py-2 text-left text-sm hover:bg-gray-50 flex items-center gap-2"
                >
                  <Edit2 className="w-4 h-4" />
                  Edit Task
                </button>
                
                <button
                  onClick={() => {
                    handleDelete();
                    setShowActions(false);
                  }}
                  className="w-full px-3 py-2 text-left text-sm hover:bg-gray-50 text-error-600 flex items-center gap-2"
                >
                  <Trash2 className="w-4 h-4" />
                  Delete Task
                </button>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Click outside to close actions menu */}
      {showActions && (
        <div 
          className="fixed inset-0 z-0" 
          onClick={() => setShowActions(false)}
        />
      )}
    </div>
  );
}