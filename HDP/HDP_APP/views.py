from django.shortcuts import render,HttpResponse
from HDP_APP.models import Home
from joblib import load
import numpy as np

# Create your views here.
def index(request):
    return render(request, 'home.html')
    
def model_sel(request):
    return render(request, 'model_sel.html')

# Logistic Regression
def log_reg_page(request):
    return render(request, 'logreg.html')

def log_reg_pred(request):
    if request.method == "POST":
        age = float(request.POST.get("age"))
        sex = request.POST.get("sex")
        cp = float(request.POST.get("cp"))
        trestbps = float(request.POST.get("trestbps"))
        chol = float(request.POST.get("chol"))
        fbs = request.POST.get("fbs")
        restecg = float(request.POST.get("restecg"))
        thalach = float(request.POST.get("thalach"))
        exang = request.POST.get("exang")
        oldpeak = float(request.POST.get("oldpeak"))
        slope = float(request.POST.get("slope"))
        ca = float(request.POST.get("ca"))
        thal = float(request.POST.get("thal"))

        if sex.lower() == "male":
            sex = 1
        else:
            sex = 0
            
        if fbs.lower() == "yes":
            fbs = 1
        else:
            fbs = 0
            
        if exang.lower() == "yes":
            exang = 1
        else:
            exang = 0
                
        # home = Home(age=age)
        # home.save()
        
        model = load(r'SkModels/HDP_LogReg_Model.joblib')
        features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if model.predict(features) == 0:
            prediction = "Heart is healthy"
        else:
            prediction = "Heart is not healthy"
        
        testacc = "90.32%"
        
        model = "Logistic Regressor"
        return render(request, 'status.html', {'ans': prediction, 'mod': model, 'acc': testacc})
    
# Decision Tree Regressor
def dec_tree_page(request):
    return render(request, 'dectree.html')

def dec_tree_pred(request):
    if request.method == "POST":
        age = float(request.POST.get("age"))
        sex = request.POST.get("sex")
        cp = float(request.POST.get("cp"))
        trestbps = float(request.POST.get("trestbps"))
        chol = float(request.POST.get("chol"))
        fbs = request.POST.get("fbs")
        restecg = float(request.POST.get("restecg"))
        thalach = float(request.POST.get("thalach"))
        exang = request.POST.get("exang")
        oldpeak = float(request.POST.get("oldpeak"))
        slope = float(request.POST.get("slope"))
        ca = float(request.POST.get("ca"))
        thal = float(request.POST.get("thal"))
        
        if sex.lower() == "male":
            sex = 1
        else:
            sex = 0
            
        if fbs.lower() == "yes":
            fbs = 1
        else:
            fbs = 0
            
        if exang.lower() == "yes":
            exang = 1
        else:
            exang = 0
    
        model = load(r'SkModels/HDP_DecTreReg_Model.joblib')
        features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if model.predict(features) == 0:
            prediction = "Heart is healthy"
        else:
            prediction = "Heart is not healthy"
        
        testacc = "83.87%"
        
        model = "Decision Tree Classifier"
        return render(request, 'status.html', {'ans': prediction, 'mod': model, 'acc': testacc})

# Random Forest Classifier
def ran_for_cla_page(request):
    return render(request, 'ranforclass.html')

def ran_for_cla_pred(request):
    if request.method == "POST":
        age = float(request.POST.get("age"))
        sex = request.POST.get("sex")
        cp = float(request.POST.get("cp"))
        trestbps = float(request.POST.get("trestbps"))
        chol = float(request.POST.get("chol"))
        fbs = request.POST.get("fbs")
        restecg = float(request.POST.get("restecg"))
        thalach = float(request.POST.get("thalach"))
        exang = request.POST.get("exang")
        oldpeak = float(request.POST.get("oldpeak"))
        slope = float(request.POST.get("slope"))
        ca = float(request.POST.get("ca"))
        thal = float(request.POST.get("thal"))
        
        if sex.lower() == "male":
            sex = 1
        else:
            sex = 0
            
        if fbs.lower() == "yes":
            fbs = 1
        else:
            fbs = 0
            
        if exang.lower() == "yes":
            exang = 1
        else:
            exang = 0
    
        model = load(r'SkModels/HDP_RanForCla_Model.joblib')
        features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        
        if model.predict(features) == 0:
            prediction = "Heart is healthy"
        else:
            prediction = "Heart is not healthy"
        
        testacc = "93.55%"
        
        model = "Random Forest Classifier"
        return render(request, 'status.html', {'ans': prediction, 'mod': model, 'acc': testacc})
    
# K-Neighbours Classifier
def kn_class_page(request):
    return render(request, 'knclass.html')

def kn_class_pred(request):
    if request.method == "POST":
        age = float(request.POST.get("age"))
        sex = request.POST.get("sex")
        cp = float(request.POST.get("cp"))
        trestbps = float(request.POST.get("trestbps"))
        chol = float(request.POST.get("chol"))
        fbs = request.POST.get("fbs")
        restecg = float(request.POST.get("restecg"))
        thalach = float(request.POST.get("thalach"))
        exang = request.POST.get("exang")
        oldpeak = float(request.POST.get("oldpeak"))
        slope = float(request.POST.get("slope"))
        ca = float(request.POST.get("ca"))
        thal = float(request.POST.get("thal"))
    
        if sex.lower() == "male":
            sex = 1
        else:
            sex = 0
            
        if fbs.lower() == "yes":
            fbs = 1
        else:
            fbs = 0
            
        if exang.lower() == "yes":
            exang = 1
        else:
            exang = 0
    
        model = load(r'SkModels/HDP_KNClass_Model.joblib')
        features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if model.predict(features) == 0:
            prediction = "Heart is healthy"
        else:
            prediction = "Heart is not healthy"
        
        testacc = "82.42%"
        
        model = "K-Neighbours Classifier"
        return render(request, 'status.html', {'ans': prediction, 'mod': model, 'acc': testacc})

# Linear Support Vector Classifier
def lin_svc_page(request):
    return render(request, 'linsvc.html')

def lin_svc_pred(request):
    if request.method == "POST":
        age = float(request.POST.get("age"))
        sex = request.POST.get("sex")
        cp = float(request.POST.get("cp"))
        trestbps = float(request.POST.get("trestbps"))
        chol = float(request.POST.get("chol"))
        fbs = request.POST.get("fbs")
        restecg = float(request.POST.get("restecg"))
        thalach = float(request.POST.get("thalach"))
        exang = request.POST.get("exang")
        oldpeak = float(request.POST.get("oldpeak"))
        slope = float(request.POST.get("slope"))
        ca = float(request.POST.get("ca"))
        thal = float(request.POST.get("thal"))
        
        if sex.lower() == "male":
            sex = 1
        else:
            sex = 0
            
        if fbs.lower() == "yes":
            fbs = 1
        else:
            fbs = 0
            
        if exang.lower() == "yes":
            exang = 1
        else:
            exang = 0
    
        model = load(r'SkModels/HDP_LinSVC_Model.joblib')
        features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if model.predict(features) == 0:
            prediction = "Heart is healthy"
        else:
            prediction = "Heart is not healthy"
        
        testacc = "87.10%"
        
        model = "Linear Support Vector Classifier"
        return render(request, 'status.html', {'ans': prediction, 'mod': model, 'acc': testacc})