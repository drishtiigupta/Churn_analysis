from django.shortcuts import render

from joblib import load
model = load('./savedModels/learnandbuild.joblib')

def predictor(request):
    if request.method == 'POST':
        tenure = request.POST['tenure']
        SeniorCitizen = request.POST['SeniorCitizen']
        Contract = request.POST['Contract']
        PaperlessBilling = request.POST['PaperlessBilling']
        MonthlyCharges = request.POST['MonthlyCharges']
        y_pred = model.predict([[ tenure	,SeniorCitizen,	Contract	,PaperlessBilling,	MonthlyCharges]])
        if y_pred[0] == 0:
            y_pred = 'Customer will Not Churn out'
        elif y_pred[0] == 1: 
            y_pred = 'Customer will Churn out'
        else:
            y_pred = 'There is some error in data'
        return render(request, 'result.html', {'result' : y_pred})
    return render(request, 'main.html')
