### **Python Code (`ecg_analysis.py`)**

```python
import argparse
import pandas as pd
import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

def load_ecg_data(file_path):
    """Load ECG data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        if 'time' not in data.columns or 'voltage' not in data.columns:
            raise ValueError("The input file must have 'time' and 'voltage' columns.")
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        exit(1)

def analyze_ecg(data):
    """Perform detailed analysis on ECG data."""
    time = data['time']
    voltage = data['voltage']

    # Detect R-peaks
    peaks, _ = find_peaks(voltage, height=0.5, distance=200)

    # Calculate heart rate
    rr_intervals = np.diff(time[peaks])  # Time difference between consecutive R-peaks
    heart_rate = 60 / np.mean(rr_intervals)  # Convert to bpm

    # Heart rate variability
    hr_variability = np.std(rr_intervals)

    # QRS duration (simplified for example purposes)
    qrs_duration = (np.max(rr_intervals) - np.min(rr_intervals)) * 1000  # in milliseconds

    # Generate basic health insights
    consultation = "Normal ECG detected. Keep following a healthy lifestyle."

    if heart_rate < 60:
        consultation = "Bradycardia detected (low heart rate). Consult a cardiologist."
    elif heart_rate > 100:
        consultation = "Tachycardia detected (high heart rate). Consult a cardiologist."
    elif hr_variability > 0.1:
        consultation = "Possible arrhythmia detected. Consult a cardiologist."

    # Print results
    print("=== ECG Analysis Results ===")
    print(f"Heart Rate: {heart_rate:.2f} bpm")
    print(f"Heart Rate Variability: {hr_variability:.4f}")
    print(f"QRS Duration: {qrs_duration:.2f} ms")
    print("Consultation:", consultation)

    return {
        "heart_rate": heart_rate,
        "hr_variability": hr_variability,
        "qrs_duration": qrs_duration,
        "consultation": consultation
    }

def generate_report(results, output_file="ecg_report.txt"):
    """Save the analysis results into a text report."""
    with open(output_file, "w") as f:
        f.write("=== ECG Analysis Report ===\n")
        f.write(f"Heart Rate: {results['heart_rate']:.2f} bpm\n")
        f.write(f"Heart Rate Variability: {results['hr_variability']:.4f}\n")
        f.write(f"QRS Duration: {results['qrs_duration']:.2f} ms\n")
        f.write(f"Consultation: {results['consultation']}\n")
    print(f"Report saved to {output_file}")

def plot_ecg(data):
    """Plot the ECG data."""
    plt.figure(figsize=(12, 6))
    plt.plot(data['time'], data['voltage'], label="ECG Signal")
    plt.title("ECG Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (mV)")
    plt.legend()
    plt.grid()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Analyze Patient ECG Report")
    parser.add_argument("--file", required=True, help="Path to the ECG CSV file")
    args = parser.parse_args()

    # Load the ECG data
    data = load_ecg_data(args.file)

    # Analyze the ECG data
    results = analyze_ecg(data)

    # Generate a report
    generate_report(results)

    # Plot the ECG signal
    plot_ecg(data)

if __name__ == "__main__":
    main()
