import { User, AuthResult } from '../types';

export class UserManager {
  private users: Map<string, string> = new Map();

  constructor() {
    this.loadUsers();
  }

  private loadUsers() {
    const usersData = localStorage.getItem('users');
    if (usersData) {
      const users = JSON.parse(usersData);
      this.users = new Map(Object.entries(users));
    }
  }

  private saveUsers() {
    const usersObj = Object.fromEntries(this.users);
    localStorage.setItem('users', JSON.stringify(usersObj));
  }

  private hashPassword(password: string): string {
    // Simple hash function for demo purposes
    // In production, use a proper hashing library like bcrypt
    let hash = 0;
    for (let i = 0; i < password.length; i++) {
      const char = password.charCodeAt(i);
      hash = ((hash << 5) - hash) + char;
      hash = hash & hash; // Convert to 32-bit integer
    }
    return hash.toString();
  }

  async login(username: string, password: string): Promise<AuthResult> {
    if (!username.trim() || !password.trim()) {
      return { success: false, message: 'Username and password are required' };
    }

    const hashedPassword = this.hashPassword(password);
    const storedPassword = this.users.get(username);

    if (!storedPassword) {
      return { success: false, message: 'Invalid username' };
    }

    if (storedPassword !== hashedPassword) {
      return { success: false, message: 'Invalid password' };
    }

    return {
      success: true,
      message: 'Login successful',
      user: { username }
    };
  }

  async register(username: string, password: string): Promise<AuthResult> {
    if (!username.trim() || !password.trim()) {
      return { success: false, message: 'Username and password are required' };
    }

    if (username.length < 3) {
      return { success: false, message: 'Username must be at least 3 characters long' };
    }

    if (password.length < 6) {
      return { success: false, message: 'Password must be at least 6 characters long' };
    }

    if (this.users.has(username)) {
      return { success: false, message: 'Username already exists' };
    }

    const hashedPassword = this.hashPassword(password);
    this.users.set(username, hashedPassword);
    this.saveUsers();

    return {
      success: true,
      message: 'Registration successful',
      user: { username }
    };
  }
}