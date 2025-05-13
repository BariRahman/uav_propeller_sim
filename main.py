from datetime import datetime
import os

from src import text_generator, graph_generator, xrotor_runner

# === Timestamp ===
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# === Paths ===
input_folder = "input_data"
results_folder = "results"
geometry_file = "geometry/propeller_geometry.txt"
xrotor_path = "xrotor.exe"  # Adjust if it's somewhere else

os.makedirs(input_folder, exist_ok=True)
os.makedirs(results_folder, exist_ok=True)

input_filename = f"input_{timestamp}.txt"
output_filename = f"result_{timestamp}.txt"

input_path = os.path.join(input_folder, input_filename)
output_path = os.path.join(results_folder, output_filename)

# === Run steps ===
text_generator.generate_input_file(input_path, geometry_file)
xrotor_runner.run_xrotor(xrotor_path, input_path, output_path)
graph_generator.generate_graph(output_path)
