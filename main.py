# ============================================
# MAIN.PY - Start All Servers at Once!
# ============================================
# This file starts all 3 API servers together
# so you don't need to open 3 separate terminals.
#
# Just run: python main.py
# ============================================

# Import subprocess to run multiple Python processes
import subprocess
import sys
import time

# List of all our API servers with their port numbers
# Each tuple contains: (file_name, port_number, description)
servers = [
    ("student_app", 8001, "Student Performance Predictor"),
    ("patient_risk_app", 8002, "Patient Risk Checker"),
    ("waiting_time_app", 8003, "Waiting Time Estimator"),
]


def start_all_servers():
    """
    This function starts all 3 API servers at the same time.
    Each server runs in its own process (like opening separate terminals).
    """
    
    print("=" * 50)
    print("🚀 STARTING ALL AI DASHBOARD SERVERS")
    print("=" * 50)
    print()
    
    # This list will hold all running processes
    processes = []
    
    # Loop through each server and start it
    for app_name, port, description in servers:
        
        # Build the command to run uvicorn
        # This is the same as typing: uvicorn student_app:app --port 8001
        command = [
            sys.executable,  # This gets the current Python interpreter
            "-m",            # Run as a module
            "uvicorn",       # The uvicorn server
            f"{app_name}:app",  # The app to run (filename:app_variable)
            "--port", str(port),  # The port number
            "--reload"       # Auto-reload when code changes
        ]
        
        # Start the server in a new process
        # shell=False is safer, stdout/stderr show in console
        process = subprocess.Popen(command)
        
        # Add this process to our list
        processes.append(process)
        
        # Print a message so user knows what's happening
        print(f"✅ Started: {description}")
        print(f"   → Running on: http://localhost:{port}")
        print()
        
        # Small delay between starting each server
        time.sleep(1)
    
    print("=" * 50)
    print("🎉 ALL SERVERS ARE RUNNING!")
    print("=" * 50)
    print()
    print("📌 Open index.html in your browser to use the dashboard")
    print()
    print("🔗 API Endpoints:")
    print("   • Student API:  http://localhost:8001")
    print("   • Patient API:  http://localhost:8002")
    print("   • Waiting API:  http://localhost:8003")
    print()
    print("⚠️  Press Ctrl+C to stop all servers")
    print("=" * 50)
    
    # Keep the script running and wait for all processes
    # This also allows us to catch Ctrl+C to stop everything
    try:
        # Wait for all processes (this keeps the script running)
        for process in processes:
            process.wait()
    except KeyboardInterrupt:
        # User pressed Ctrl+C, so we stop all servers
        print()
        print("🛑 Stopping all servers...")
        
        # Kill each process
        for process in processes:
            process.terminate()
        
        print("✅ All servers stopped. Goodbye!")


# This runs when you execute: python main.py
if __name__ == "__main__":
    start_all_servers()
