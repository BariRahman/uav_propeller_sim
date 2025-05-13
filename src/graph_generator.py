import re
import matplotlib.pyplot as plt

def generate_graph(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    def extract_float(label, text, fallback=None):
        pattern = rf"{label}\s*[:=]\s*([-+]?[\d.]+(?:E[+-]?\d+)?)"
        match = re.search(pattern, text)
        return float(match.group(1)) if match else fallback

    # Extract values...
    num_blades = extract_float(r"no\. blades", content)
    radius = extract_float(r"radius\(m\)", content)
    thrust = extract_float(r"thrust\(N\)", content)
    torque = extract_float(r"torque\(N-m\)", content)
    power = extract_float(r"power\(W\)", content)
    efficiency = extract_float(r"Efficiency", content)
    speed = extract_float(r"speed\(m/s\)", content)
    rpm = extract_float(r"rpm", content)
    area = extract_float(r"Area\(m\^2\)", content)
    rho = extract_float(r"rho\(kg/m3\)", content)

    pattern = r"^\s*\d+\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+(?:s\s*)?([\d.]+)"
    matches = re.findall(pattern, content, re.MULTILINE)

    omega = 2 * 3.14159265 * rpm / 60

    r_R_vals, lift_vals = [], []

    for match in matches:
        r_R = float(match[0])
        c_R = float(match[1])
        beta = float(match[2])
        CL = float(match[3])
        Cd = float(match[4])

        c = c_R * radius
        r = r_R * radius
        V = omega * r
        lift = 0.5 * rho * c * V**2 * CL

        r_R_vals.append(r_R)
        lift_vals.append(lift)

    plt.figure(figsize=(10, 6))
    plt.plot(r_R_vals, lift_vals, marker='o', linestyle='-', color='darkgreen')
    plt.xlabel('r/R')
    plt.ylabel('Elemental Lift (N/m)')
    plt.title('Elemental Lift vs r/R')
    plt.grid(True)

    info_text = (
        f"---------------------------------------------------------------------------------------\n"
        f"|{'Blades'      :<15}: {int(num_blades):<10} |{'Radius (m)'   :<15}: {radius:<10.3f} |{'Area (m²)'     :<15}: {area:<10.5f}|\n"
        f"|{'Thrust (N)'  :<15}: {thrust:<10.3f} |{'Torque (Nm)' :<15}: {torque:<10.5f} |{'Power (W)'     :<15}: {power:<10.2f}|\n"
        f"|{'Efficiency'  :<15}: {efficiency:<10.4f} |{'Speed (m/s)' :<15}: {speed:<10.2f} |{'RPM'           :<15}: {int(rpm):<10}|\n"
        f"---------------------------------------------------------------------------------------"
    )

    plt.gca().text(0.01, -0.2, info_text,
                   fontsize=11, family='monospace',
                   ha='left', va='top', transform=plt.gca().transAxes)

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.3)
    plt.show()
