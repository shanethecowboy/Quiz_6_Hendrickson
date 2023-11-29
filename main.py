import tkinter as tk
from tkinter import ttk
from app.functions import add_numbers, subtract_numbers, divide_numbers, multiply_numbers

def main():
    def calculate_numbers():
        try:
            # Get user inputs
            first_name = entry_first_name.get()
            last_name = entry_last_name.get()
            num1 = float(entry_num1.get())
            num2 = float(entry_num2.get())

            # Perform calculations
            add_result = add_numbers(num1, num2)
            subtract_result = subtract_numbers(num1, num2)
            divide_result = divide_numbers(num1, num2)
            multiply_result = multiply_numbers(num1, num2)

            # Display formatted results in the GUI
            result_text.set(f"{first_name}'s results:\n"
                            f"{num1} + {num2} = {add_result}\n"
                            f"{num1} - {num2} = {subtract_result}\n"
                            f"{num1} / {num2} = {round(divide_result, 2)}\n"
                            f"{num1} * {num2} = {multiply_result}")

            # Write results to a text file with error handling
            filename = f"{last_name.lower()}.txt"
            with open(filename, 'w') as file:
                file.write(result_text.get())

        except ValueError:
            result_text.set("Error: Please enter valid numerical values.")

    # Create the main GUI window
    root = tk.Tk()
    root.title("Number Calculator")

    # Create and place widgets in the GUI
    frame = ttk.Frame(root, padding="10")
    frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(frame, text="First Name:").grid(column=0, row=0, sticky=tk.W)
    entry_first_name = ttk.Entry(frame)
    entry_first_name.grid(column=1, row=0, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="Last Name:").grid(column=0, row=1, sticky=tk.W)
    entry_last_name = ttk.Entry(frame)
    entry_last_name.grid(column=1, row=1, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="Number 1:").grid(column=0, row=2, sticky=tk.W)
    entry_num1 = ttk.Entry(frame)
    entry_num1.grid(column=1, row=2, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="Number 2:").grid(column=0, row=3, sticky=tk.W)
    entry_num2 = ttk.Entry(frame)
    entry_num2.grid(column=1, row=3, sticky=(tk.W, tk.E))

    result_text = tk.StringVar()
    ttk.Label(frame, textvariable=result_text).grid(column=0, row=4, columnspan=2, sticky=tk.W)

    calculate_button = ttk.Button(frame, text="Calculate", command=calculate_numbers)
    calculate_button.grid(column=0, row=5, columnspan=2, sticky=(tk.W, tk.E))

    # Run the main loop
    root.mainloop()

# Call the main function when the script is executed
if __name__ == "__main__":
    main()
