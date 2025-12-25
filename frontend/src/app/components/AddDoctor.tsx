import { useState } from 'react';
import { doctorAPI } from '../services/api';
import { toast } from 'sonner';

interface AddDoctorProps {
  onSuccess: () => void;
}

export function AddDoctor({ onSuccess }: AddDoctorProps) {
  const [formData, setFormData] = useState({
    id: '',
    name: '',
    age: '',
    gender: '',
    speciality: '',
  });
  const [loading, setLoading] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!formData.id || !formData.name || !formData.age || !formData.gender || !formData.speciality) {
      toast.error('Please fill in all required fields');
      return;
    }

    try {
      setLoading(true);
      await doctorAPI.create({
        ...formData,
        age: parseInt(formData.age),
      });
      toast.success('Doctor added successfully');
      setFormData({ id: '', name: '', age: '', gender: '', speciality: '' });
      onSuccess();
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Failed to add doctor');
      console.error('Error adding doctor:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow">
      <h2 className="text-2xl mb-6 text-gray-800">Add New Doctor</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label className="block mb-2 text-gray-700">Doctor ID *</label>
            <input
              type="text"
              name="id"
              value={formData.id}
              onChange={handleChange}
              required
              placeholder="e.g. D001"
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          <div>
            <label className="block mb-2 text-gray-700">Name *</label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          <div>
            <label className="block mb-2 text-gray-700">Age *</label>
            <input
              type="number"
              name="age"
              value={formData.age}
              onChange={handleChange}
              required
              min="25"
              max="150"
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          <div>
            <label className="block mb-2 text-gray-700">Gender *</label>
            <select
              name="gender"
              value={formData.gender}
              onChange={handleChange}
              required
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="">Select Gender</option>
              <option value="Male">Male</option>
              <option value="Female">Female</option>
              <option value="Other">Other</option>
            </select>
          </div>
          <div>
            <label className="block mb-2 text-gray-700">Speciality *</label>
            <input
              type="text"
              name="speciality"
              value={formData.speciality}
              onChange={handleChange}
              required
              placeholder="e.g., Cardiologist, Pediatrician"
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
        </div>
        <div className="flex justify-end">
          <button
            type="submit"
            disabled={loading}
            className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {loading ? 'Adding...' : 'Add Doctor'}
          </button>
        </div>
      </form>
    </div>
  );
}
