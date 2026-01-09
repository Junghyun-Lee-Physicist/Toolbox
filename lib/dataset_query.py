#!/usr/bin/env python3
"""
CMS Dataset Query Library
=========================
Description:
    Queries the CMS Data Aggregation System (DAS) to retrieve file lists
    for a given dataset and prepends the global XRootD redirector.

Dependencies:
    - dasgoclient (Must be available in PATH, usually via cmsenv)
"""

import subprocess
import logging
import shutil
from typing import List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("DatasetQuery")

class DatasetQuery:
    def __init__(self, redirector: str = "root://cms-xrd-global.cern.ch//"):
        """
        Args:
            redirector (str): XRootD redirector to prepend (default: global cern).
        """
        self.redirector = redirector
        self._check_dependency()

    def _check_dependency(self):
        """Checks if dasgoclient is installed."""
        if not shutil.which("dasgoclient"):
            logger.error("Command 'dasgoclient' not found.")
            logger.error("Please ensure you have run 'cmsenv' and have a valid grid certificate.")
            raise RuntimeError("dasgoclient missing")

    def get_files(self, dataset_path: str) -> List[str]:
        """
        Queries DAS for the list of files.

        Args:
            dataset_path (str): The full CMS dataset path (e.g., /Dataset/../NANOAODSIM).

        Returns:
            List[str]: List of full PFNs (Physical File Names) with redirector.
        """
        logger.info(f"Querying DAS for: {dataset_path}")
        
        # Construct command: dasgoclient --query="file dataset=..." --limit=0
        query = f"file dataset={dataset_path}"
        cmd = ["dasgoclient", "--query", query, "--limit=0"]

        try:
            # Execute command
            result = subprocess.run(
                cmd, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                text=True, 
                check=True
            )
            
            # Process output
            files = result.stdout.strip().split('\n')
            files = [f.strip() for f in files if f.strip()] # Remove empty lines

            if not files:
                logger.warning(f"No files found for: {dataset_path}")
                return []

            logger.info(f" -> Found {len(files)} files.")
            
            # Add redirector
            full_paths = [self.redirector + f for f in files]
            return full_paths

        except subprocess.CalledProcessError as e:
            logger.error(f"DAS query failed: {e.stderr}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return []
