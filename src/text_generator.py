def generate_input_file(output_path, geometry_file):
    number_of_blades = int(input("Enter number of blades: "))
    speed = float(input("Enter forward speed [m/s]: "))
    tip_radius = float(input("Enter tip radius [m]: "))
    hub_radius = float(input("Enter hub radius [m]: "))
    rpm = int(input("Enter RPM: "))

    with open(geometry_file, "r") as geo_file:
        lines = geo_file.readlines()
        geometry_lines = lines[1:]  # Skip header

    with open(output_path, "w") as file:
        file.write("ARBI\n")
        file.write(f"{number_of_blades}\n")
        file.write(f"{speed}\n")
        file.write(f"{tip_radius}\n")
        file.write(f"{hub_radius}\n")
        file.write(f"{len(geometry_lines)}\n")

        for line in geometry_lines:
            file.write(line.strip() + "\n")

        file.write("n\nOPER\nRPM\n")
        file.write(f"{rpm}\n\nQUIT\n")

    print(f"[✔] Input file generated: {output_path}")
