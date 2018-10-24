#!/bin/sh

echo "Removing old code..."
rm -rf go-corpus
rm -rf c-corpus

echo "Cloning Go corpus..."
git clone https://github.com/kubernetes/kubernetes.git go-corpus/kubernetes
# git clone https://github.com/istio/istio.git go-corpus/istio
# git clone https://github.com/hashicorp/terraform.git go-corpus/terraform
# git clone https://github.com/prometheus/prometheus.git go-corpus/prometheus
# git clone https://github.com/gohugoio/hugo.git go-corpus/hugo

echo "Cloning C corpus..."
git clone https://github.com/curl/curl.git c-corpus/curl
# git clone https://github.com/FFmpeg/FFmpeg.git c-corpus/FFmpeg
# git clone https://github.com/torvalds/linux.git c-corpus/linux
# git clone https://github.com/git/git.git c-corpus/git
# git clone https://github.com/netdata/netdata.git c-corpus/netdata
# git clone https://github.com/antirez/redis.git c-corpus/redis

echo "Compute Go corpus..."
python go-corpus-build.py

echo "Compute C corpus..."
python go-corpus-build.py