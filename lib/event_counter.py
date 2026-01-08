#!/usr/bin/env python3
"""
ROOT Event Counter Library
==========================
Description:
    A utility class to recursively scan directories or specific files for ROOT files
    and count the total number of entries in a specific Tree using Uproot.

Features:
    - Fast metadata reading (lazy loading).
    - Recursive directory scanning.
    - Specific file targeting.

Dependencies:
    - uproot >= 5.0.0
    - awkward >= 2.0.0 (usually installed with uproot)

Usage as Library:
    -------------------------------------------------------------------
    from event_counter import EventCounter, expand_file_paths

    # 1. Get list of files (handles recursion automatically)
    files = expand_file_paths(["./data", "./output/test.root"])

    # 2. Count events
    counter = EventCounter(tree_name="Events")
    total = counter.count(files)
    print(f"Total events: {total}")
    -------------------------------------------------------------------

Usage as Script:
    python event_counter.py ./data/ --tree Events
"""

import uproot
import logging
import argparse
import sys
from pathlib import Path
from typing import List

# Configure logging to stdout
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("EventCounter")

def expand_file_paths(input_paths: List[str]) -> List[Path]:
    """
    Takes a list of strings (files or directories) and returns a flat list of 
    resolved Path objects. Directories are scanned recursively for *.root files.
    """
    resolved_files = []
    
    for p_str in input_paths:
        path = Path(p_str).resolve()
        
        if not path.exists():
            logger.warning(f"Path does not exist: {path}")
            continue

        if path.is_file():
            if path.suffix == ".root":
                resolved_files.append(path)
            else:
                logger.debug(f"Skipping non-ROOT file: {path.name}")
                
        elif path.is_dir():
            logger.info(f"Scanning directory (recursive): {path}")
            found = list(path.rglob("*.root"))
            logger.info(f"  -> Found {len(found)} ROOT files in {path.name}")
            resolved_files.extend(found)
            
    return sorted(list(set(resolved_files)))

class EventCounter:
    def __init__(self, tree_name: str = "Events"):
        self.tree_name = tree_name

    def count(self, file_paths: List[Path]) -> int:
        total_events = 0
        
        if not file_paths:
            logger.warning("No files provided to count.")
            return 0

        logger.info(f"Starting count for Tree: '{self.tree_name}'")
        
        for file_path in file_paths:
            try:
                # Open file lazily (only reads header)
                with uproot.open(file_path) as f:
                    if self.tree_name in f:
                        n_entries = f[self.tree_name].num_entries
                        total_events += n_entries
                        logger.info(f"  [OK] {file_path.name}: {n_entries} events")
                    else:
                        logger.warning(f"  [SKIP] Tree '{self.tree_name}' not found in {file_path.name}")
            
            except Exception as e:
                logger.error(f"  [ERR] Failed to read {file_path.name}: {e}")

        return total_events

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recursively count events in ROOT files.")
    parser.add_argument("inputs", nargs='+', help="Input files or directories")
    parser.add_argument("--tree", "-t", default="Events", help="Target TTree name")
    
    args = parser.parse_args()
    target_files = expand_file_paths(args.inputs)
    
    if not target_files:
        logger.error("No ROOT files found.")
        sys.exit(1)

    counter = EventCounter(tree_name=args.tree)
    grand_total = counter.count(target_files)
    
    print("=" * 50)
    print(f" GRAND TOTAL : {grand_total}")
    print("=" * 50)
