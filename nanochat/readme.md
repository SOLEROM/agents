# nanochat

nanochat is the simplest experimental harness for training LLMs. It is designed to run on a single GPU node, the code is minimal/hackable, and it covers all major LLM stages including tokenization, pretraining, finetuning, evaluation, inference, and a chat UI

What the nanochat Model Actually Is
* A transformer-based causal language model trained for conversational use (“chat”).
* About 561 million parameters (a relatively small model compared to huge commercial LLMs).
* Designed to be trained and run efficiently (low compute cost) and freely available.
* It’s similar in style to models like GPT-2/GPT-Neo but built from a minimalist open-source codebase.


## deps

```
sudo apt-get install -y \
  git python3-pip python3-venv build-essential cmake pkg-config \
  libopenblas-dev libssl-dev libffi-dev
sudo apt-get install -y git-lfs
git lfs install
python3 -m pip install --user -U huggingface_hub


//uv
python3 -m pip install --user uv
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
echo 'export UV_NO_SYNC=1' >> ~/.bashrc
source ~/.bashrc
uv --version

//install NVIDIA’s Jetson wheel (CUDA-enabled)
uv pip uninstall -- -y torch torchvision torchaudio || true
wget raw.githubusercontent.com/pytorch/pytorch/5c6af2b583709f6176898c017424dc9981023c28/.ci/docker/common/install_cusparselt.sh 
nvcc --version ==>>> Build cuda_12.6
export CUDA_VERSION=12.4
bash ./install_cusparselt.sh
/// get version
cat /etc/nv_tegra_release ==> REVISION: 4.4
dpkg -l | grep -E 'nvidia-jetpack|nvidia-l4t' | head  ==> vidia-jetpack        6.2.1
python3 -V ==> Python 3.10.12
/// 
wget https://developer.download.nvidia.com/compute/redist/jp/v61/pytorch/torch-2.5.0a0+872d972e41.nv24.08.17622132-cp310-cp310-linux_aarch64.whl
export UV_SKIP_WHEEL_FILENAME_CHECK=1
uv pip install --no-cache-dir ./torch-2.5.0a0+872d972e41.nv24.08.17622132-cp310-cp310-linux_aarch64.whl

//nano
git clone https://github.com/karpathy/nanochat.git
cd nanochat
uv sync --no-install-package torch --no-install-package triton
// make sure torch is working and CUDA is available
uv run python -c "import torch; print(torch.__version__); print('cuda:', torch.cuda.is_available())"
```

### the model

* https://huggingface.co/sdobson/nanochat

```
mkdir -p ~/.cache/nanochat/chatsft_checkpoints
mkdir -p ~/.cache/nanochat/tokenizer
mkdir -p ~/.cache/nanochat/chatsft_checkpoints/d20

hf download sdobson/nanochat tokenizer.pkl token_bytes.pt   --local-dir ~/.cache/nanochat/tokenizer
hf download sdobson/nanochat model_000650.pt meta_000650.json   --local-dir ~/.cache/nanochat/chatsft_checkpoints/d20

UV_NO_SYNC=1 uv run python -m scripts.chat_web
UV_NO_SYNC=1 uv run python -m scripts.chat_web --host 0.0.0.0 --port 8000 --model-tag d20 --step 650


```

### wroking hash

```
cd ~/nanochat
git fetch --all --tags
# pick a date around the model release (Oct 13–15 2025)
HASH=$(git rev-list -n 1 --before="2025-10-15 00:00" origin/master)
echo "$HASH"
git checkout -b sdobson-compat "$HASH"

UV_NO_SYNC=1 uv run python -m scripts.chat_web --host 0.0.0.0 --port 8000 --model-tag d20 --step 650

//use from http://?.?.?.?:8000/


```

```
browser ──HTTP──> nanochat web server ──> PyTorch model ──> text tokens


scripts/chat_web.py
    starts a FastAPI / Starlette web server
    exposes a chat textbox
    User input → tokenized → fed to the GPT model
    Model outputs text only
    Text is streamed back to the browser
```
