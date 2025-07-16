from django.shortcuts import render
from .forms import PatientForm
import joblib
import numpy as np
from .models import PatientRecord

# Load model once when server starts
model = joblib.load('model.pkl')

def index(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            features = np.array([[data['age'], data['cholesterol'], data['blood_pressure'], data['max_heart_rate']]])
            prediction = model.predict(features)[0]

            # Save to DB
            record = PatientRecord(
                age=data['age'],
                cholesterol=data['cholesterol'],
                blood_pressure=data['blood_pressure'],
                max_heart_rate=data['max_heart_rate'],
                prediction=bool(prediction)
            )
            record.save()

            return render(request, 'predictor/result.html', {'prediction': prediction})
    else:
        form = PatientForm()
    return render(request, 'predictor/index.html', {'form': form})

from django.shortcuts import render

def index(request):
    if request.method == "POST":
        # Your prediction logic here...
        prediction = ... # True or False result

        # Render result page or same page with prediction
        return render(request, 'predictor/result.html', {'prediction': prediction})

    # GET request: just show the form
    return render(request, 'predictor/index.html')

