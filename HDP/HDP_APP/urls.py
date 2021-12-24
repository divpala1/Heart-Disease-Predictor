from django.contrib import admin
from django.urls import path, include
from HDP_APP import views

urlpatterns = [
    # path('', views.index, name="homepage"),
    path('', views.model_sel, name='homepage'),
    
    # Logistic Regression
    path('LogisticRegression', views.log_reg_page, name='LogRegPage'),
    path('LogisticRegressionPrediction', views.log_reg_pred, name='LogRegPrediction'),
    
    # Decision Tree Regressor
    path('DecisionTreeRegressor', views.dec_tree_page, name='DecTreePage'),
    path('DecisionTreeRegressorPrediction', views.dec_tree_pred, name='DecTreePrediction'),
    
    # Random Forest Classifier
    path('RandomForestClassifier', views.ran_for_cla_page, name='RFCPage'),
    path('RandomForestClassifierPrediction', views.ran_for_cla_pred, name='RFCPrediction'),
    
    # K-Neighbours Classifier
    path('KNeighboursClassifier', views.kn_class_page, name='KNClassPage'),
    path('KNeighboursClassifierPrediction', views.kn_class_pred, name='KNClassPrediction'),
    
    # Linear Support Vector Classifier
    path('LinearSVC', views.lin_svc_page, name='LinSVCPage'),
    path('LinearSVCPrediction', views.lin_svc_pred, name='LinSVCPrediction'),
]