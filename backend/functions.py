import psycopg2
from fastapi import HTTPException
from backend.db import get_connection
from backend.schemas import AppointmentUpdate, CancelAppointmentRequest

# ----------------- Patients -----------------
def ListPatient():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM patientsdata")
        rows = cursor.fetchall()
        return [
            {
                "PatientID": row[0],
                "PatientName": row[1],
                "PatientAge": row[2],
                "PatientGender": row[3],
                "PatientCase": row[4],
                "PatientPhone": row[5],
                "PatientAddress": row[6]
            } for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


def AddPatient(Id, name, age, gender, case, phone, address):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO patientsdata (
                patient_id, patient_name, patient_age, patient_gender, patient_case, patient_phone, patient_address
            ) VALUES (%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(query, (Id, name, age, gender, case, phone, address))
        conn.commit()
        return {"Message": "Patient Added Successfully"}
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        raise HTTPException(status_code=400, detail="Patient with this ID already exists.")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


def ViewById(patient_ID):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM patientsdata WHERE patient_id=%s", (patient_ID,))
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Patient not exist")
        return {
            "PatientID": row[0],
            "PatientName": row[1],
            "PatientAge": row[2],
            "PatientGender": row[3],
            "PatientCase": row[4],
            "PatientPhone": row[5],
            "PatientAddress": row[6]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


def SearchByName(patientName):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM patientsdata WHERE patient_name = %s", (patientName,))
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Patient not exist")
        return {
            "PatientID": row[0],
            "PatientName": row[1],
            "PatientAge": row[2],
            "PatientGender": row[3],
            "PatientCase": row[4],
            "PatientPhone": row[5],
            "PatientAddress": row[6]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


def UpdatePatient(PatientName, PatientAge, PatientGender, PatientCase, PatientPhone, PatientAddress, patientID):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM patientsdata WHERE patient_id=%s", (patientID,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Patient with this ID does not exist")
        query = """
            UPDATE patientsdata
            SET patient_name=%s, patient_age=%s, patient_gender=%s,
                patient_case=%s, patient_phone=%s, patient_address=%s
            WHERE patient_id = %s
        """
        cursor.execute(query, (PatientName, PatientAge, PatientGender, PatientCase, PatientPhone, PatientAddress, patientID))
        conn.commit()
        return {"Message": "Patient Information Successfully Updated"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


def DeletePatient(patientid: str):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM patientsdata WHERE patient_id=%s", (patientid,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Patient with entered ID not exist")
        cursor.execute("DELETE FROM patientsdata WHERE patient_id=%s", (patientid,))
        conn.commit()
        return {"Message": "Patient Successfully Deleted"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


# ----------------- Doctors -----------------
def ListDoctors():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM doctorsdata")
        rows = cursor.fetchall()
        return [
            {
                "DoctorID": row[0],
                "DoctorName": row[1],
                "DoctorAge": row[2],
                "DoctorGender": row[3],
                "DoctorSpeciality": row[4]
            } for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


def AddDoctor(doctorId, doctorName, doctorAge, doctorGender, doctorSpeciality):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO doctorsdata(doctor_id, doctor_name, doctor_age, doctor_gender, doctor_speciality) VALUES (%s,%s,%s,%s,%s)",
            (doctorId, doctorName, doctorAge, doctorGender, doctorSpeciality)
        )
        conn.commit()
        return {"Message": "Doctor Successfully Added."}
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        raise HTTPException(status_code=400, detail="Doctor with this ID already exists.")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


def ViewDoctorById(doctorid):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM doctorsdata WHERE doctor_id=%s", (doctorid,))
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Doctor with the provided ID not exist")
        return {
            "DoctorID": row[0],
            "DoctorName": row[1],
            "DoctorAge": row[2],
            "DoctorGender": row[3],
            "DoctorSpeciality": row[4]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


def UpdateDoctor(newDoctorName, newDoctorAge, newDoctorGender, newDoctorSpeciality, doctorID):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM doctorsdata WHERE doctor_id=%s", (doctorID,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Doctor with this ID not exist")
        cursor.execute(
            "UPDATE doctorsdata SET doctor_name=%s, doctor_age=%s, doctor_gender=%s, doctor_speciality=%s WHERE doctor_id=%s",
            (newDoctorName, newDoctorAge, newDoctorGender, newDoctorSpeciality, doctorID)
        )
        conn.commit()
        return {"Message": "Doctor Information Successfully Updated."}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


def DeleteDoctor(doctorid):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM doctorsdata WHERE doctor_id=%s", (doctorid,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Doctor with entered ID not exist")
        cursor.execute("DELETE FROM doctorsdata WHERE doctor_id=%s", (doctorid,))
        conn.commit()
        return {"Message": "Doctor Successfully Deleted."}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


# ----------------- Appointments -----------------
def ListAppointments():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM appointmentmngt")
        rows = cursor.fetchall()
        return [
            {
                "AppointmentID": row[0],
                "PatientID": row[1],
                "DoctorID": row[2],
                "Appointment_Date": row[3],
                "Appointment_Time": row[4],
                "Status": row[5]
            } for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


def BookAppointment(patientid, doctorid, date, time, status):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM patientsdata WHERE patient_id=%s", (patientid,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Patient with entered ID not exist")
        cursor.execute("SELECT * FROM doctorsdata WHERE doctor_id=%s", (doctorid,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Doctor with entered ID not exist")

        try:
            cursor.execute(
                "INSERT INTO appointmentmngt(patient_id, doctor_id, appointment_date, appointment_time, appointment_status) VALUES(%s,%s,%s,%s,%s)",
                (patientid, doctorid, date, time, status)
            )
        except psycopg2.errors.UniqueViolation:
            conn.rollback()
            raise HTTPException(status_code=400, detail="This doctor already has an appointment at this date and time.")
        conn.commit()
        return {"Message": "Appointment Successfully Booked."}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


def ViewAppointmentsByPatientID(patientid):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM appointmentmngt WHERE patient_id=%s", (patientid,))
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="Appointment with entered Patient ID not exist.")
        return [
            {
                "ID": row[0],
                "PatientID": row[1],
                "DoctorID": row[2],
                "Date": row[3],
                "Time": row[4],
                "Status": row[5]
            } for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


def ViewAppointmentsByDoctorID(doctorid):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM appointmentmngt WHERE doctor_id=%s", (doctorid,))
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="Appointment with entered Doctor ID not exist.")
        return [
            {
                "ID": row[0],
                "PatientID": row[1],
                "DoctorID": row[2],
                "Date": row[3],
                "Time": row[4],
                "Status": row[5]
            } for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


def UpdateAppointment(patientid, number, data: AppointmentUpdate):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT appointment_id FROM appointmentmngt WHERE patient_id=%s", (patientid,))
        appointments = cursor.fetchall()
        if not appointments:
            raise HTTPException(status_code=404, detail="Patient with entered ID does not exist or has no Appointment.")
        if number < 1 or number > len(appointments):
            raise HTTPException(status_code=400, detail="Invalid appointment number.")

        selectedAppID = appointments[number - 1][0]

        # Check for duplicate appointment for the same doctor
        cursor.execute(
            """
            SELECT appointment_id FROM appointmentmngt
            WHERE doctor_id = (SELECT doctor_id FROM appointmentmngt WHERE appointment_id=%s)
            AND appointment_date = %s
            AND appointment_time = %s
            AND appointment_id != %s
            """,
            (selectedAppID, data.appointment_date, data.appointment_time, selectedAppID)
        )
        duplicate = cursor.fetchone()
        if duplicate:
            raise HTTPException(status_code=400, detail="This doctor already has an appointment at this date and time.")

        cursor.execute(
            """
            UPDATE appointmentmngt
            SET appointment_date=%s, appointment_time=%s, appointment_status=%s
            WHERE appointment_id=%s
            """,
            (data.appointment_date, data.appointment_time, data.appointment_status, selectedAppID)
        )
        conn.commit()
        return {"Message": "Appointment Successfully Updated."}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


def CancelAppointment(request: CancelAppointmentRequest):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM appointmentmngt WHERE patient_id=%s", (request.patientID,))
        patient_appointments = cursor.fetchall()
        if not patient_appointments:
            raise HTTPException(status_code=404, detail=f"Patient ID {request.patientID} does not exist or has no appointments.")
        if request.appointmentNumber < 1 or request.appointmentNumber > len(patient_appointments):
            raise HTTPException(status_code=400, detail="Invalid appointment number.")

        selectedAppID = patient_appointments[request.appointmentNumber - 1][0]
        cursor.execute("DELETE FROM appointmentmngt WHERE appointment_id=%s", (selectedAppID,))
        conn.commit()
        return {"Message": "Appointment Successfully Deleted."}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()
