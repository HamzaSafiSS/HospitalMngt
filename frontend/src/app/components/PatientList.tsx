import { useState, useEffect } from 'react';
import { patientAPI } from '../services/api';
import { Trash2, Edit, Search } from 'lucide-react';
import { toast } from 'sonner';

interface Patient {
  id: number;
  name: string;
  age: number;
  gender: string;
  phone: string;
  email?: string;
  address?: string;
}

interface PatientListProps {
  onEdit: (patient: Patient) => void;
}

export function PatientList({ onEdit }: PatientListProps) {
  const [patients, setPatients] = useState<Patient[]>([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');

  const fetchPatients = async () => {
    try {
      setLoading(true);
      const response = await patientAPI.getAll();
      setPatients(response.data);
      toast.success('Patients loaded successfully');
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Failed to load patients');
      console.error('Error fetching patients:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = async () => {
    if (!searchTerm.trim()) {
      fetchPatients();
      return;
    }
    try {
      setLoading(true);
      const response = await patientAPI.searchByName(searchTerm);
      setPatients(response.data);
      toast.success('Search completed');
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Search failed');
      console.error('Error searching patients:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id: number) => {
    if (!confirm('Are you sure you want to delete this patient?')) return;
    
    try {
      await patientAPI.delete(id);
      toast.success('Patient deleted successfully');
      fetchPatients();
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Failed to delete patient');
      console.error('Error deleting patient:', error);
    }
  };

  useEffect(() => {
    fetchPatients();
  }, []);

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      <div className="flex gap-2">
        <div className="flex-1 relative">
          <input
            type="text"
            placeholder="Search by patient name or ID..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSearch()}
            className="w-full px-4 py-2 pl-10 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <Search className="absolute left-3 top-2.5 h-5 w-5 text-gray-400" />
        </div>
        <button
          onClick={handleSearch}
          className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
        >
          Search
        </button>
      </div>

      <div className="overflow-x-auto bg-white rounded-lg shadow">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-gray-700">ID</th>
              <th className="px-6 py-3 text-left text-gray-700">Name</th>
              <th className="px-6 py-3 text-left text-gray-700">Age</th>
              <th className="px-6 py-3 text-left text-gray-700">Gender</th>
              <th className="px-6 py-3 text-left text-gray-700">Phone</th>
              <th className="px-6 py-3 text-left text-gray-700">Email</th>
              <th className="px-6 py-3 text-left text-gray-700">Actions</th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {patients.length === 0 ? (
              <tr>
                <td colSpan={7} className="px-6 py-8 text-center text-gray-500">
                  No patients found
                </td>
              </tr>
            ) : (
              patients.map((patient) => (
                <tr key={patient.id} className="hover:bg-gray-50">
                  <td className="px-6 py-4 whitespace-nowrap text-gray-900">{patient.id}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-gray-900">{patient.name}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-gray-900">{patient.age}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-gray-900">{patient.gender}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-gray-900">{patient.phone}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-gray-900">{patient.email || '-'}</td>
                  <td className="px-6 py-4 whitespace-nowrap space-x-2">
                    <button
                      onClick={() => onEdit(patient)}
                      className="inline-flex items-center px-3 py-1 bg-green-600 text-white rounded hover:bg-green-700 transition-colors"
                    >
                      <Edit className="h-4 w-4 mr-1" />
                      Edit
                    </button>
                    <button
                      onClick={() => handleDelete(patient.id)}
                      className="inline-flex items-center px-3 py-1 bg-red-600 text-white rounded hover:bg-red-700 transition-colors"
                    >
                      <Trash2 className="h-4 w-4 mr-1" />
                      Delete
                    </button>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
