FROM prefecthq/prefect:2.20-python3.12 AS gdal-image 
# Install wget
RUN apt-get update && apt-get install -y \
    wget \
    pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Miniforge & set PATH
RUN wget -o ~/miniforge.sh -O Miniforge3.sh "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"

RUN bash Miniforge3.sh -b -p "/root/conda" && \
 bash "/root/conda/etc/profile.d/conda.sh"
ENV PATH=/root/conda/bin:$PATH 

# Install GDAL
RUN conda install gdal

FROM gdal-image AS base-image

# Install curl and other required packages
RUN apt-get update && apt-get install -y \
    curl \
    gettext \
    libssl-dev \
    python3-pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

    # Install pip packages into the base environment
RUN pip3 install --upgrade pip \
&& pip3 install \
   # prefect==2.19.4 \
    trino \
    griffe==0.49.0 \
    boto3 

# Install additional Python packages using conda-miniforge, GEOS, and PROJ
RUN conda install -n base geopandas geos shapely -y \
    && conda clean -afy

# Clean up to reduce image size
RUN apt-get remove -y wget && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set environment variables for GDAL and PROJ
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# Set the user to root to ensure appropriate permissions
USER root


WORKDIR /code
COPY ./app /code/app

ENTRYPOINT ["tail", "-f", "/dev/null"]