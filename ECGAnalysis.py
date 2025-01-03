import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

def get_ecg_data():
    """Manually input time and voltage data."""
    # Example data: Hardcoded time and voltage values
    time = np.array([0.016, 0.032, 0.048, 0.064, 0.080])
    voltage = np.array([0.21, 0.23, 0.19, 0.25, 0.20])

    # Display provided data for reference
    print("Time Data (s):", time)
    print("Voltage Data (mV):", voltage)
    return time, voltage

def analyze_ecg(time, voltage):
    """Perform detailed analysis on ECG data."""
    # Detect R-peaks
    peaks, _ = find_peaks(voltage, height=0.2, distance=1)  # Adjust height and distance as needed

    # Calculate heart rate (per minute)
    rr_intervals = np.diff(time[peaks])  # Time difference between consecutive R-peaks
    heart_rate = 60 / np.mean(rr_intervals) if len(rr_intervals) > 0 else 0  # Convert to bpm

    # Heart rate variability
    hr_variability = np.std(rr_intervals) if len(rr_intervals) > 1 else 0

    # QRS duration (simplified for example purposes)
    qrs_duration = (np.max(rr_intervals) - np.min(rr_intervals)) * 1000 if len(rr_intervals) > 1 else 0  # in ms

    # Generate basic health insights based on heart rate
    consultation = "Normal ECG detected. Keep following a healthy lifestyle."

    if heart_rate < 60 and len(rr_intervals) > 0:
        consultation = "Bradycardia detected (low heart rate). Consult a cardiologist."
    elif heart_rate > 100:
        consultation = "Tachycardia detected (high heart rate). Consult a cardiologist."
    elif hr_variability > 0.1:
        consultation = "Possible arrhythmia detected. Consult a cardiologist."

    # Print results
    print("\n=== ECG Analysis Results ===")
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

def plot_ecg(time, voltage):
    """Plot the ECG data."""
    plt.figure(figsize=(12, 6))
    plt.plot(time, voltage, label="ECG Signal", color='r')
    plt.title("ECG Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (mV)")
    plt.legend()
    plt.grid(color="white")
    plt.gca().set_facecolor("white")  # Set white background
    plt.show()

def main():
    # Get time and voltage data (either manually or hard-coded)
    time, voltage = get_ecg_data()

    # Perform analysis on the data
    results = analyze_ecg(time, voltage)

    # Plot the ECG signal
    plot_ecg(time, voltage)

    # Summary Report in Terminal
    print("\n=== ECG Report ===")
    for key, value in results.items():
        print(f"{key.replace('_', ' ').capitalize()}: {value}")

# Entry point for the script
if __name__ == "__main__":
    main()
