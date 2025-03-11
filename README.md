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

```bash
$ whispy --help
Usage: whispy [OPTIONS]

  Simple program that transcribes audio when a hotkey is pressed. Once the
  program has started, these are the keys you can use:

          RIGHT_CTRL: Press and hold to start recording audio
          RIGHT_SHIFT: Press briefly while recording to translate transcript
          LEFT_SHIFT: Press briefly while recording to output email
          ESC: Press briefly while recording to cancel

Options:
  -m, --model [tiny|base|small|medium|large|turbo|tiny.en|base.en|small.en|medium.en]
                                  Whisper model to use.  [default: small]
  -l, --language [en|zh|de|es|ru|ko|fr|ja|pt|tr|pl|ca|nl|ar|sv|it|id|hi|fi|vi|he|uk|el|ms|cs|ro|da|hu|ta|no|th|ur|hr|bg|lt|la|mi|ml|cy|sk|te|fa|lv|bn|sr|az|sl|kn|et|mk|br|eu|is|hy|ne|mn|bs|kk|sq|sw|gl|mr|pa|si|km|sn|yo|so|af|oc|ka|be|tg|sd|gu|am|yi|lo|uz|fo|ht|ps|tk|nn|mt|sa|lb|my|bo|tl|mg|as|tt|haw|ln|ha|ba|jw|su|yue]
                                  Language to listen to.  [default: en]
  -t, --translate [en|zh|de|es|ru|ko|fr|ja|pt|tr|pl|ca|nl|ar|sv|it|id|hi|fi|vi|he|uk|el|ms|cs|ro|da|hu|ta|no|th|ur|hr|bg|lt|la|mi|ml|cy|sk|te|fa|lv|bn|sr|az|sl|kn|et|mk|br|eu|is|hy|ne|mn|bs|kk|sq|sw|gl|mr|pa|si|km|sn|yo|so|af|oc|ka|be|tg|sd|gu|am|yi|lo|uz|fo|ht|ps|tk|nn|mt|sa|lb|my|bo|tl|mg|as|tt|haw|ln|ha|ba|jw|su|yue]
                                  Language to translate to.  [default: no]
  -k, --openai-api-key TEXT       OpenAI API key. Only used for translations.
                                  [env: OPENAI_API_KEY]
  --help                          Show this message and exit.
```
