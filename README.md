<h1>
  <p align="center">
    <a href="https://github.com/gbbirkisson/whispy">
      <img src="logo.png" alt="Logo" height="128">
    </a>
    <br>whispy
  </p>
</h1>

<p align="center">
  Easy speech transcriptions using OpenAI <b>whis</b>per and <b>py</b>thon
</p>

<!-- vim-markdown-toc GFM -->

* [Installation](#installation)
* [Usage](#usage)

<!-- vim-markdown-toc -->

## Installation

```bash
pipx install -f git+https://github.com/gbbirkisson/whispy.git
```

## Usage

```
$ whispy --help
Usage: whispy [OPTIONS]

  Simple program that transcribes audio when a hotkey is pressed. Once the
  program has started, these are the keys you can use:

          RIGHT_CTRL: Press and hold to start recording audio
          RIGHT_SHIFT: Press briefly while recording to translate transcript
          LEFT_SHIFT: Press briefly while recording to output email
          ESC: Press briefly while recording to cancel

Options:
  -m, --model TEXT           Whisper model to use.  [default: small.en]
  -t, --translate TEXT       Language to translate to.  [default: norwegian]
  -k, --openai-api-key TEXT  OpenAI API key.  [env: OPENAI_API_KEY]
  --help                     Show this message and exit.
```
