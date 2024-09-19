#!/bin/bash

# Copyright 2023 PickNik Inc.
# All rights reserved.
#
# Unauthorized copying of this code base via any medium is strictly prohibited.
# Proprietary and confidential.

# Script to call the isaac launch system (see python.sh in the ISAAC_SCRIPT_DIR)
source /opt/ros/humble/setup.bash
ISAAC_SCRIPT_DIR=/isaac-sim
CUR_SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
NEW_ARGS=""
for arg in "$@"
do
    NEW_ARGS="${NEW_ARGS} ${CUR_SCRIPT_DIR}/${arg}"
done

pushd $ISAAC_SCRIPT_DIR
./python.sh $NEW_ARGS
popd
