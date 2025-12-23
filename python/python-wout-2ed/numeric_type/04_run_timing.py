def run_timing() -> None:
    """
    10km Run Time Calculator

    Example usage:
    $ python3 04_run_timing.py
    Enter 10 km run time: 10
    Enter 10 km run time: 20
    Enter 10 km run time: 30
    Enter 10 km run time: q
    Average of 20.00 minutes, over 3 runs
    """
    number_of_runs = 0
    total_time = 0

    while True:
        user_input = input("Enter 10 km run time: ")

        if user_input.lower() == 'q':
            break
        try:
            one_run = float(user_input)
            if one_run < 0:
                print("Time cannot be negative. Please try again.")
                continue
            number_of_runs += 1
            total_time += one_run                    
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
            continue

    if number_of_runs > 0:
        average_time = total_time / number_of_runs
        print(f"Average of {average_time:.2f} minutes, over {number_of_runs} runs")
    else:
        print("No runs recorded.")


def main() -> None:
    run_timing()

if __name__ == "__main__":
    main()
