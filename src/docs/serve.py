
import os
import sys
import webbrowser
import subprocess
import time

def run_docs_server():
    """Start the main application and open the browser to the documentation page"""
    print("Starting Kasal with documentation...")
    print("Opening documentation at http://localhost:8000/docs")
    
    try:
        # Try to import the main module and run it
        from kasal import run_app
        
        # Open the documentation in a new browser tab after a short delay
        def open_browser():
            time.sleep(2)  # Give the server time to start
            webbrowser.open("http://localhost:8000/docs")
        
        # Start browser in a separate thread so it doesn't block
        import threading
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
        
        # Start the app - this will block until the server is stopped
        run_app()
    except ImportError as e:
        print(f"Error: Could not import the Kasal application. Is it installed? Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_docs_server()