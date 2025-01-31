import re
from email import message_from_string

def extract_ip_from_header(email_header):
    """Extract the IP address from the email header."""
    # Parse the email header
    msg = message_from_string(email_header)
    
    # Look for the "Received" field in the headers (which contains the IP)
    received_header = msg.get_all('Received')
    
    # Regex to match IP address patterns in the Received headers
    ip_pattern = r'\[([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\]'
    
    for header in received_header:
        # Search for IP address in each Received header
        match = re.search(ip_pattern, header)
        if match:
            return match.group(1)
    return None

def save_ip_to_file(ip, file_path="input.txt"):
    """Save the IP address to a file, one IP per line (appending if file exists)."""
    with open(file_path, "a") as file:  # Open in append mode ('a')
        if ip:
            file.write(ip + "\n")
        else:
            # If no IP is found, ensure the file is empty (optional)
            file.write("") 

# Example Email Header (replace with your actual email header)
email_header = """Received: from example.com (example.com [192.168.0.1])
                  by mail.example.com with ESMTP; Wed, 30 Jan 2025 10:20:45 -0500"""

# Extract the IP address
ip = extract_ip_from_header(email_header)

# Save the IP address to input.txt (appending if the file already exists)
save_ip_to_file(ip)

# Print the result
if ip:
    print(f"IP Address Found: {ip}")
else:
    print("No IP Address found.")
