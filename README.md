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
