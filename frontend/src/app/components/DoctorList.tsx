import { useState, useEffect } from 'react';
import { doctorAPI } from '../services/api';
import { Trash2, Edit, Search } from 'lucide-react';
import { toast } from 'sonner';

interface Doctor {
  id: string;
  name: string;
  age: number;
  gender: string;
  speciality: string;
}

interface DoctorListProps {
  onEdit: (doctor: Doctor) => void;
}

export function DoctorList({ onEdit }: DoctorListProps) {
  const [doctors, setDoctors] = useState<Doctor[]>([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');

  const fetchDoctors = async () => {
    try {
      setLoading(true);
      const response = await doctorAPI.getAll();
      setDoctors(response.data);
      toast.success('Doctors loaded successfully');
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Failed to load doctors');
      console.error('Error fetching doctors:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = async () => {
    if (!searchTerm.trim()) {
      fetchDoctors();
      return;
    }
    try {
      setLoading(true);
      const response = await doctorAPI.searchByName(searchTerm);
      setDoctors(response.data);
      toast.success('Search completed');
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Search failed');
      console.error('Error searching doctors:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id: string) => {
    if (!confirm('Are you sure you want to delete this doctor?')) return;

    try {
      await doctorAPI.delete(id);
      toast.success('Doctor deleted successfully');
      fetchDoctors();
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Failed to delete doctor');
      console.error('Error deleting doctor:', error);
    }
  };

  useEffect(() => {
    fetchDoctors();
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
            placeholder="Search by doctor name or ID..."
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
              <th className="px-6 py-3 text-left text-gray-700">Speciality</th>
              <th className="px-6 py-3 text-left text-gray-700">Actions</th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {doctors.length === 0 ? (
              <tr>
                <td colSpan={7} className="px-6 py-8 text-center text-gray-500">
                  No doctors found
                </td>
              </tr>
            ) : (
              doctors.map((doctor) => (
                <tr key={doctor.id} className="hover:bg-gray-50">
                  <td className="px-6 py-4 whitespace-nowrap text-gray-900">{doctor.id}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-gray-900">{doctor.name}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-gray-900">{doctor.age}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-gray-900">{doctor.gender}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-gray-900">{doctor.speciality}</td>
                  <td className="px-6 py-4 whitespace-nowrap space-x-2">
                    <button
                      onClick={() => onEdit(doctor)}
                      className="inline-flex items-center px-3 py-1 bg-green-600 text-white rounded hover:bg-green-700 transition-colors"
                    >
                      <Edit className="h-4 w-4 mr-1" />
                      Edit
                    </button>
                    <button
                      onClick={() => handleDelete(doctor.id)}
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
