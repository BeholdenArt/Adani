from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse
from FeeStructure.models import FeeFormat
import pandas as pd
import csv
from django.utils.encoding import smart_str

# Create your fviews here.
def dashboard(request):
    return render(request, "FeeStructure/dashboard.html")



def enter_data(request):
    if request.method == "POST":
        receipt_number = request.POST["receipt-number"]
        received_sum = request.POST["received-sum"]
        date = request.POST['submission-date']
        student_name = request.POST['student-name']
        enrolment_number = request.POST['enrolment-number']
        semester = request.POST['semester-select']
        stream = request.POST["stream-select"]
        payment_mode = request.POST["payment-mode"]
        transaction_number = request.POST['transaction-number']
        cheque_date = request.POST["cheque-date"]

        
        print(receipt_number, received_sum, date, student_name, enrolment_number, semester, stream, payment_mode, transaction_number, cheque_date)
        
        student_data = FeeFormat(
            receipt_number= receipt_number, received_sum= received_sum, date= date, 
            student_name=student_name, enrolment_number= enrolment_number, semester= semester, 
            stream= stream, payment_mode= payment_mode, transaction_number= transaction_number,
            cheque_date= cheque_date
        )

        student_data.enrolment_number= enrolment_number
        student_data.save()

        return HttpResponse("SUCCESS")

        # redirect('insert-data')
    else:
        return render(request, "FeeStructure/insertData.html")


def retrieve_data(request):
    if request.method == "POST":
        value = request.POST['enrolment-number']
        print(value)
        student_data = FeeFormat.objects.filter(enrolment_number__exact=value)
        print(student_data.values('cheque_date'))
        # student_data = FeeFormat.objects.filter(enrolment_number__ == value)
        # print(student_data)
        return render(request, 'FeeStructure/retrieve.html', {'studentData': student_data})
    else:
        return render(request, 'FeeStructure/retrieve.html')


def download_data(request):

    if request.method == "POST":
        response = HttpResponse(content_type= 'text/csv')
        response['Content-Disposition'] = 'attachment; filename="FeeReceipt.csv"'
        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8'))

        writer.writerow([
            smart_str(u"Received Sum"),
            smart_str(u"Tuition Fees"),
            smart_str(u"Total"),
            smart_str(u"Dated"),
            smart_str(u"From"),
            smart_str(u"Enrolment Number"),
            smart_str(u"Semester"),
            smart_str(u"Payment mode"),
            smart_str(u"Transaction Number"),
            smart_str(u"Cheque Date"),
        ])
    
        value = request.POST['Enrollment']
        print(value)
        student_data = FeeFormat.objects.filter(Enrollment__exact=value)
        for student in student_data: 
            writer.writerow([ 
                smart_str(student.ReceivedFees),
                smart_str(student.TuitionFee),
                smart_str(student.Total),
                smart_str(student.Date),
                smart_str(student.Name),
                smart_str(student.Enrollment),
                smart_str(student.Sem),
                smart_str(student.MOP),
                smart_str(student.ChNo),
                smart_str(student.Date),
            ])

        return response
    else:
        return render(request, "FeeStructure/retrieve.html")
        # student_data = FeeFormat.objects.filter(enrolment_number__ == value)
        # print(student_data)
     