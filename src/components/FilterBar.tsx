import React from 'react';
import { TaskFilter } from '../types';
import { Search, Plus, Filter } from 'lucide-react';

interface FilterBarProps {
  filter: TaskFilter;
  onFilterChange: (filter: TaskFilter) => void;
  onAddTask: () => void;
}

export function FilterBar({ filter, onFilterChange, onAddTask }: FilterBarProps) {
  const statusOptions = [
    { value: '', label: 'All Tasks' },
    { value: 'pending', label: 'Pending' },
    { value: 'in_progress', label: 'In Progress' },
    { value: 'completed', label: 'Completed' },
    { value: 'cancelled', label: 'Cancelled' },
  ];

  return (
    <div className="card">
      <div className="flex flex-col sm:flex-row gap-4 items-start sm:items-center justify-between">
        <div className="flex flex-col sm:flex-row gap-4 flex-1">
          <div className="relative flex-1 max-w-md">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400" />
            <input
              type="text"
              placeholder="Search tasks..."
              value={filter.search || ''}
              onChange={(e) => onFilterChange({ ...filter, search: e.target.value })}
              className="input pl-10"
            />
          </div>

          <div className="relative">
            <Filter className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400" />
            <select
              value={filter.status || ''}
              onChange={(e) => onFilterChange({ 
                ...filter, 
                status: e.target.value as any || undefined 
              })}
              className="input pl-10 pr-8 appearance-none bg-white"
            >
              {statusOptions.map(option => (
                <option key={option.value} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>
          </div>
        </div>

        <button
          onClick={onAddTask}
          className="btn-primary whitespace-nowrap"
        >
          <Plus className="w-4 h-4 mr-2" />
          Add Task
        </button>
      </div>
    </div>
  );
}