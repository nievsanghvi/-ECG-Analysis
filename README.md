ECG Analysis Program
Overview
This is a Python-based application designed to analyze ECG (Electrocardiogram) signals and provide detailed heart health insights. The program processes ECG data entered as time-voltage pairs, detects abnormalities, calculates key cardiac metrics (e.g., heart rate, variability, QRS duration), and generates a consultation report.

Features
Input ECG Data: Accepts ECG data (time and voltage) interactively via user input.
Peak Detection: Identifies peaks (R-peaks) in the ECG signal to compute metrics.
Cardiac Metrics Calculation:
Heart rate (bpm)
Heart rate variability (ms)
QRS duration (ms)
Abnormality Detection: Detects common abnormalities such as:
Bradycardia (low heart rate)
Tachycardia (high heart rate)
Arrhythmias (irregular heart activity)
Health Recommendations: Provides health consultation based on analysis.
Report Generation: Saves the complete analysis results in a text file (ecg_report.txt).
Manual Plot Display: Displays time-voltage data for external plotting tools if needed.
