import csv
from datetime import datetime

DATA_FILE = "health_data.csv"

def initialize_file():
    try:
        with open(DATA_FILE, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Steps", "Calories", "Sleep (hrs)", "Heart Rate", "Health Score"])
    except FileExistsError:
        pass

def calculate_health_score(steps, calories, sleep, heart_rate):
    score = 0
    score += min(steps / 10000, 1) * 25
    score += min(calories / 2000, 1) * 25
    score += min(sleep / 8, 1) * 25
    score += max(0, (70 - abs(heart_rate - 70)) / 70) * 25
    return round(score, 2)

def add_health_data():
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    steps = int(input("Enter steps walked today: "))
    calories = int(input("Enter calories consumed: "))
    sleep = float(input("Enter sleep hours: "))
    heart_rate = int(input("Enter average heart rate: "))

    score = calculate_health_score(steps, calories, sleep, heart_rate)

    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, steps, calories, sleep, heart_rate, score])

    print(f"\n✅ Data added successfully! Your Health Score: {score}/100")
    show_health_tip(score)

def show_health_tip(score):
    print("\n💡 Health Tip:")
    if score >= 80:
        print("Excellent! Keep maintaining your healthy lifestyle! 🏆")
    elif score >= 60:
        print("Good job! Try adding more physical activity to your day 💪")
    elif score >= 40:
        print("You need to improve your sleep and diet habits 🌿")
    else:
        print("Warning! Focus on balanced diet, regular exercise, and sleep! ⚠️")

def show_all_data():
    print("\n📊 Health Data Records:\n")
    with open(DATA_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def main():
    initialize_file()
    while True:
        print("\n========= Health Monitoring System =========")
        print("1. Add Daily Health Data")
        print("2. View All Records")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_health_data()
        elif choice == "2":
            show_all_data()
        elif choice == "3":
            print("Exiting... Stay healthy! ❤️")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
