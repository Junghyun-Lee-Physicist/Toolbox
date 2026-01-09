````
# Toolbox

**Collection of scripts and execution files for HEP analysis.**

This repository serves as a personal toolkit for High Energy Physics (HEP) data analysis. It creates a unified environment for Python modules, shell scripts, and binaries without heavy dependencies.

## 📂 Directory Structure

```text
Toolbox/
├── bin/                 # Executable files (added to PATH)
├── lib/                 # Python modules/libraries (added to PYTHONPATH)
├── scripts/             # Miscellaneous shell scripts and utilities
├── requirements.txt     # Python dependencies list
├── setup.sh             # Environment setup script
└── README.md            # Project documentation
````

## 🚀 Environment Setup

### ⚠️ Important Note on Python Environment (HEP/CMS Context)

In High Energy Physics environments (e.g., CERN LXPLUS, Tier-2 Clusters), environment variables can be fragile. Please be aware of the following potential issues:

1.  **PYTHONPATH Sanitization:**
    * Some secure shells or environment wrapper scripts (like complex `cmsenv` setups) may **reset or sanitize** `PYTHONPATH` upon initialization. This can cause the shell to "forget" the location of `lib/`.

2.  **Python Version Mismatch (Shebang Issue):**
    * If you run `source setup.sh` under **Python 3.6**, but the script's shebang (`#!/usr/bin/env python3`) triggers a newly loaded **Python 3.9** (e.g., from a newer CMSSW release), the `PYTHONPATH` set for 3.6 might be ignored or incompatible with 3.9.

3.  **Virtual Environment Base:**
    * A virtual environment inherits the properties of the Python executable used to create it.
    * A venv created with **System Python** vs. **CMSSW Python** behaves differently. Mixing them (e.g., activating a system-based venv inside a CMSSW shell) often leads to library conflicts (binary incompatibility).

> [!WARNING]
> **Environment Loading Order is Critical!**
>
> You must execute `source setup.sh` **AFTER** establishing your base working environment (e.g., `cmsenv`, `source /cvmfs/...`).
>
> * **Correct:** `cmsenv` → `source setup.sh`
> * **Incorrect:** `source setup.sh` → `cmsenv` (Your settings will be overwritten!)

### 1. Python Virtual Environment (Optional)

To isolate dependencies, it is recommended to create a virtual environment.

> **Note:** If you are working within a **configured CMSSW environment** or already have the required modules, **you can skip this step.**

Bash

```
# 1. Create the virtual environment
python3 -m venv toolBoxVirEnv

# 2. Activate it manually for installation
source toolBoxVirEnv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

### 2. Loading the Environment

The `setup.sh` script automatically handles environment variables (PATH, PYTHONPATH) and virtual environment activation.

**Standard Usage:** Activates `toolBoxVirEnv` (if it exists) and sets up paths.

Bash

```
source setup.sh
```

**Without Virtual Environment:** Use this if you rely on system Python or CMSSW environment.

Bash

```
source setup.sh --no-venv
```

---

## 🛠 Included Tools & Usage

### 1. `count_events`

* **Dependencies:**
    * `uproot >= 5.0.0`
    * `awkward >= 2.0.0`
    * *(Install via `pip install -r requirements.txt`)*

* **Usage:**
    Ensure the script is executable: `chmod +x bin/count_events`
    
    ```bash
    # A. Single Directory (Recursive)
    count_events /data/store/user/sample_2017/

    # B. Multiple Inputs (Separate reports for each)
    count_events TTHH_TuneCP5 TTTT_TuneCP5
    # Output:
    #   [OK] TTHH_TuneCP5 -- file1.root: 500
    #   ...
    #   Summary for TTHH_TuneCP5: 15000
    #   ...
    #   Summary for TTTT_TuneCP5: 12000
    #   GRAND TOTAL: 27000

    # C. Specific Tree
    count_events ./output/ --tree Runs
    ```
