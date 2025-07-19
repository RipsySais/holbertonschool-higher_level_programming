#!/usr/bin/env python3
"""
Generates personalized invitation files based on a template and a list of attendees.
Handles various error cases gracefully.
"""

import os
import logging

# Configure logging to show messages on the console
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def generate_invitations(template, attendees):
    """
    Generate personalized invitation files using the given template and attendee data.

    Parameters:
    - template (str): The string template containing placeholders.
    - attendees (list): A list of dictionaries containing attendee information.
    """

    # --- Step 1: Validate input types ---
    if not isinstance(template, str):
        logging.error("Invalid template type: expected string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        logging.error("Invalid attendees type: expected a list of dictionaries.")
        return

    # --- Step 2: Handle empty inputs ---
    if template.strip() == "":
        logging.error("Template is empty, no output files generated.")
        return
    if not attendees:
        logging.info("No data provided, no output files generated.")
        return

    # --- Step 3: Process each attendee ---
    for idx, attendee in enumerate(attendees, start=1):
        # Copy template to a new string to personalize
        personalized = template

        # Define required placeholders
        placeholders = ["name", "event_title", "event_date", "event_location"]

        # Replace each placeholder with the corresponding value or 'N/A' if missing or None
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            personalized = personalized.replace(f"{{{key}}}", str(value))

        # --- Step 4: Write output file ---
        output_filename = f"output_{idx}.txt"
        try:
            with open(output_filename, 'w') as f:
                f.write(personalized)
            logging.info(f"Generated {output_filename}")
        except Exception as e:
            logging.error(f"Failed to write {output_filename}: {e}")
