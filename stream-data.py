import time
import random
import json
from datetime import datetime

diagnosis = ['Asthma', 'Diabetes', 'Flu', 'Hypertension', 'COVID-19']
statuses = ['New', 'Ongoing', 'Resolved']
medications = ['Medication A', 'Medication B', 'Medication C', 'Medication D']
departments = ['General Medicine', 'Pediatrics', 'Cardiology', 'Infectious Diseases']

def generate_patient_record(patient_id):
    """Generate a single patient record with specified keys."""
    record = {
        'patient_id': patient_id,
        'diagnosis': random.choice(diagnosis),
        'status': random.choice(statuses),
        'medication': random.choice(medications),
        'department': random.choice(departments),
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return record

def stream_patient_records(filename='patient_records.txt', duration=60):
    """Continuously generate and write patient records to a file for a specified duration."""
    patient_id = 1
    end_time = time.time() + duration
    with open(filename, 'a') as file:
        while time.time() < end_time:
            record = generate_patient_record(patient_id)
            file.write(json.dumps(record) + '\n')
            file.flush()
            print(f"Record {patient_id} written.")
            time.sleep(1)
            patient_id += 1

if __name__ == '__main__':
    stream_patient_records()
