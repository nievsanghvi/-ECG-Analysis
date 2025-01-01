import argparse


def load_ecg_data():
    """Load ECG data by accepting input for time and voltage."""
    print("Enter the ECG data as time-voltage pairs. Enter 'done' when finished:")
    time = []
    voltage = []

    while True:
        user_input = input("Enter time and voltage separated by a space (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            t, v = user_input.split()
            time.append(float(t))
            voltage.append(float(v))
        except ValueError:
            print("Invalid input! Please enter two numbers separated by a space.")

    if not time or not voltage:
        print("No data provided. Exiting.")
        exit(1)
    
    return time, voltage


def find_peaks(voltage, height=0.5, min_distance=200):
    """Basic peak detection algorithm."""
    peaks = []

    for i in range(1, len(voltage) - 1):
        if voltage[i] >= height and voltage[i] > voltage[i - 1] and voltage[i] > voltage[i + 1]:
            if not peaks or (i - peaks[-1]) >= min_distance:
                peaks.append(i)

    return peaks


def analyze_ecg(time, voltage):
    """Perform detailed analysis on ECG data."""
    # Detect R-peaks
    peaks = find_peaks(voltage, height=0.5, min_distance=200)

    # Calculate RR intervals
    rr_intervals = [time[peaks[i+1]] - time[peaks[i]] for i in range(len(peaks) - 1)]
    heart_rate = 60 / (sum(rr_intervals) / len(rr_intervals)) if rr_intervals else 0
    hr_variability = (max(rr_intervals) - min(rr_intervals)) if rr_intervals else 0
    qrs_duration = (max(rr_intervals) - min(rr_intervals)) * 1000 if rr_intervals else 0

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


def plot_ecg(time, voltage):
    """Plot the ECG data."""
    print("\n=== ECG Signal Plot ===")
    print(f"Time (s):   {' '.join(map(str, time))}")
    print(f"Voltage (mV): {' '.join(map(str, voltage))}")
    print("NOTE: To view a proper graph, you would need to use an external plotting tool like Excel.")


def main():
    """Main function."""
    print("ECG Analysis Program")
    time, voltage = load_ecg_data()  # Load ECG data directly from user input

    # Analyze the ECG data
    results = analyze_ecg(time, voltage)

    # Generate a report
    generate_report(results)

    # Display the ECG data for manual plotting
    plot_ecg(time, voltage)


if __name__ == "__main__":
    main()
