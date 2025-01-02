ECG Analysis Program
Overview
The ECG Analysis Program is a Python-based application designed to analyze ECG (Electrocardiogram) signals and provide detailed heart health insights. The program processes ECG data entered interactively as time-voltage pairs, detects abnormalities, calculates key cardiac metrics, and generates a consultation report summarizing the findings.

Features
1. Input ECG Data
Accepts ECG data input (time and voltage pairs) interactively via the terminal.
Provides flexibility for users to manually input data.
2. Peak Detection
Identifies R-peaks in the ECG signal using a threshold-based algorithm.
Helps analyze the electrical activity of the heart.
3. Cardiac Metrics Calculation
The application computes the following critical metrics:

Heart Rate (bpm): The number of beats per minute based on detected peaks in the ECG signal.
Heart Rate Variability (ms): The variation in RR intervals, useful for detecting irregularities.
QRS Duration (ms): The time taken by the QRS complex (ventricular depolarization).
4. Abnormality Detection
Detects potential abnormalities in the ECG signal and provides health insights, such as:
Bradycardia: Low heart rate (< 60 bpm).
Tachycardia: High heart rate (> 100 bpm).
Arrhythmia: Irregular heart activity detected through variability patterns.
5. Health Recommendations
Generates recommendations based on ECG analysis results, such as advising consulting a cardiologist for abnormalities.
6. Report Generation
Saves the analysis results (heart rate, heart rate variability, QRS duration, and consultation) into a text file named ecg_report.txt for record-keeping.
7. Manual Plot Display
Outputs the time-voltage data in text format for manual plotting using external tools (e.g., Excel, Matplotlib) if required.
