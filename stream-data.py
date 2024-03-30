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
    start_time = time.time()
    with open(filename, 'a') as file:  # Open the file in append mode
        while True:
            current_time = time.time()
            # Check if the duration is up
            if current_time - start_time >= duration:
                break
            record = generate_patient_record(patient_id)
            file.write(json.dumps(record) + '\n')  # Write the JSON string plus a newline character
            file.flush()  # Ensure each record is written to disk immediately
            print(f"Record {patient_id} written.")  # Optional: print a message to the console
            time.sleep(1)  # Pause for a second
            patient_id += 1

# The following line will start the function and generate records for 1 minute.
# It is commented out to prevent automatic execution in this environment.
# stream_patient_records()
