# AutoGPT4All

<div align="center">
<a href="https://github.com/aorumbayev/autogpt4all"><img src="https://ipfs.algonode.xyz/ipfs/bafybeigvns6nvxn4tdmnkzrlrao6ukohxkqzt2uv7zzvdqqlmo2nfvhi6q"></a>
</div>

<p align="center">
    <img  src="https://visitor-badge.glitch.me/badge?page_id=aorumbayev.awesome-algorand&right_color=black" />
    <a target="_blank" href="https://awesomealgo.com"><img src="https://img.shields.io/badge/url-website-black.svg" /></a>
    <a target="_blank" href="https://github.com/aorumbayev/awesome-algorand"><img src="https://img.shields.io/badge/url-repository-black.svg" /></a>
    <br />
    <a target="_blank" href="https://rss.com/podcasts/the-awesomealgo-podcast"><img src="https://img.shields.io/badge/podcast-rss-black.svg?color=gold" /></a>
    <a target="_blank" href="https://developer.algorand.org"><img src="https://img.shields.io/coincap/price-usd/algorand?color=teal" /></a>
    <a target="_blank" href="https://github.com/aorumbayev/awesome-algorand"><img src="https://img.shields.io/github/stars/aorumbayev/awesome-algorand?color=teal" /></a>
    <a target="_blank" href="https://github.com/aorumbayev/awesome-algorand/network/members"><img src="https://img.shields.io/github/forks/aorumbayev/awesome-algorand?color=gold" /></a>
</p>

A simple bash script to setup and configure [AutoGPT](https://github.com/Significant-Gravitas/Auto-GPT.git) running against [GPT4All]() model via [LocalAI](https://github.com/go-skynet/LocalAI) server on your local machine.

## Usage

1. Clone this repo
2. Run `./autogtp4all.sh` to start the server
   2.1 If needed run `chmod +x autogtp4all.sh` to make the script executable

> Please note this is a very simple PoC tested on MacOS with M2 processor. It should work on Linux and Windows as well but it's not tested.

### Optional Arguments

The script supports the following optional named arguments:

#### `--custom_model_url`

This argument allows you to specify a custom URL for the model download step. By default, the script will use `https://gpt4all.io/models/ggml-gpt4all-l13b-snoozy.bin`. If you wish to use a different URL, you can provide it as a parameter like so:

```bash
./autogtp4all.sh --custom_model_url "https://example.com/path/to/model.bin"
```

#### `--uninstall`

This argument will make the script delete the `LocalAI` and `Auto-GPT` directories, effectively uninstalling the projects from your local machine. To use this argument, simply include it when running the script:

```bash
./autogtp4all.sh --uninstall"
```

## Notes

-   The script checks if the directories exist before trying to clone the repositories, so it's safe to run even if you have already cloned them.
-   The script will install `cmake` and `go` using `brew` if it detects that you're on a macOS system.
-   If the `--uninstall` argument is passed, the script will stop executing after the uninstallation step.

## How to run

Upon execution of `./autogtp4all.sh` the script will have everything configured to use AutoGPT in cli mode.

To run GPT4All model locally now, simply run `cd LocalAI && ./local-ai --models-path ./models/ --debug`, model will become available at `localhost:8080`.

At this point navigate to `Auto-GPT` folder and run `./run.sh` to start the cli.

## Notes on configuration

Please note, to simplify this script and setup, by default the downloaded model is renamed to `gpt-3.5-turbo` which serves as a base model that auto gpt expects for `FAST_LLM_MODEL` parameter.
