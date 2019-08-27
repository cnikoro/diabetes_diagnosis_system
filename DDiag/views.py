from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import DiagnosisForm
from django.urls import reverse

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpld3
import os
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.externals import joblib

"""
def test(request):
    return HttpResponse("<h1>This is only a test</h1>")
"""

def test(request):
    data=[]
    if request.method == 'POST':
        form = DiagnosisForm(request.POST)
        if form.is_valid():
            # process the form with our model
            no_preg=(form.cleaned_data['no_preg'])
            glu=form.cleaned_data["glu"]
            bp=form.cleaned_data["bp"]
            st=form.cleaned_data["st"]
            isl=form.cleaned_data["isl"]
            bmi=form.cleaned_data["bmi"]
            dpf=form.cleaned_data["dpf"]
            age=form.cleaned_data["age"]
            data = np.array([[no_preg,glu,bp,st,isl,bmi,dpf,age]])
            columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
            df = pd.DataFrame(data, columns=columns)
            print(df.shape)
            ddmodel = joblib.load('diabetesModel.pkl')
            pred = ddmodel.predict_proba(df)
            print(pred)
            predClass = pred.argmax()
            predproba = round((float(pred[0][predClass]) * 100), 2)
            ## Create a plot
            predictions = [pred[0][0], pred[0][1]]
            labels = 'Non-Diabetic', 'Diabetic'
            fig = plt.figure(figsize=(3,3))
            colors = ['red', 'green']
            #explode=(0.5,0.5)
            autopct = '%1.1f%%'
            plt.pie(predictions, labels = labels, colors=colors, autopct = autopct, shadow=True, startangle=90, rotatelabels=False)
            plt.axis('equal')
            #plt.title('Pie chart showing the prediction statistics', pad=5.5)
            graph = mpld3.fig_to_html(fig)
            display = 0
            #plt.savefig('static/graph.png')
            #path = os.path.abspath('../template')
            #os.system('touch {}/graph.html'.format(path))
            #f = open(path+'/graph.html', 'w')
            #f.write(graph)
            #f.close()
            print(predproba)
            return render(request, "home.html", {'predClass': predClass, 'probability': predproba, 'form': form, 'data': data, 'display': display, 'graph': graph})
    else:
        form = DiagnosisForm()
    return render(request, "home.html", {'form':form, 'data': data})
