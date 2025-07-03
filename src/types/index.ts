export interface User {
  username: string;
}

export interface Task {
  id: string;
  username: string;
  title: string;
  status: 'pending' | 'completed' | 'in_progress' | 'cancelled';
  createdAt?: Date;
  updatedAt?: Date;
}

export interface AuthResult {
  success: boolean;
  message: string;
  user?: User;
}

export interface TaskFilter {
  status?: Task['status'];
  search?: string;
}