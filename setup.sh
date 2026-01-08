#!/bin/bash

# ==============================================================================
# Setup Script for HEP Analysis Environment
#
# Description:
#   Configures the local environment for 'MyLittleScriptBox'.
#
# Usage:
#   source setup.sh             # Default: Activates venv if found & sets env vars
#   source setup.sh --no-venv   # Option: Sets env vars ONLY (skips venv activation)
# ==============================================================================

# 1. Set project root directory
export MY_REPO_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VENV_NAME="toolBoxVirEnv"
VENV_DIR="$MY_REPO_ROOT/$VENV_NAME"

echo ">>> [Init] Setup environment for: $MY_REPO_ROOT"

# 2. Virtual Environment Configuration
# Check if the --no-venv argument is passed
if [[ "$1" == "--no-venv" ]]; then
    echo ">>> [Info] Skipping virtual environment activation (--no-venv flag detected)."
else
    # Check if the specific venv directory exists
    if [ -d "$VENV_DIR" ]; then
        # Check if already activated to avoid redundancy
        if [[ "$VIRTUAL_ENV" != "$VENV_DIR" ]]; then
            source "$VENV_DIR/bin/activate"
            echo ">>> [Venv] Activated virtual environment: $VENV_NAME"
        else
            echo ">>> [Venv] $VENV_NAME is already active."
        fi
    else
        echo ">>> [Info] No virtual environment named '$VENV_NAME' found. Skipping."
    fi
fi

# 3. Configure Environment Variables (PATH, PYTHONPATH)

# Add 'lib' to PYTHONPATH
if [ -d "$MY_REPO_ROOT/lib" ]; then
    # Prevent duplicate entries in PYTHONPATH
    if [[ ":$PYTHONPATH:" != *":$MY_REPO_ROOT/lib:"* ]]; then
        export PYTHONPATH="$MY_REPO_ROOT/lib:$PYTHONPATH"
        echo "    - Added 'lib/' to PYTHONPATH"
    fi
fi

# Add 'bin' to PATH
if [ -d "$MY_REPO_ROOT/bin" ]; then
    if [[ ":$PATH:" != *":$MY_REPO_ROOT/bin:"* ]]; then
        export PATH="$MY_REPO_ROOT/bin:$PATH"
        echo "    - Added 'bin/' to PATH"
    fi
fi

# Add 'scripts' to PATH (Optional)
if [ -d "$MY_REPO_ROOT/scripts" ]; then
    if [[ ":$PATH:" != *":$MY_REPO_ROOT/scripts:"* ]]; then
        export PATH="$MY_REPO_ROOT/scripts:$PATH"
        echo "    - Added 'scripts/' to PATH"
    fi
fi

echo ">>> [Ready] Environment setup complete."
