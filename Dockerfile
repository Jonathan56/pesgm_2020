FROM python:latest

# Install glpk (glpsol):
RUN apt-get update && \
    apt-get install -y --no-install-recommends glpk-utils

# Update paths (for glpk not sure if needed):
ENV LD_LIBRARY_PATH /usr/local/lib:${LD_LIBRARY_PATH}

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Launch script
CMD ["python", "4_optimize_over_battery_size.py"]
