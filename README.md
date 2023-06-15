AutoGPT4All is a simple bash script that sets up and configures [AutoGPT](https://github.com/Significant-Gravitas/Auto-GPT.git) running with the [GPT4All](#) model on the [LocalAI](https://github.com/go-skynet/LocalAI) server. This setup allows you to run queries against an open-source licensed model without any limits, completely free and offline.

> If you are interested in building decentralized applications, check out my other repo at [AwesomeAlgorand](https://github.com/aorumbayev/awesome-algorand).

<p align="center">
    <img  src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Faorumbayev%2Fautogpt4all&countColor=black&style=flat" />
    <a target="_blank" href="https://github.com/aorumbayev/autogpt4all"><img src="https://img.shields.io/github/stars/aorumbayev/autogpt4all?color=black" /></a>
    <a target="_blank" href="https://github.com/aorumbayev/2Fautogpt4all/network/members"><img src="https://img.shields.io/github/forks/aorumbayev/autogpt4all?color=black" /></a>
</p>

## 🚀 Quickstart

```bash
git clone https://github.com/aorumbayev/autogpt4all.git && cd autogpt4all && chmod +x autogtp4all.sh && ./autogtp4all.sh
```

> ❗️ Please note this script has been primarily tested on MacOS with an M1 processor. It should work on Linux and Windows, but it has not been thoroughly tested on these platforms. If not on MacOS install git, goland and make before running the script

## 🎛️ Script Options

### `--custom_model_url`

Specify a custom URL for the model download step. By default, the script will use `https://gpt4all.io/models/ggml-gpt4all-l13b-snoozy.bin`.

Example:

```bash
./autogtp4all.sh --custom_model_url "https://example.com/path/to/model.bin"
```

### `--uninstall`

Uninstall the projects from your local machine by deleting the `LocalAI` and `Auto-GPT` directories.

Example:

```bash
./autogtp4all.sh --uninstall
```

> To recap the commands a `--help` flag is also available

## 💡 Notes

-   The script checks if the directories exist before cloning the repositories.
-   On macOS, the script installs `cmake` and `go` using `brew`.
-   If the `--uninstall` argument is passed, the script stops executing after the uninstallation step.

## 🎯 How to Run

After executing `./autogtp4all.sh`, the script configures everything needed to use AutoGPT in CLI mode.

To run the GPT4All model locally, use `cd LocalAI && ./local-ai --models-path ./models/ --debug`. The model will be available at `localhost:8080`.

Then, navigate to the `Auto-GPT` folder and run `./run.sh` to start the CLI.

## 🔧 Configuration

Please note, to simplify this script and setup, by default the downloaded model is renamed to `gpt-3.5-turbo` which serves as a base model that auto gpt expects for `FAST_LLM_MODEL` parameter.

## ⭐️ Stargazers

Special thanks to everyone who starred the repository ❤️

[![Stargazers repo roster for @aorumbayev/autogpt4all](https://reporoster.com/stars/light/aorumbayev/autogpt4all)](https://github.com/aorumbayev/autogpt4all/stargazers)
