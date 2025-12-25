import { useState } from 'react';
import { Toaster } from 'sonner';
import { Users, Stethoscope, Calendar, Plus } from 'lucide-react';

// Patient Components
import { PatientList } from './components/PatientList';
import { AddPatient } from './components/AddPatient';
import { UpdatePatient } from './components/UpdatePatient';

// Doctor Components
import { DoctorList } from './components/DoctorList';
import { AddDoctor } from './components/AddDoctor';
import { UpdateDoctor } from './components/UpdateDoctor';

// Appointment Components
import { AppointmentList } from './components/AppointmentList';
import { BookAppointment } from './components/BookAppointment';
import { UpdateAppointment } from './components/UpdateAppointment';

type Tab = 'patients' | 'doctors' | 'appointments';
type PatientView = 'list' | 'add';
type DoctorView = 'list' | 'add';
type AppointmentView = 'list' | 'book';

export default function App() {
  const [activeTab, setActiveTab] = useState<Tab>('patients');
  
  // Patient state
  const [patientView, setPatientView] = useState<PatientView>('list');
  const [selectedPatient, setSelectedPatient] = useState<any>(null);
  const [refreshPatients, setRefreshPatients] = useState(0);

  // Doctor state
  const [doctorView, setDoctorView] = useState<DoctorView>('list');
  const [selectedDoctor, setSelectedDoctor] = useState<any>(null);
  const [refreshDoctors, setRefreshDoctors] = useState(0);

  // Appointment state
  const [appointmentView, setAppointmentView] = useState<AppointmentView>('list');
  const [selectedAppointment, setSelectedAppointment] = useState<any>(null);
  const [refreshAppointments, setRefreshAppointments] = useState(0);

  // Patient handlers
  const handlePatientEdit = (patient: any) => {
    setSelectedPatient(patient);
  };

  const handlePatientUpdateClose = () => {
    setSelectedPatient(null);
  };

  const handlePatientUpdateSuccess = () => {
    setRefreshPatients((prev) => prev + 1);
  };

  const handlePatientAddSuccess = () => {
    setRefreshPatients((prev) => prev + 1);
  };

  // Doctor handlers
  const handleDoctorEdit = (doctor: any) => {
    setSelectedDoctor(doctor);
  };

  const handleDoctorUpdateClose = () => {
    setSelectedDoctor(null);
  };

  const handleDoctorUpdateSuccess = () => {
    setRefreshDoctors((prev) => prev + 1);
  };

  const handleDoctorAddSuccess = () => {
    setRefreshDoctors((prev) => prev + 1);
  };

  // Appointment handlers
  const handleAppointmentEdit = (appointment: any) => {
    setSelectedAppointment(appointment);
  };

  const handleAppointmentUpdateClose = () => {
    setSelectedAppointment(null);
  };

  const handleAppointmentUpdateSuccess = () => {
    setRefreshAppointments((prev) => prev + 1);
  };

  const handleAppointmentBookSuccess = () => {
    setRefreshAppointments((prev) => prev + 1);
  };

  const tabs = [
    { id: 'patients' as Tab, label: 'Patients', icon: Users },
    { id: 'doctors' as Tab, label: 'Doctors', icon: Stethoscope },
    { id: 'appointments' as Tab, label: 'Appointments', icon: Calendar },
  ];

  return (
    <div className="min-h-screen bg-gray-100">
      <Toaster position="top-right" richColors />
      
      {/* Header */}
      <header className="bg-white shadow-md">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <h1 className="text-3xl text-blue-600">Hospital Management System</h1>
          <p className="mt-1 text-gray-600">FastAPI Backend Integration</p>
        </div>
      </header>

      {/* Navigation Tabs */}
      <div className="bg-white border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <nav className="flex space-x-8">
            {tabs.map((tab) => {
              const Icon = tab.icon;
              return (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id)}
                  className={`flex items-center gap-2 py-4 px-1 border-b-2 transition-colors ${
                    activeTab === tab.id
                      ? 'border-blue-600 text-blue-600'
                      : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                  }`}
                >
                  <Icon className="h-5 w-5" />
                  <span>{tab.label}</span>
                </button>
              );
            })}
          </nav>
        </div>
      </div>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Patients Tab */}
        {activeTab === 'patients' && (
          <div className="space-y-6">
            <div className="flex justify-between items-center">
              <h2 className="text-2xl text-gray-800">Patients Management</h2>
              <div className="flex gap-2">
                <button
                  onClick={() => setPatientView('list')}
                  className={`px-4 py-2 rounded-lg transition-colors ${
                    patientView === 'list'
                      ? 'bg-blue-600 text-white'
                      : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                  }`}
                >
                  View List
                </button>
                <button
                  onClick={() => setPatientView('add')}
                  className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-colors ${
                    patientView === 'add'
                      ? 'bg-blue-600 text-white'
                      : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                  }`}
                >
                  <Plus className="h-5 w-5" />
                  Add Patient
                </button>
              </div>
            </div>
            {patientView === 'list' ? (
              <PatientList key={refreshPatients} onEdit={handlePatientEdit} />
            ) : (
              <AddPatient onSuccess={handlePatientAddSuccess} />
            )}
            <UpdatePatient
              patient={selectedPatient}
              onClose={handlePatientUpdateClose}
              onSuccess={handlePatientUpdateSuccess}
            />
          </div>
        )}

        {/* Doctors Tab */}
        {activeTab === 'doctors' && (
          <div className="space-y-6">
            <div className="flex justify-between items-center">
              <h2 className="text-2xl text-gray-800">Doctors Management</h2>
              <div className="flex gap-2">
                <button
                  onClick={() => setDoctorView('list')}
                  className={`px-4 py-2 rounded-lg transition-colors ${
                    doctorView === 'list'
                      ? 'bg-blue-600 text-white'
                      : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                  }`}
                >
                  View List
                </button>
                <button
                  onClick={() => setDoctorView('add')}
                  className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-colors ${
                    doctorView === 'add'
                      ? 'bg-blue-600 text-white'
                      : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                  }`}
                >
                  <Plus className="h-5 w-5" />
                  Add Doctor
                </button>
              </div>
            </div>
            {doctorView === 'list' ? (
              <DoctorList key={refreshDoctors} onEdit={handleDoctorEdit} />
            ) : (
              <AddDoctor onSuccess={handleDoctorAddSuccess} />
            )}
            <UpdateDoctor
              doctor={selectedDoctor}
              onClose={handleDoctorUpdateClose}
              onSuccess={handleDoctorUpdateSuccess}
            />
          </div>
        )}

        {/* Appointments Tab */}
        {activeTab === 'appointments' && (
          <div className="space-y-6">
            <div className="flex justify-between items-center">
              <h2 className="text-2xl text-gray-800">Appointments Management</h2>
              <div className="flex gap-2">
                <button
                  onClick={() => setAppointmentView('list')}
                  className={`px-4 py-2 rounded-lg transition-colors ${
                    appointmentView === 'list'
                      ? 'bg-blue-600 text-white'
                      : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                  }`}
                >
                  View List
                </button>
                <button
                  onClick={() => setAppointmentView('book')}
                  className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-colors ${
                    appointmentView === 'book'
                      ? 'bg-blue-600 text-white'
                      : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                  }`}
                >
                  <Plus className="h-5 w-5" />
                  Book Appointment
                </button>
              </div>
            </div>
            {appointmentView === 'list' ? (
              <AppointmentList key={refreshAppointments} onEdit={handleAppointmentEdit} />
            ) : (
              <BookAppointment onSuccess={handleAppointmentBookSuccess} />
            )}
            <UpdateAppointment
              appointment={selectedAppointment}
              onClose={handleAppointmentUpdateClose}
              onSuccess={handleAppointmentUpdateSuccess}
            />
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 mt-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <p className="text-center text-gray-600">
            Hospital Management System - Connected to FastAPI Backend at http://127.0.0.1:8000
          </p>
        </div>
      </footer>
    </div>
  );
}
