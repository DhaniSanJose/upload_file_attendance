# attendance/views.py
from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import AttendanceRecord
from datetime import datetime

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']

            # Read and process each line in the uploaded file
            for line in uploaded_file:
                line = line.decode('utf-8').strip()  # Decode bytes to string and remove leading/trailing whitespace
                if line:  # Check if line is not empty
                    columns = line.split('\t')  # Split each line into columns based on tab delimiter

                    # Ensure that columns list has at least 2 elements before processing
                    if len(columns) >= 2:
                        employee_number = int(columns[0]) if columns[0].strip() else None

                        # Extract only the date part from columns[1]
                        date_time_parts = columns[1].split()
                        date_only = None
                        if len(date_time_parts) > 0:
                            date_only = date_time_parts[0]  # Extract only the date part

                        # Extracting other columns
                        if len(columns) >= 6:
                            column1 = int(columns[2])
                            column2 = int(columns[3])
                            column3 = int(columns[4])
                            column4 = int(columns[5])

                        # Check if an AttendanceRecord already exists for the employee and date
                        existing_records = AttendanceRecord.objects.filter(employee_id=employee_number, date=date_only)

                        # Create a new AttendanceRecord instance if it doesn't exist
                        if existing_records.exists():
                            record = existing_records.first()
                        else:
                            record = AttendanceRecord(employee_id=employee_number, date=date_only)

                        # Assigning time components to the appropriate fields based on column values
                        # Note: I assume you want to save the full date_time string for time-related fields
                        if columns[1]:  # Check if date_time is not empty
                            if column1 == 1 and column2 == 0 and column3 == 1 and column4 == 0:
                                record.time_in = columns[1]
                            elif column1 == 1 and column2 == 1 and column3 == 1 and column4 == 0:
                                record.break_in = columns[1]
                            elif column1 == 1 and column2 == 4 and column3 == 1 and column4 == 0:
                                record.break_out = columns[1]
                            elif column1 == 1 and column2 == 5 and column3 == 1 and column4 == 0:
                                record.time_out = columns[1]

                        record.save()  # Save the record to the database

            return render(request, 'attendance/upload_success.html')
    else:
        form = FileUploadForm()
    return render(request, 'attendance/upload.html', {'form': form})


def upload_success(request):
    return render(request, 'attendance/upload_success.html')
