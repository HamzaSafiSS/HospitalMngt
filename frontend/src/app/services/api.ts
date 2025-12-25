import axios from 'axios';

// Configure base URL for your FastAPI backend
const API_BASE_URL = 'http://127.0.0.1:8000';

// Create axios instance with default config
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Patient API calls
export const patientAPI = {
  getAll: () => apiClient.get('/patients'),
  getById: (id: string) => apiClient.get(`/patients/${id}`),
  searchByName: (name: string) => apiClient.get(`/patients/search?name=${name}`),
  create: (patient: any) => apiClient.post('/patients', patient),
  update: (patient: any) => apiClient.put('/patients', patient),
  delete: (id: string) => apiClient.delete(`/patients/${id}`),
};

// Doctor API calls
export const doctorAPI = {
  getAll: () => apiClient.get('/doctors'),
  getById: (id: string) => apiClient.get(`/doctors/${id}`),
  searchByName: (name: string) => apiClient.get(`/doctors/search?name=${name}`),
  create: (doctor: any) => apiClient.post('/doctors', doctor),
  update: (doctor: any) => apiClient.put('/doctors', doctor),
  delete: (id: string) => apiClient.delete(`/doctors/${id}`),
};

// Appointment API calls
export const appointmentAPI = {
  getAll: () => apiClient.get('/appointments'),
  getById: (id: number) => apiClient.get(`/appointments/${id}`),
  getByPatient: (patientId: string) => apiClient.get(`/appointments/patient/${patientId}`),
  getByDoctor: (doctorId: string) => apiClient.get(`/appointments/doctor/${doctorId}`),
  create: (appointment: any) => apiClient.post('/appointments', appointment),
  update: (id: number, appointment: any) => apiClient.put(`/appointments/${id}`, appointment),
  cancel: (id: number) => apiClient.delete(`/appointments/${id}`),
};

export default apiClient;
