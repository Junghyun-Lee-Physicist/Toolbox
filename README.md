# Toolbox
**Collection of scripts and execution files for HEP analysis.**

This repository serves as a personal toolkit for High Energy Physics (HEP) data analysis. It contains lightweight Python modules, shell scripts, and utilities designed to be easily integrated into any workflow without heavy dependencies.

## 📂 Directory Structure

```text
Toolbox/
├── bin/                 # Executable files (added to PATH)
├── lib/                 # Python modules/libraries (added to PYTHONPATH)
├── scripts/             # Miscellaneous shell scripts and utilities
├── requirements.txt     # Python dependencies list
├── setup.sh             # Environment setup script
└── README.md            # Project documentation
```

## 🚀 Environment Setup
1. Python Virtual Environment (One-time Setup)
To isolate dependencies, it is recommended to create a virtual environment named `toolBoxVirEnv`.

	Note: If you already have the required modules installed, are working within a **configured CMSSW environment**, or simply do not need a virtual environment, **you can skip this step**.

```
# 1. Create the virtual environment
python3 -m venv toolBoxVirEnv

# 2. Activate it manually for installation
source toolBoxVirEnv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

2. Loading the Environment (Daily Usage)
The `setup.sh` script automatically handles environment variables and virtual environment activation.

Standard Usage: Activates `toolBoxVirEnv` (if it exists) and sets up `PATH` & `PYTHONPATH`.

```bash
source setup.sh
```

Without Virtual Environment: If you want to use the system Python or a different environment, use the `--no-venv` flag. This only sets up the directory paths.
```bash
source setup.sh --no-venv
```

3. Deactivating the Environment
When you are done with your work, you can exit the virtual environment using the standard command:
```bash
deactivate
```

Note: `deactivate` only exits the Python virtual environment. The `PATH` and `PYTHONPATH` changes made by `setup.sh` will persist until you close the current terminal session.

📝 Usage Examples
- Python: You can import modules inside `lib/` directly.

```python
import my_analysis_tools
```

- Shell: You can run executables inside bin/ from any directory.

```bash
run_cms_job.sh --option 1
```
