import subprocess

def run_xrotor(xrotor_path, input_path, output_path):
    print("[...] Running xrotor...")
    result = subprocess.run(f'"{xrotor_path}" < {input_path} > {output_path}', shell=True)
    if result.returncode != 0:
        raise RuntimeError("xrotor failed to run.")
    print(f"[✔] xrotor completed: {output_path}")
