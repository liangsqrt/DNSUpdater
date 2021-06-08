FROM conda/miniconda3

MAINTAINER liangsqrt

copy ./ /root/DNSUpdater

RUN pip --disable-pip-version-check --no-cache-dir install pylint -i https://pypi.douban.com/simple \
    && if [ -f "/tmp/conda-tmp/environment.yml" ]; then /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yml; fi \
    && rm -rf /tmp/conda-tmp \
    && pip install -i https://pypi.douban.com/simple -r /root/DNSUpdater/requirements.txt