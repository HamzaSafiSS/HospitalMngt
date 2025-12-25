import { useState, useEffect } from 'react';
import { appointmentAPI } from '../services/api';
import { Trash2, Edit, Calendar } from 'lucide-react';
import { toast } from 'sonner';

interface Appointment {
  id: number;
  patient_id: string;
  doctor_id: string;
  date: string;
  time: string;
  status: string;
}

interface AppointmentListProps {
  onEdit: (appointment: Appointment) => void;
}

export function AppointmentList({ onEdit }: AppointmentListProps) {
  const [appointments, setAppointments] = useState<Appointment[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchAppointments = async () => {
    try {
      setLoading(true);
      const response = await appointmentAPI.getAll();
      setAppointments(response.data);
      toast.success('Appointments loaded successfully');
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Failed to load appointments');
      console.error('Error fetching appointments:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleCancel = async (id: number) => {
    if (!confirm('Are you sure you want to cancel this appointment?')) return;

    try {
      await appointmentAPI.cancel(id);
      toast.success('Appointment cancelled successfully');
      fetchAppointments();
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Failed to cancel appointment');
      console.error('Error cancelling appointment:', error);
    }
  };

  useEffect(() => {
    fetchAppointments();
  }, []);

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  const getStatusColor = (status: string) => {
    switch (status.toLowerCase()) {
      case 'scheduled':
        return 'bg-blue-100 text-blue-800';
      case 'completed':
        return 'bg-green-100 text-green-800';
      case 'cancelled':
        return 'bg-red-100 text-red-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <div className="space-y-4">
      <div className="flex items-center gap-2 mb-4">
        <Calendar className="h-6 w-6 text-blue-600" />
        <h3 className="text-xl text-gray-800">All Appointments</h3>
      </div>

      <div className="overflow-x-auto bg-white rounded-lg shadow">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-gray-700">ID</th>
              <th className="px-6 py-3 text-left text-gray-700">Patient ID</th>
              <th className="px-6 py-3 text-left text-gray-700">Doctor ID</th>
              <th className="px-6 py-3 text-left text-gray-700">Date</th>
              <th className="px-6 py-3 text-left text-gray-700">Time</th>
              <th className="px-6 py-3 text-left text-gray-700">Status</th>
              <th className="px-6 py-3 text-left text-gray-700">Actions</th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {appointments.length === 0 ? (
              <tr>
                <td colSpan={8} className="px-6 py-8 text-center text-gray-500">
                  No appointments found
                </td>
              </tr>
            ) : (
              appointments.map((appointment) => (
                <tr key={appointment.id} className="hover:bg-gray-50">
                  <td className="px-6 py-4 whitespace-nowrap text-gray-900">{appointment.id}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-gray-900">{appointment.patient_id}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-gray-900">{appointment.doctor_id}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-gray-900">{appointment.date}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-gray-900">{appointment.time}</td>
                  <td className="px-6 py-4 whitespace-nowrap">
                    <span className={`px-3 py-1 rounded-full text-sm ${getStatusColor(appointment.status)}`}>
                      {appointment.status}
                    </span>
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap space-x-2">
                    <button
                      onClick={() => onEdit(appointment)}
                      className="inline-flex items-center px-3 py-1 bg-green-600 text-white rounded hover:bg-green-700 transition-colors"
                    >
                      <Edit className="h-4 w-4 mr-1" />
                      Edit
                    </button>
                    <button
                      onClick={() => handleCancel(appointment.id)}
                      className="inline-flex items-center px-3 py-1 bg-red-600 text-white rounded hover:bg-red-700 transition-colors"
                    >
                      <Trash2 className="h-4 w-4 mr-1" />
                      Cancel
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
