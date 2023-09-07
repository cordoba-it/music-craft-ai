# Music Craft AI
A music tool for music composing (Work In Progress)

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   cd music-craft-ai
   ```

4. Create a new virtual environment:

   ```bash
   python -m venv venv
   . venv/bin/activate
   ```

5. Set env vars `OPENAI_API_KEY=sk-your-openapi-key;PYTHONUNBUFFERED=1`

6. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

7. Make a copy of the example environment variables file:

   ```bash
   cp .env.example .env
   ```

8. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

9. Install FastAPI

   ```console
   pip install fastapi
   ``` 
   
   <div class="termy">
       You will also need an ASGI server, for production such as <a href="https://www.uvicorn.org" class="external-link"
                                                                    target="_blank">Uvicorn</a> or <a href="https://github.com/pgjones/hypercorn" class="external-link" target="_blank">Hypercorn</a>.
   </div>

   ```console
   pip install "uvicorn[standard]"
   ```

10. Run the app:

   ```bash
   uvicorn app:app --reload
   ```

# AudioCraft

This project utilizes AudioCraft, a PyTorch library for high-quality audio generation using deep learning models.

## Prerequisites

- Python 3.9
- PyTorch 2.0.0
- FFmpeg (recommended)

## Installation

### Install PyTorch

If you don't have PyTorch installed, run the following command:

```shell
pip install 'torch>=2.0'
```

### Install PyMongo

```shell
pip install pymongo
```

### Install AudioCraft

To install the stable release of AudioCraft, run:

```shell
pip install -U audiocraft
```

If you prefer the development version:

```shell
pip install -U git+https://git@github.com/facebookresearch/audiocraft#egg=audiocraft
```

### Install FFmpeg (Optional but Recommended)

#### Ubuntu:

```bash
sudo apt-get install ffmpeg
```

#### Anaconda or Miniconda:

   ```bash
   conda install "ffmpeg<5" -c conda-forge
   ```

### Install Transformers (Required for MusicGen)

   ```shell
   pip install torchaudio transformers
   ```
   
You should now be able to access the app at [http://localhost:8000](http://localhost:5000)!

## Ableton

1. Install [ClyphX-Pro](https://isotonikstudios.com/product/clyphx-pro/)
2. TODO
