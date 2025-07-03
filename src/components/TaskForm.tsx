import React, { useState } from 'react';
import { Plus, X } from 'lucide-react';

interface TaskFormProps {
  onSubmit: (title: string) => Promise<boolean>;
  onCancel: () => void;
}

export function TaskForm({ onSubmit, onCancel }: TaskFormProps) {
  const [title, setTitle] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim()) return;

    setLoading(true);
    const success = await onSubmit(title.trim());
    if (success) {
      setTitle('');
    }
    setLoading(false);
  };

  return (
    <div className="card">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-medium text-gray-900">Add New Task</h3>
        <button
          onClick={onCancel}
          className="p-1 text-gray-400 hover:text-gray-600 rounded"
        >
          <X className="w-4 h-4" />
        </button>
      </div>

      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label htmlFor="task-title" className="block text-sm font-medium text-gray-700 mb-1">
            Task Title
          </label>
          <input
            type="text"
            id="task-title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="input"
            placeholder="Enter task description..."
            required
            autoFocus
          />
        </div>

        <div className="flex gap-2">
          <button
            type="submit"
            disabled={!title.trim() || loading}
            className="btn-primary flex-1"
          >
            {loading ? (
              <div className="flex items-center justify-center">
                <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
                Adding...
              </div>
            ) : (
              <>
                <Plus className="w-4 h-4 mr-2" />
                Add Task
              </>
            )}
          </button>
          
          <button
            type="button"
            onClick={onCancel}
            className="btn-secondary"
          >
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
}