# a_calculate_real_size.py

def calculate_real_size(microscope_size, magnification):
    return microscope_size / magnification

def main():
    specimen = input("Enter specimen name: ")
    microscope_size = float(input("Enter microscope size (μm): "))
    magnification = float(input("Enter magnification level: "))
    actual_size = calculate_real_size(microscope_size, magnification)
    print(f"The actual size of {specimen} is approximately {actual_size:.2f} μm.")

if __name__ == "__main__":
    main()
