#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p /tmp/rh-verification
for f in \
 certificates/riemann_phase9_weighted_sign.cpp \
 certificates/riemann_phase10_weighted_sign_certificate.cpp \
 certificates/riemann_phase12_alpha2_certificate.cpp \
 certificates/riemann_phase13_sign_window.cpp
do
 name=$(basename "$f" .cpp)
 echo "Compiling $f"
 g++ -O3 -std=c++17 -Wall -Wextra "$f" -o "/tmp/rh-verification/$name"
 echo "Executing $name"
 "/tmp/rh-verification/$name"
done
echo "All four finite verification programs completed."
