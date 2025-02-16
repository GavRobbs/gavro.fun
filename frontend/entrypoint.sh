#!/bin/sh

echo "Copying built files to bind mount."
cp -r /app/dist/* /var/www/home/
echo "Built files copied."